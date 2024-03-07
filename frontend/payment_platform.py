import streamlit as st
import requests

# Define the URL of your FastAPI prediction endpoint
API_URL = 'http://backend:8000/predict/'


# logo_path = 'path_to_your_logo_image.png'  
# st.image(logo_path, width=200)  
# st.title('SecurePay: Online Payment Platform')


st.sidebar.header("SecurePay!")

# team_members = {
#     'Alice Johnson': 'path_to_alice_image.png',
#     'Bob Smith': 'path_to_bob_image.png',
#     'Charlie Davis': 'path_to_charlie_image.png',
#     'Dana Lee': 'path_to_dana_image.png',
#     'Evan Wright': 'path_to_evan_image.png',
# }
# for name, image_path in team_members.items():
#     st.sidebar.image(image_path, caption=name, width=100) 

# Team Introduction or Project Description in the main area
st.write("""
## Welcome to SecurePay!

SecurePay is your reliable partner for secure online transactions, leveraging advanced machine learning method for fraud detection algorithms to ensure your payments are safe and sound. Our team of dedicated professionals works tirelessly to provide you with a seamless payment experience.

This platform was developed as part of our final year project to showcase our skills in creating secure, efficient, and user-friendly online payment solutions. It integrates cutting-edge fraud detection technology to safeguard transactions against fraudulent activities.

**Why Choose SecurePay?**
- Advanced fraud detection
- User-friendly interface
- Secure and fast transactions
- Comprehensive support

We're committed to your safety and satisfaction. Trust SecurePay for your online transactions today!

**Project Contributors:**
- Alice Johnson
- Bob Smith
- Charlie Davis
- Dana Lee
- Evan Wright

This project is the culmination of our hard work, dedication, and collaboration. We hope SecurePay meets your online transaction needs effectively and securely.
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
