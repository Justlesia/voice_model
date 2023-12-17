# Project:  Air quality data. Environmental and climate monitoring.
# Atmosfer pressure. Regression model.
``` 
Artificial Intelligence  
Domain             : Regression
Sub-Domain         : Time series 
Architectures      : GradientBoostingRegressor
Application        : Meteological domain
```

### Description of data

Audio generated dataset used for the all talks and the noises vs the world Marvin

## Metrics of the Final Model
```
Final Model             : model.
Final DictVectorizer    : dv.bin
Final MinMaxScaler      : scaler.bin
Accuracy :                    : Val - 3,  Test - 6 
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
Notebook                : [https://github.com/Justlesia/predict-atm-pressure/blob/main/notebook.ipynb]
Predict Script          : [https://github.com/Justlesia/predict-atm-pressure/blob/main/predict.py]
Train Script            : [https://github.com/Justlesia/predict-atm-pressure/blob/main/train.py]
Test Script             : [https://github.com/Justlesia/predict-atm-pressure/blob/main/test_docker.py]
Test Script             : [https://github.com/Justlesia/predict-atm-pressure/blob/main/test_heroku.py]
```

## Run the Model as is  
Steps to run the scripts/notebooks as is:

1. Clone the repo by running the following command:
   ```
   git clone https://github.com/Justlesia/predict-atm-pressure.git
   ```

2. Download data into the ./datasets:
   (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Averages/:format/csv)
   (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Quantity/:format/csv)
   (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/QuantityUnits/:format/csv)
   (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Station/:format/csv)


### Using Docker 
 
   1. Build and run the application using the commands:
      ```
      docker build -t predict . 
      docker run -it -p 9696:9696 predict:latest 
      ```
      
   2. Open another terminal/prompt and run test_docker.py  
      ``` 
      python test_docker.py
      ```
      If the prediction services gives prediction, then it means the docker container is working.
   
   
