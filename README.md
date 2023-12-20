# Project:  Marvin
#  Audio categorization. Deep learning 
``` 
Artificial Intelligence  
Domain             : Audio recognition
Sub-Domain         : Audio categorization
Architectures      : Sequential
Application        : Voice recognition for the voice assistance
```
### The objective is to develop audio recognition for initiating commands with brief trigger words, specifically tailored for non-commercial voice assistants. The designated keyword for recognition is "Marvin."

### Description of data
The dataset for training encompasses audio snippets covering various conversational scenarios, including background noise, to enhance the model's ability to recognize "Marvin" amidst real-world conditions.

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
Test Script             : [test_AWS.py]
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

   ## Deployment using AWS Lambda

   Skip this step and go through to the 2 step.
   1. Go to use `` awscli`` in the repository and type the following commands. The lambda in the folder will be used to create a docker image and run the app.
      ```
      aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 362414735980.dkr.ecr.eu-west-1.amazonaws.com
      docker build -t marvin-predict .
      docker tag marvin-predict:latest 362414735980.dkr.ecr.eu-west-1.amazonaws.com/marvin-predict:latest
      docker push 362414735980.dkr.ecr.eu-west-1.amazonaws.com/marvin-predict:latest
      ```
   2. Go to use setup and test lambda service:
      ![photo_2023-12-20 19 15 45](https://github.com/Justlesia/voice_model/assets/61661122/81d95ff4-4f9b-4d3c-b670-544b2fce3441)
      ![photo_2023-12-20 19 15 35](https://github.com/Justlesia/voice_model/assets/61661122/465174b7-209c-4341-9777-961a60e75007)
      ![photo_2023-12-20 19 15 27](https://github.com/Justlesia/voice_model/assets/61661122/ab08e9ec-83b8-468f-9958-ed3c56499858)

   
   3. Now the app running at the address https://bjh5fym1el.execute-api.eu-west-1.amazonaws.com/test/predict.
      To test if the docker container was built properly and running, go to the test_aws.py 
      ```
      python test_AWS.py
      ```
      If the prediction services give prediction, the service app is working.

   
   
   
