
# Boston House Price Prediction

This project implements a linear regression model to predict house prices in Boston based on various features. It includes a Jupyter notebook for data analysis and model training, as well as a Streamlit app for interactive predictions.

## Key Components

- `House Prediction - Linear Regression.ipynb`: Jupyter notebook containing data analysis, model training, and evaluation
- `app.py`: Streamlit app for interactive house price predictions
- `BostonHousing.csv`: Dataset with Boston housing data
- `requirements.txt`: Required Python packages
- `setup.py`: Package setup file
- `Procfile` and `setup.sh`: Files for Heroku deployment

## Functionality

The notebook performs the following steps:
1. Loads and explores the Boston housing dataset
2. Preprocesses the data 
3. Splits data into training and test sets
4. Trains a linear regression model
5. Evaluates model performance
6. Visualizes results

The Streamlit app allows users to:
- Input housing features via sliders
- Get a predicted house price based on those inputs

## Usage

To run the Streamlit app locally:

```
pip install -r requirements.txt
streamlit run app.py
```

The app is also deployed on Heroku for online access.

## Model Performance

The linear regression model achieves:
- R-squared: 0.669
- Mean Squared Error: 24.29

Visualizations in the notebook show the model's predictive performance.
