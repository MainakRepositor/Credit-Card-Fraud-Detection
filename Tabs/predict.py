"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Detection Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Artificial Neural Networks</b> for the Credit Card Fraud Detection.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    col1, col2, col3,col4 = st.columns(4)

    # Take input of features from the user.
    with col1:
        V1 = st.slider("V1", float(df["V1"].min()), float(df["V1"].max()))
        V2 = st.slider("V2", float(df["V2"].min()), float(df["V2"].max()))
        V3 = st.slider("V3", float(df["V3"].min()), float(df["V3"].max()))
        V4 = st.slider("V4", float(df["V4"].min()), float(df["V4"].max()))
        V5 = st.slider("V5", float(df["V5"].min()), float(df["V5"].max()))
        V6 = st.slider("V6", float(df["V6"].min()), float(df["V6"].max()))
        V7 = st.slider("V7", float(df["V7"].min()), float(df["V7"].max()))

    with col2:
        V8 = st.slider("V8", float(df["V8"].min()), float(df["V8"].max()))
        V9 = st.slider("V9", float(df["V9"].min()), float(df["V9"].max()))
        V10 = st.slider("V10", float(df["V10"].min()), float(df["V10"].max()))
        V11 = st.slider("V11", float(df["V11"].min()), float(df["V11"].max()))
        V12 = st.slider("V12", float(df["V12"].min()), float(df["V12"].max()))
        V13 = st.slider("V13", float(df["V13"].min()), float(df["V13"].max()))
        V14 = st.slider("V14", float(df["V14"].min()), float(df["V14"].max()))

    with col3:
        V15 = st.slider("V15", float(df["V15"].min()), float(df["V15"].max()))
        V16 = st.slider("V16", float(df["V16"].min()), float(df["V16"].max()))
        V17 = st.slider("V17", float(df["V17"].min()), float(df["V17"].max()))
        V18 = st.slider("V18", float(df["V18"].min()), float(df["V18"].max()))
        V19 = st.slider("V19", float(df["V19"].min()), float(df["V19"].max()))
        V20 = st.slider("V20", float(df["V20"].min()), float(df["V20"].max()))
        V21 = st.slider("V21", float(df["V21"].min()), float(df["V21"].max()))

    with col4:
        V22 = st.slider("V22", float(df["V22"].min()), float(df["V22"].max()))
        V23 = st.slider("V23", float(df["V23"].min()), float(df["V23"].max()))
        V24 = st.slider("V24", float(df["V24"].min()), float(df["V24"].max()))
        V25 = st.slider("V25", float(df["V25"].min()), float(df["V25"].max()))
        V26 = st.slider("V26", float(df["V26"].min()), float(df["V26"].max()))
        V27 = st.slider("V27", float(df["V27"].min()), float(df["V27"].max()))
        V28 = st.slider("V28", float(df["V28"].min()), float(df["V28"].max()))
    Amount = st.slider("Amount", float(df["Amount"].min()), float(df["Amount"].max()))
    
    
    # Create a list to store all the features
    features = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]

    # Create a button to predict
    if st.button("Detect"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score
        st.info("Detected Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.error("The Credit Card has a fraudulent transaction")
        else:
            st.success("The Credit Card is not fraudulent")

        # Print teh score of the model 
        st.write("The model used is trusted by analysts and has an accuracy of ", round((score*100)),"%")
