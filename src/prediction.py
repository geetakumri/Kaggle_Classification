import pickle
import json


def perform_prediction(df_test):
    new_col_name = 'probability_of_being_default'
    df_drop_id = df_test.drop(["ID"], axis=1)

    loaded_model = pickle.load(open("src/finalized_model.pkl", "rb"))
    proba = loaded_model.predict_proba(df_drop_id)
    
    df_test[new_col_name] = [round(prob, 3) for prob in proba[:, 1].tolist()]
    prediction = df_test[['ID', new_col_name]]
    
    return 200, json.dumps({
            "ID": str(prediction.at[0,"ID"]),
            "probability_of_being_default": prediction.at[0,"probability_of_being_default"],
        })