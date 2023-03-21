import numpy as np
import pickle
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
import joblib


# Create your views here.

# v = [age,sex,bmi,children,smoker,region]
def home(request):
    if request.method  == 'POST':
        age = request.POST['age']
        sex = request.POST['sex']
        bmi = request.POST['bmi']
        children = request.POST['children']
        smoker = request.POST['smoker']
        region = request.POST['region']

         # create in such a way so that it can be transformed
        k=['age','sex','bmi','children','smoker','region']
    
        v = [int(age),sex,float(bmi),int(children),smoker,region]
        
        # dictionary ready to the df create 
        dic = dict(list(zip(k,v)))
        print(dic)
        # dataframe is ready so that columnTransformer can be applied properly
        df = pd.DataFrame(dic,index=[0])
        print(df)
        
        
    
        # loading ColumnTransformer
        transformer = pickle.load(open('../ColumnTransformer/ft1.pickle','rb'))
        

        op = transformer.transform(df)
        print(op)


        model = joblib.load("../saved_models/model.joblib")
        prediction = model.predict(op)
        print("prediction=",prediction)

        prediction = int(prediction)
        # print(age,sex,bmi,children,smoker,region)
        # val={'age':age,'sex':sex,'bmi':bmi,'children':children,'smoker':smoker,'region':region}
        return render(request,'index.html',{'val':prediction})
    res = render(request,"index.html")
    return res 