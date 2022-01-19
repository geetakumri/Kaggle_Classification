curl --location --request POST 'http://127.0.0.1:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "ID":1,
    "LIMIT_BAL": "180000.0",
    "SEX": 2,
    "EDUCATION": 2,
    "MARRIAGE": 1,
    "AGE": 29,
    "PAY_0": 0,
    "PAY_2": 0,
    "PAY_3": -1,
    "PAY_4": 0,
    "PAY_5": 0,
    "PAY_6": 839.0,
    "BILL_AMT1": 0,
    "BILL_AMT2": 839.0,
    "BILL_AMT3": 0,
    "BILL_AMT4": 839.0,
    "BILL_AMT5": 10,
    "BILL_AMT6": 20,
    "PAY_AMT1": 54.0,
    "PAY_AMT2": 60.2,
    "PAY_AMT3": 65.2,
    "PAY_AMT4": 58.2,
    "PAY_AMT5": 60.2,
    "PAY_AMT6": 50.5
}'