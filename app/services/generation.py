import joblib
import os
import numpy as np
import pandas as pd


def generation(rubrics, name_org, org_address, rating):
    """ Travel time prediction """
    rubrics = str(rubrics)
    name_org = str(name_org)
    org_address = str (org_address)
    """# Load model
    #with open(os.path.join(os.path.dirname(__file__), "../ml/model/model_GB.pkl"), 'rb') as file:
    #    model = joblib.load(file)
    #    prediction = model.predict(data)
    #    prediction = pd.DataFrame(prediction, columns=['trip_duration_log_pred_gb'])
    #    predict_normal = np.exp(prediction['trip_duration_log_pred_gb'])-1
    #    result = pd.DataFrame({'trip_duration': predict_normal})"""
    
    result = name_org + " по адресу " + org_address + " - заведение на " + str(rating) + " звёзд!"
    return result