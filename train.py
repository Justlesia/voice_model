# -*- coding: utf-8 -*-
"""martvin_audio_classification


to create audio recognition to small start word for non commercial voice assistant.
The word for recogintian is Marvin
"""

#!pip install -U -q tensorflow tensorflow_datasets

"""Load the libraries"""

import os
import pathlib
import numpy as np
from tensorflow.keras import layers
from tensorflow.keras import models
import soundfile as sf
import librosa
import librosa.display
from tensorflow import keras

import tensorflow as tf
from sklearn.utils.class_weight import compute_class_weight

# Set the seed value for experiment reproducibility.
seed = 42
tf.random.set_seed(seed)
np.random.seed(seed)

"""load precleaned dataset"""

DATASET_PATH = './wake-word-examples/train/'
data_dir = DATASET_PATH
# if not load the data https://drive.google.com/uc?export=download&id=11NAqQ-T2xRd1LHT3hhT7W94F15fn6dvn

"""The dataset's audio clips are stored in 2 folders corresponding to speech command:"""

def resample_audio(label):
  directory = data_dir+label
  audio_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.wav')]
  for file_path in audio_files:
    audio_signal, current_sampling_rate = librosa.load(file_path, sr=None)  # sr=None returns the native sampling rate

    # Set the target sampling rate
    target_sampling_rate = 16000

    # Resample the audio signal
    resampled_audio = librosa.resample(audio_signal, orig_sr = current_sampling_rate, target_sr = target_sampling_rate)

    path = 'resample/'+label+"/"
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
      os.makedirs(path)
    output_file_path = './resample/'+label+"/"+file_path.split('/')[-1]  # Replace this with the desired file path

    # Save the audio signal to a WAV file
    sf.write(output_file_path, data=resampled_audio, samplerate = target_sampling_rate)
  return "resample_audio done!"

label = 'not-wake-word'
#resample_audio(label)
label = 'wake-word'
#resample_audio(label)

"""Divided into directories this way, you can easily load the data using `keras.utils.audio_dataset_from_directory`.

The audio clips are 2 second or less at 16kHz. The `output_sequence_length=32000` pads the short ones to exactly 2 second (and would trim longer ones) so that they can be easily batched.
"""

DATASET_PATH = './resample'
data_dir = pathlib.Path(DATASET_PATH)

train_ds, val_ds = tf.keras.utils.audio_dataset_from_directory(
    directory=data_dir,
    batch_size=64,
    validation_split=0.2,
    seed=0,
    shuffle=True,
    output_sequence_length=32000,
    subset='both',
    )

label_names = np.array(train_ds.class_names)

"""Create massive of the labesto find the weights"""

labels_array = np.concatenate([y.numpy() for _, y in train_ds], axis=0)

"""The dataset now contains batches of audio clips and integer labels. The audio clips have a shape of `(batch, samples, channels)`."""

def squeeze(audio, labels):
  audio = tf.squeeze(audio, axis=-1)
  return audio, labels

train_ds = train_ds.map(squeeze, tf.data.AUTOTUNE)
val_ds = val_ds.map(squeeze, tf.data.AUTOTUNE)

"""brake data on test and val split"""

test_ds = val_ds.shard(num_shards=2, index=0)
val_ds = val_ds.shard(num_shards=2, index=1)

def get_spectrogram(waveform):
  # Convert the waveform to a spectrogram via a STFT.
  spectrogram = tf.signal.stft(
      waveform, frame_length=255, frame_step=128)
  # Obtain the magnitude of the STFT.
  spectrogram = tf.abs(spectrogram)
  # Add a `channels` dimension, so that the spectrogram can be used
  # as image-like input data with convolution layers (which expect
  # shape (`batch_size`, `height`, `width`, `channels`).
  spectrogram = spectrogram[..., tf.newaxis]
  return spectrogram



def make_spec_ds(ds):
  return ds.map(
      map_func=lambda audio,label: (get_spectrogram(audio), label),
      num_parallel_calls=tf.data.AUTOTUNE)

train_spectrogram_ds = make_spec_ds(train_ds)
val_spectrogram_ds = make_spec_ds(val_ds)
test_spectrogram_ds = make_spec_ds(test_ds)


for example_spectrograms, example_spect_labels in train_spectrogram_ds.take(1):
  break


"""Examine the spectrograms for different examples of the dataset:"""

"""## Build and train the model

Add `Dataset.cache` and `Dataset.prefetch` operations to reduce read latency while training the model:
"""

train_spectrogram_ds = train_spectrogram_ds.cache().prefetch(tf.data.AUTOTUNE)

val_spectrogram_ds = val_spectrogram_ds.cache().prefetch(tf.data.AUTOTUNE)
test_spectrogram_ds = test_spectrogram_ds.cache().prefetch(tf.data.AUTOTUNE)

# Assuming you have your features (X_train) and labels (y_train) ready

# Calculate class weights
class_weights = compute_class_weight('balanced', classes=np.unique(labels_array), y=labels_array)

# Convert class weights to a dictionary
class_weight_dict = dict(enumerate(class_weights))

input_shape = example_spectrograms.shape[1:]
print('Input shape:', input_shape)
num_labels = len(label_names)

# Instantiate the `tf.keras.layers.Normalization` layer.
norm_layer = layers.Normalization()
# Fit the state of the layer to the spectrograms
# with `Normalization.adapt`.
norm_layer.adapt(data=train_spectrogram_ds.map(map_func=lambda spec, label: spec))

"""Define model"""

def make_model(learning_rate = 0.01, dropout_rate = 0.1):
      model = models.Sequential([
          layers.Input(shape=input_shape),
          # Downsample the input.
          layers.Resizing(32, 32),
          # Normalize.
          norm_layer,
          layers.Conv2D(32, 3, activation='relu'),
          layers.Conv2D(64, 3, activation='relu'),
          layers.MaxPooling2D(),
          layers.Dropout(dropout_rate),
          layers.Flatten(),
          layers.Dense(128, activation='relu'),
          layers.Dropout(dropout_rate),
          layers.Dense(num_labels)
      ])
      model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate = learning_rate),
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'], sample_weight_mode=class_weight_dict,
        )

      return model

"""Cheakpoints"""

checkpoint = keras.callbacks.ModelCheckpoint(
    'Sequential_v1_{epoch:02d}_{val_accuracy:.3f}.h5',
    save_best_only = True,
    monitor = 'val_accuracy',
    mode = 'max')


"""Ceate final model"""

model = make_model()
EPOCHS = 15
history = model.fit(
train_spectrogram_ds,validation_data=val_spectrogram_ds,
epochs=EPOCHS,
callbacks =[checkpoint],)

"""Train the model over 15 epochs for demonstration purposes:

"""
model.save('model_v1.h5', save_format = 'h5')


# Load the pre-trained Keras model
loaded_model = keras.models.load_model('model_v1.h5')

# Convert the Keras model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(loaded_model)
tflite_model = converter.convert()

# Save the TensorFlow Lite model
with open('docker/marvin_voice.tflite', 'wb') as f_out:
    f_out.write(tflite_model)

# Load the TensorFlow Lite model and make predictions

