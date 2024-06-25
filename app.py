import streamlit as st
import pickle
import pandas as pd


#Streamlit design

st.header("Boston House Prices")

st.subheader('Lets predict the house Prediction')
st.sidebar.header("Input Features")


#load the pickle files
model = pickle.load(open('artifacts/predicted_price.pkl','rb'))


def user_input_features(model):
    st.sidebar.text("CRIM - per capita crime rate by town")
    CRIM = st.sidebar.slider('CRIM', min_value=0.0, max_value=100.0, value=0.1)
    
    st.sidebar.text("ZN - proportion of residential land zoned for lots over 25,000 sq.ft.")
    ZN = st.sidebar.slider('ZN', min_value=0.0, max_value=100.0, value=11.0)

    st.sidebar.text("INDUS - proportion of non-retail business acres per town.")
    INDUS = st.sidebar.slider('INDUS', min_value=0.0, max_value=30.0, value=11.0)

    st.sidebar.text("CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)")
    CHAS = st.sidebar.slider('CHAS', min_value=0, max_value=1, value=0)

    st.sidebar.text("NOX - nitric oxides concentration (parts per 10 million)")
    NOX = st.sidebar.slider('NOX', min_value=0.0, max_value=1.0, value=0.5)

    st.sidebar.text("RM - average number of rooms per dwelling")
    RM = st.sidebar.slider('RM', min_value=0.0, max_value=10.0, value=6.0)

    st.sidebar.text("AGE - proportion of owner-occupied units built prior to 1940")
    AGE = st.sidebar.slider('AGE', min_value=0.0, max_value=100.0, value=65.0)

    st.sidebar.text("DIS - weighted distances to five Boston employment centres")
    DIS = st.sidebar.slider('DIS', min_value=0.0, max_value=15.0, value=5.0)

    st.sidebar.text("RAD - index of accessibility to radial highways")
    RAD = st.sidebar.slider('RAD', min_value=1, max_value=24, value=5)

    st.sidebar.text("TAX - full-value property-tax rate per $10,000")
    TAX = st.sidebar.slider('TAX', min_value=100, max_value=800, value=296)

    st.sidebar.text("PTRATIO - pupil-teacher ratio by town")
    PTRATIO = st.sidebar.slider('PTRATIO', min_value=10.0, max_value=30.0, value=15.0)

    st.sidebar.text("B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town")
    B = st.sidebar.slider('B', min_value=0.0, max_value=400.0, value=350.0)

    st.sidebar.text("LSTAT - percent lower status of the population")
    LSTAT = st.sidebar.slider('LSTAT', min_value=0.0, max_value=40.0, value=12.0)
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




input_df = user_input_features(model)

# Predict using the Linear Regression model
prediction = model.predict(input_df)



#Click Button 
if st.sidebar.button("submit"):
    st.write(f"The predicted house price is ${prediction[0] * 1000:.2f}")



