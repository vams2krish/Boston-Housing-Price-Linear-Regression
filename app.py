import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt


#Streamlit design

st.header("Boston House Prices")

st.subheader("Input Features")


#load the pickle files
predicted_price = pickle.load(open('artifacts/predicted_price.pkl','rb'))


def user_input_features(predicted_price):
    st.text("CRIM - per capita crime rate by town")
    CRIM = st.slider('CRIM', min_value=0.00632, max_value=88.9762, value=0.1)
    
    st.text("ZN - proportion of residential land zoned for lots over 25,000 sq.ft.")
    ZN = st.slider('ZN', min_value=0.0, max_value=100.0, value=11.0)

    st.text("INDUS - proportion of non-retail business acres per town.")
    INDUS = st.slider('INDUS', min_value=0.46, max_value=27.74, value=11.0)

    st.text("CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)")
    CHAS = st.slider('CHAS', min_value=0, max_value=1, value=0)

    st.text("NOX - nitric oxides concentration (parts per 10 million)")
    NOX = st.slider('NOX', min_value=0.385, max_value=0.871, value=0.5)

    st.text("RM - average number of rooms per dwelling")
    RM = st.slider('RM', min_value=0.0, max_value=8.78, value=6.0)

    st.text("AGE - proportion of owner-occupied units built prior to 1940")
    AGE = st.slider('AGE', min_value=3.561, max_value=100.0, value=65.0)

    st.text("DIS - weighted distances to five Boston employment centres")
    DIS = st.slider('DIS', min_value=1.1296, max_value=12.1265, value=5.0)

    st.text("RAD - index of accessibility to radial highways")
    RAD = st.slider('RAD', min_value=1, max_value=24, value=5)

    st.text("TAX - full-value property-tax rate per $10,000")
    TAX = st.slider('TAX', min_value=187, max_value=711, value=296)

    st.text("PTRATIO - pupil-teacher ratio by town")
    PTRATIO = st.slider('PTRATIO', min_value=12.6, max_value=22.0, value=15.0)

    st.text("B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town")
    B = st.slider('B', min_value=0.32, max_value=400.0, value=120.9)

    st.text("LSTAT - percent lower status of the population")
    LSTAT = st.slider('LSTAT', min_value=1.73, max_value=37.97, value=12.0)
    data = {
        'CRIM': CRIM,
        'ZN': ZN,
        'INDUS': INDUS,
        'CHAS': CHAS,
        'NOX': NOX,
        'RM': RM,
        'AGE': AGE,
        'DIS': DIS,
        'RAD': RAD,
        'TAX': TAX,
        'PTRATIO': PTRATIO,
        'B': B,
        'LSTAT': LSTAT
    }
    features = pd.DataFrame(data, index=[0])
    return features




input_df = user_input_features(predicted_price)

# Predict using the Linear Regression model
prediction = predicted_price.predict(input_df)



#Click Button 
if st.button("submit"):
    st.write(f"The predicted house price is ${prediction[0] * 1000:.2f}")


    





