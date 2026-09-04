import joblib
import pandas as pd

def premium_predict(data: dict):
    x = pd.DataFrame([data])
    
    if data['age'] <= 25:
        try:
            model1 = joblib.load('artifacts/young_gr_model.pkl')
            pred = model1.predict(x)
            return pred
        
        except Exception as e:

            print(type(e).__name__, e)
            raise e
    else:
        try:
            model2 = joblib.load('artifacts/rest_model.pkl')
            pred = model2.predict(x.drop('genetical_risk', axis = 1))
            return pred
        
        except Exception as e:

            print(type(e).__name__, e)
            raise e