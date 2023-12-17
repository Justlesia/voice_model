#!/usr/bin/env python
# coding: utf-8

import tensorflow.lite as tflite
from tensorflow.audio import decode_wav
from tensorflow import squeeze
from tensorflow import newaxis
from tensorflow.signal import stft
from tensorflow import abs
from tensorflow.nn import softmax
from tensorflow.io import read_file
import requests

# Load the TensorFlow Lite interpreter
interpreter = tflite.Interpreter(model_path='marvin_voice.tflite')
interpreter.allocate_tensors()


def predict(url):
    audio_data = requests.get(str(url), allow_redirects=True).content
    # Load an example audio file

    audio_data, sample_rate = decode_wav(audio_data, desired_channels=1, desired_samples=32000)
    audio_data = squeeze(audio_data, axis=-1)
    waveform = audio_data

    # Compute spectrogram
    spectrogram = stft(audio_data, frame_length=255, frame_step=128)
    spectrogram = abs(spectrogram)
    audio_data = spectrogram[..., newaxis]
    input_data = audio_data[newaxis, ...]

    # Set input tensor and make predictions
    input_index = interpreter.get_input_details()[0]['index']
    output_index = interpreter.get_output_details()[0]['index']
    interpreter.set_tensor(input_index, input_data)
    interpreter.invoke()

    # Get and display the softmax predictions
    predictions = interpreter.get_tensor(output_index)
    softmax_predictions = softmax(predictions)

    return float(softmax_predictions[0, 1])


def lambda_handler(event, context):
    url = event['url']
    pred = predict(url)
    result = {
        'probability': pred
    }

    return result




