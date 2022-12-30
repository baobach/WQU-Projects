# Predicting Apartment Prices in Mexico City
In this project, I will demonstate how I build a machine learning model to predict the price of the apartment in Mexico city.
I will use jupyter notebook to wrangle the datasets contains data of housing price in Mexico city, build a data pipeline to fit the model, train the model and deploy the model.
All the original data can be find in "/data" folder.
# The premise

1. The model only predict the price of the `apartment`. This can't be used to predict other type of real estate
2. I only train the model with value less than $100k to avoid outliers
3. After explore the data, there are some apartments have very large area so I will remove those as well to keep the data clean.
4. Install `catergory_encoders` using pip install `pip install category_encoders`