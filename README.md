# Readme

* Python 3
* Install `catergory_encoders` using pip install `pip install category_encoders`
* Install `scikit-learn` using pip install `pip install -U scikit-learn`

## NFT Price Predictor

### Introduction

This project aims to build a machine learning model to predict the price of NFTs based on their traits. The data from the Bored Ape Yatch Club collection is used to form the feature matrix (X) and the price data from Dune.xyz is used as the target vector (y). The model will be trained on this data to make predictions on NFT prices.

### Data Collection

The data for the project is collected from two sources. The NFT traits are collected from the IPFS server "https://ipfs.io/ipfs/QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/". The price data is collected by querying the Opensea data from "https://dune.com/home".

### Data Preparation

The collected data is then processed to create a dataframe that contains both the feature matrix (X) and the target vector (y). The dataframe is then split into a training set and a test set with an 80/20 split to allow for the model to be evaluated on unseen data.

### Model Building

A simple linear regression model is built to predict the price of the NFTs based on their traits. The model is trained using the training set data and the target vector (y).

### Conclusion

This project provides a simple example of how to build a machine learning model to predict the price of NFTs based on their traits. The model can be improved upon and made more complex to improve its accuracy. The use of a training and test set split allows for an evaluation of the model's performance on unseen data.

## Predicting Apartment Prices in Mexico City

In this project, I will demonstate how I build a machine learning model to predict the price of the apartment in Mexico city.
I will use jupyter notebook to wrangle the datasets contains data of housing price in Mexico city, build a data pipeline to fit the model, train the model and deploy the model.
All the original data can be find in "/data" folder.

1. The model only predict the price of the `apartment`. This can't be used to predict other type of real estate
2. I only train the model with value less than $100k to avoid outliers
3. After explore the data, there are some apartments have very large area so I will remove those as well to keep the data clean.

## 2015 Nepal Earthquake ML project help predict house condition after earthquake

In this project, I will use data from [2015 NEPAL Earthquake Data](https://eq2015.npc.gov.np/) to build a ML model using Logistic Regression and Decision Tree to predict the condition of buildings after the earthquake.
To use this notebook, please install catergory_encoders and scikit_learn libraries.

1. All the data is dowloaded from [2015 NEPAL Earthquake Data](https://eq2015.npc.gov.np/) and can be find in /csv_files folder.
2. Using both Logistic Regression and Decision Tree model to determine the best model to predict with highest accuracy.

Please contact me <robertbach.vietnam@outlook.com> if you have any questions.
