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

The system of automatic state ambient air monitoring stations in Lithuania consists of 14 urban air quality monitoring stations operating in Vilnius, Kaunas, Klaipėda, Šiauliai, Panevėžys, Jonava, Kėdainiai, Naujoji Akmenė and Mažeikiai and 3 integrated monitoring stations operating in Aukštaitija, Žemaitija and Dzūkija National Parks.

Concentrations of the following pollutants are measured at automatic air quality monitoring stations: particulate matter PM10, fine particulate matter PM2.5, nitrogen oxides (NO2, NOx, NO), sulfur dioxide (SO2), carbon monoxide (CO), ozone (O3), benzene, mercury.
The tests and measurements shall be carried out in accordance with the requirements of Directives 2004/107/EC of the European Parliament and of the Council relating to arsenic, cadmium, mercury, nickel and polycyclic aromatic hydrocarbons in ambient air and 2008/50/EC on ambient air quality and cleaner air for Europe.

We will look at Atmosfer pressure measurements.

The data consists of files obtained from different sources(https://data.gov.lt/datasets/500/ ):

* Averages.csv - data air monitoring (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Averages/:format/csv)
* Quantity.csv - dictionary (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Quantity/:format/csv)
* QuantityUnits.csv - dictionary (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/QuantityUnits/:format/csv)
* Station.csv - dictionary (https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Station/:format/csv)

## Metrics of the Final Model
```
Final Model             : model.bin
Final DictVectorizer    : dv.bin
Final MinMaxScaler      : scaler.bin
MAE:                    : Val - 3,  Test - 6 
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
   
   
