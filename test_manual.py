# Importing necessary libraries from TensorFlow
import tensorflow.lite as tflite
from tensorflow.io import read_file
from tensorflow.audio import decode_wav
from tensorflow import squeeze, newaxis
from tensorflow.signal import stft
from tensorflow import abs
from tensorflow.nn import softmax

# Reading the audio file
x = './common_voice_ru_18851609.wav'
# Alternatively, you can use a different audio file
x = './silero_m_arvin_v4_cyrillic_b_bashkir_8000.wav'

# Reading the contents of the audio file
x = read_file(str(x))

# Decoding the audio file into waveform and obtaining sample rate
x, sample_rate = decode_wav(x, desired_channels=1, desired_samples=32000,)

# Squeezing the waveform to remove singleton dimensions
x = squeeze(x, axis=-1)
waveform = x

# Computing the spectrogram of the audio waveform
spectrogram = stft(x, frame_length=255, frame_step=128)

# Calculating the absolute values of the spectrogram
spectrogram = abs(spectrogram)

# Adding a new axis to the spectrogram
x = spectrogram[..., newaxis]
X = x[newaxis,...]

# Creating a TensorFlow Lite interpreter with the specified model path
interpreter = tflite.Interpreter(model_path='./marvin_voice.tflite')
interpreter.allocate_tensors()

# Obtaining the input and output indices of the interpreter
input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

# Setting the input tensor of the interpreter
interpreter.set_tensor(input_index, X)

# Invoking the interpreter to perform inference
interpreter.invoke()

# Obtaining the predictions from the output tensor of the interpreter
preds = interpreter.get_tensor(output_index)

# Printing the probability of the positive class (index 1) using softmax
print('probability - ', float(softmax(preds)[0, 1]))
