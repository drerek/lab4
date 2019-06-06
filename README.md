# Using machine learning (ML) for prediction with open data-set

### Dataset:
Dataset getted from https://catalog.data.gov/dataset/nypd-complaint-data-historic

Description of dataset: https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i

### Parsed time:
From all dataset (~2gb) we select timeframe in 3 years: from 2007 to 2009 years, includes

### Methods:
AR method: https://en.wikipedia.org/wiki/Autoregressive_model

SARIMA method: https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average

HWES method: https://en.wikipedia.org/wiki/Exponential_smoothing


### Requirements
python3

statsmodels


### Results:

| Date       | Origin data | Autoregression predicted data | SARIMA predicted data | HWES_predicted_data |
|---         |---          |---                            |---                    |---                  |
12/22/2009|1194|1270|1223|1205
12/23/2009|1122|1291|1331|1205
12/24/2009|938|1276|1366|1205
12/25/2009|772|1315|1376|1205
12/26/2009|951|1218|1379|1205
12/27/2009|1091|1053|1379|1205
12/28/2009|1056|1139|1380|1205
12/29/2009|1048|1295|1379|1205
12/30/2009|1139|1288|1379|1205
12/31/2009|698|1249|1379|1205


### Conclusion
In our opinion, from all of methods that we tested, the best-resulted method is AR. This method predicted the closest value to origin value.