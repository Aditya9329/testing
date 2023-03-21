import numpy as np
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

def eval_metrics(actual , prediction):
    rmse = mean_squared_error(actual, prediction)
    mae = mean_absolute_error(actual, prediction)
    r2 = r2_score(actual, prediction)
    # print("RMSE:",rmse)
    # print("MAE:",mae)
    # print("r2-score:",r2)
    return rmse,mae,r2






    