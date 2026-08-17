# Technical Assessment: Fraud Detection & Anti-Fraud System

This project contains an end-to-end fraud detection solution developed as a technical assessment for CloudWalk.

- Notebook analysis: `clouwalk_test.ipynb`
- Script version of notebook logic: `cloudwalk_test.py`
- FastAPI endpoint: `app.py`

## Project Scope

1. Industry Analysis (Task 3.1)
A breakdown of acquiring flows, key players, and chargeback dynamics.

2. Exploratory Data Analysis (Task 3.2)
Pattern analysis on transactional behavior, entity history, and temporal fraud risk.

3. Machine Learning Pipeline
Feature engineering with rolling 24h metrics and entity diversity features, plus model benchmarking (Logistic Regression, XGBoost, Random Forest).

4. Hybrid Anti-Fraud System (Task 3.3)
Rule-based controls combined with ML scoring for recommendation output (`approve` or `deny`).

## Run the API

### 1) Install dependencies

```powershell
python.exe -m pip install fastapi uvicorn pandas numpy missingno plotly nbformat scikit-learn xgboost seaborn matplotlib
```

### 2) Start the server

```powershell
python.exe -m uvicorn app:app --host 127.0.0.1 --port 8001
```

## Test Endpoints from Terminal

### Health check

```powershell
Invoke-RestMethod -Method Get -Uri http://127.0.0.1:8001/health | ConvertTo-Json
```

Expected response:

```json
{"status":"ok"}
```

### Evaluate transaction

```powershell
$body = @{
  transaction_id = 1
  merchant_id = 29744
  user_id = 97051
  card_number = "434505******9116"
  transaction_date = "2019-11-30T23:16:32.812632"
  transaction_amount = 373
  device_id = 285475
} | ConvertTo-Json

Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8001/evaluate -ContentType "application/json" -Body $body | ConvertTo-Json
```

Example response:

```json
{"transaction_id":1,"recommendation":"approve"}
```

## Direct Python Usage (Without API)

```python
from cloudwalk_test import antifraud_engine

test_payload = {
    "transaction_id": 2342357,
    "merchant_id": 29744,
    "user_id": 97051,
    "card_number": "434505******9116",
    "transaction_date": "2019-11-30T23:16:32.812632",
    "transaction_amount": 373,
    "device_id": 285475,
}

result = antifraud_engine.evaluate(test_payload)
print(result)
```
