# load the model   
# make ready for the prediction

import joblib
import pandas as pd 
from src.feature_engineering import encoder_function

# generate prediction value
def predict(age,sex,bmi,children,smoker,region):
    
    # create in such a way so that it can be transformed
    k=['age','sex','bmi','children','smoker','region']
    
    v = [age,sex,bmi,children,smoker,region]
    
    # dictionary ready to the df create 
    dic = dict(list(zip(k,v)))

    # dataframe is ready so that columnTransformer can be applied properly
    df = pd.DataFrame(dic,index=[0])
    print(df)
    # getting path of the model 
    # model_path = '../saved_models/model.joblib'
    # loading the prediction model using above path 
    # prediction_model = joblib.load(model_path)
    #ready to predict the values
    # prediction = prediction_model.predict(data)
    # return prediction
