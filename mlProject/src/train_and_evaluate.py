# categorical column encoding will done by encoding_function which is available in the 'feature_engineering.py'

# load training & testing file 
# train the algorithm
# save the metrics

import os
import argparse
import pandas as pd 
# import numpy as np 
# from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.model_selection import train_test_split
from get_data import read_params
from feature_engineering import encoder_function
from metrics_eval import eval_metrics
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

import joblib
import json

def training_and_evaluation(config_path):
    config = read_params(config_path)
    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    model_dir = config["model_dir"]
    n_estimators = config["estimators"]["RandomForestRegressor"]["params"]["n_estimators"]
    max_depth = config["estimators"]["RandomForestRegressor"]["params"]["max_depth"]
    max_leaf_nodes = config["estimators"]["RandomForestRegressor"]["params"]["max_leaf_nodes"]
    target = [config["base"]["target_col"]]
    train = pd.read_csv(train_data_path,sep=",")
    test = pd.read_csv(test_data_path,sep=",")
    y_train = train[target]
    y_test  = test[target]
    x_train = train.drop(target,axis=1)
    x_test  = test.drop(target,axis=1)
    # encoder_function - it will encode the categorical values into the numerical
    for_training,for_testing= encoder_function(x_train,x_test)
    print(for_training)
    print("testing=",for_testing.shape)
    print("training=",for_training.shape)
    print("hello")

    # algorithm training start
    print("Algoithm training phase start now ...")
    rf = RandomForestRegressor(
        n_estimators = n_estimators,
        max_depth    = max_depth,
        max_leaf_nodes = max_leaf_nodes
    )

    rf.fit(for_training,y_train)
    # algorithm training done 
    print("Algorithm trained successfully")
    prediction_qualites = rf.predict(for_testing)
    (rmse,mae,r2) = eval_metrics(y_test,prediction_qualites)
    # print("RMSE:",rmse)
    # print("MAE:",mae)
    # print("r2-score:",r2)

    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]

    with open(scores_file,"w") as f:
        scores={
            "rmse":rmse,
            "mae":mae,
            "r2-score":r2
        }
        json.dump(scores,f,indent=4)


    with open(params_file,"w") as f:
        params={
            "n_estimators":n_estimators,
            "max_depth":max_depth,
            "max_leaf_nodes":max_leaf_nodes
        }
        json.dump(params,f,indent=4)



    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")
    joblib.dump(rf, model_path)



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default='params.yaml')
    parsed_args = args.parse_args()
    training_and_evaluation(config_path=parsed_args.config)