# validate method
# if req okay
# call predict get prediction create response and send response, and status code
# if req not okay
# create error response return response , and status code
import pandas as pd
import prediction

def data_handler(request):
    column_list = ['ID', 'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0',
       'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
       'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
       'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']

    df_test = pd.DataFrame(request, index=[0])
    missing_columns = [i for i in column_list if i not in request.keys()]

    if len(missing_columns) > 0:
        return 400, f"{missing_columns} are missing"
    else:
        return prediction.perform_prediction(df_test)