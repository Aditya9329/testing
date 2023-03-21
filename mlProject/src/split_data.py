# split the data for training and testing
# save it into data/processed



import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params


def split_data_and_save_data(config_path):
    config = read_params(config_path)
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    training_data_path = config["split_data"]["train_path"]
    testing_data_path  = config["split_data"]["test_path"]
    test_size = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]
    # print("test_size=",test_size)
    # print("raw_data_path=",raw_data_path)
    # print("testing_data_path =",testing_data_path )
    # print("training_data_path=",training_data_path)
    df = pd.read_csv(raw_data_path,sep=",")
    train,test = train_test_split(df,
                                    test_size=test_size,
                                    random_state=random_state,
                                    )
    train.to_csv(training_data_path,sep=",",index=False)
    test.to_csv(testing_data_path,sep=",",index=False)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default='params.yaml')
    parsed_args = args.parse_args()
    split_data_and_save_data(config_path=parsed_args.config)

