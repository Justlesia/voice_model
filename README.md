# Project:  Marvin
#  Audio categorization. Deep learning 
``` 
Artificial Intelligence  
Domain             : Audio recognition
Sub-Domain         : Audio categorization
Architectures      : Sequential
Application        : Voice recognition for the voice assistance
```
### The purpose is to create audio recognition for small start words for noncommercial voice assistants.
The word for recognition is Marvin

### Description of data
Audio generated dataset used for all talks and the noises vs the world Marvin

## Metrics of the Final Model
```
Final Model             : marvin_voice.tflite
Accuracy :              : Val - 99,  Test - 98
``` 
## Tools / Libraries
```
Languages               : Python
Tools/IDE               : Anaconda
Libraries               : Keras, TensorFlow
Virtual Environment     : pipenv
```

## Scripts and Notebook:
```
Notebook                : [martvin_audio_classification.ipynb]
Predict Script          : [predict.py]
Train Script            : [train.py]
Test Script             : [test_manual.py]
Test Script             : [test.py]
```

## Run the Model as is  
Steps to run the scripts/notebooks as is:

1. Clone the repo by running the following command:
   ```
   git clone https://github.com/Justlesia/voice_model.git
   ```

2. Download data:

   https://drive.google.com/uc?export=download&id=11NAqQ-T2xRd1LHT3hhT7W94F15fn6dvn

### Using Docker 
 
   1. Build and run the application using the commands:
      ```
      docker build -t predict .
      docker run --rm -p 9696:8080 predict

      ```
      
   2. Open another terminal/prompt and run test_docker.py  
      ``` 
      python test.py
      ```
      If the prediction services give a prediction, then it means the docker container is working.
   
   
