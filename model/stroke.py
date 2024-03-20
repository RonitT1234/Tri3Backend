#Importating Packages
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import pdb
import pickle
from sklearn.metrics import accuracy_score

class Stroke():
    #userInput=[pclass, sex, age, sibsp,fare]
    def predict(userInput):
        save_path = "logistic_regression_model_stroke.pkl"
        userInput = pd.DataFrame.from_dict([userInput])
        with open(save_path, 'rb') as model_file:
            loaded_model = pickle.load(model_file)
        stroke = loaded_model.predict_proba(userInput)[0]
        print(stroke)
        return stroke[1]
    
