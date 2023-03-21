import pickle
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

def encoder_function(x_train,x_test):
    transformer = ColumnTransformer(transformers=[
    ('tnf1',OneHotEncoder(sparse=False,drop='first'),['sex','smoker','region'])
    ],remainder='passthrough')


    
    x_train_transformed = transformer.fit_transform(x_train)
    pickle.dump(x_train_transformed,open('ColumnTransformer.sav','wb'))
    x_test_transformed  = transformer.transform(x_test)
    # print(x_train_transformed)
    # print(x_test_transformed)
    return x_train_transformed, x_test_transformed