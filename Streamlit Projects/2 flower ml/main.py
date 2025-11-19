# simple iris flower prediction

import streamlit as st 
import pandas as pd 
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write(
    """
# Simple Iris Flower Prediction App

This app predicts the Iris flower type
"""
)


#######--------> sidebar
st.sidebar.header('Wser Input Parameters')

def user_input_features():
    sepal_leangth = st.sidebar.slider('sepal length', 4.3,7.9,5.4)

#   4.3,7.9,5.4  , 4.3 => minimum value  , 7.9 max, 5.4 curr (default)
    sepal_width = st.sidebar.slider('sepal width', 2.0, 4.4, 3.4)
    petal_leangth = st.sidebar.slider('petal length',0.1,2.5,0.2)
    petal_width = st.sidebar.slider('petal width',0.1,2.5,0.2)

    data = {'sepal_leangth' : sepal_leangth,
            'sepal_width' : sepal_width,
            'petal_leangth' : petal_leangth,
            'petal_width' : petal_width
            }
    
    features = pd.DataFrame(data, index =[0])
    return features

df = user_input_features()

st.subheader('User Input Parameters')
st.write(df)

# random forest classifier
# loading iris datset ⬇️
iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proab = clf.predict_proba(df)

st.subheader('class lables and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])

st.subheader('Prediction Proability')
st.write(prediction_proab)





