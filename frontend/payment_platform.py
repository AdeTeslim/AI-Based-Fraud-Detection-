import streamlit as st
import requests

# Define the URL of your FastAPI prediction endpoint
API_URL = 'http://backend:8000/predict/'


logo_path = 'images/img.jpeg'  
st.image(logo_path, width=100)  
st.title('SecurePay: Online Payment Platform')


st.sidebar.header("SecurePay!")

st.write("""
## Welcome to SecurePay!

SecurePay is your reliable partner for secure online transactions, leveraging advanced machine learning method for fraud detection algorithms to ensure your payments are safe and sound. 

This platform was developed as part of our final year project to showcase our approach in creating secure, efficient, fraud detection payment solutions. It integrates cutting-edge fraud detection machine learning technology to safeguard transactions against fraudulent activities.

The modelling Dataset was gotten from: https://www.kaggle.com/datasets/jainilcoder/online-payment-fraud-detection

**Project Contributors:**
- Momodu Teslim Oluwaseun (20/2564)
- Achugwo Stephanie Chidumebi (20/1464)
- Nelson Davidson Oremiloluwa (19/0852)
- Bailey Chidera Akinlolu (20/3244)

""")

# Mapping of transaction types from string to their corresponding integer value
transaction_type_mapping = {
    'CASH_OUT': 1,
    'CASH_IN': 2,
    'PAYMENT': 3,
    'TRANSFER': 4,
    'DEBIT': 5
}

# Input fields for transaction details in the sidebar
with st.sidebar.form("payment_form", clear_on_submit=True):
    st.write("Please fill out the payment details:")
    
    # Displaying transaction types as a selectbox
    type_str = st.selectbox('Transaction Type', list(transaction_type_mapping.keys()), index=0)
    amount = st.number_input('Amount', min_value=1.0, step=1.0)
    oldbalanceOrg = st.number_input('Current Balance', min_value=0.0, step=1.0)
    newbalanceOrig = st.number_input('Balance After Transaction', min_value=0.0, step=1.0)
    oldbalanceDest = st.number_input('Recipient Old Balance', min_value=0.0, step=1.0)
    newbalanceDest = st.number_input('Recipient New Balance', min_value=0.0, step=1.0)
    
    # Submit Button
    submitted = st.form_submit_button("Process Payment")

if submitted:
    # Convert the selected transaction type string to its corresponding integer value
    type_int = transaction_type_mapping[type_str]
    
    # Prepare and send the transaction data to the FastAPI backend for fraud check
    transaction_data = {
        "type": type_int,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }
    # Assuming your API is accessible and CORS is configured correctly
    try:
        response = requests.post(API_URL, json=transaction_data)
        if response.status_code == 200:
            prediction = response.json()['prediction']
            if prediction == "fraudulent":
                st.sidebar.error("🚨 Fraud Alert! This transaction has been flagged as suspicious.")
            else:
                st.sidebar.success("✅ Transaction processed successfully. No fraud detected.")
        else:
            st.sidebar.error("An error occurred while processing the transaction. Please try again.")
    except requests.exceptions.RequestException as e:
        st.sidebar.error(f"Failed to connect to the fraud detection service: {e}")
