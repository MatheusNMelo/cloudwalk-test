# Technical Assessment: Fraud Detection & Anti-Fraud System
This project contains a comprehensive end-to-end solution for payment fraud detection, developed as a technical assessment for CloudWalk. The analysis and implementation are contained within the Jupyter Notebook (.ipynb).

Contents of the Notebook
Industry Analysis (Task 3.1): A detailed breakdown of the payments ecosystem, covering money and information flows, the roles of key players (Acquirers, Gateways, Sub-acquirers), and the dynamics of chargebacks vs. cancellations.

Exploratory Data Analysis (Task 3.2): A deep dive into transactional data to identify suspicious patterns, including behavioral velocity, entity risk history, and temporal fraud spikes.
Machine Learning Pipeline: Implementation of a FeatureETL class that handles automated feature engineering, including rolling 24-hour windows and entity diversity metrics. It evaluates multiple models (Logistic Regression, XGBoost, Random Forest), with the Random Forest model achieving an AUC-ROC of 0.928.

Hybrid Anti-Fraud System (Task 3.3): A production-ready engine that combines business rules (hard limits on amounts, blacklisted users, and transaction velocity) with the predictive ML model.

# How to Use the Model
The AntiFraudSystem is designed for real-time evaluation. You can pass a standard transaction payload to the engine to receive an automated recommendation.

# Example usage of the Anti-Fraud Engine
test_payload = {
  "transaction_id" : 2342357,
  "merchant_id" : 29744,
  "user_id" : 97051,
  "card_number" : "434505******9116",
  "transaction_date" : "2019-11-30T23:16:32.812632",
  "transaction_amount" : 373,
  "device_id" : 285475
}

# The engine returns a JSON-style recommendation
result = antifraud_engine.evaluate(test_payload)
print(result)
# Output: {'transaction_id': 2342357, 'recommendation': 'approve'}
