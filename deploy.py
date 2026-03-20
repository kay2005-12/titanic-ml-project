import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Titanic Survival Prediction ")

# 🔹 User Input
Pclass = st.selectbox("Passenger Class", [1, 2, 3])
Sex = st.selectbox("Sex", ["Male", "Female"])
Age = st.slider("Age", 1, 80, 25)
Fare = st.number_input("Fare", 0.0, 500.0, 10.0)
Embarked = st.selectbox("Embarked", ["S", "C", "Q"])
SibSp = st.number_input("Siblings/Spouse", 0, 8, 0)
Parch = st.number_input("Parents/Children", 0, 6, 0)

# 🔹 Encoding
Sex = 1 if Sex == "Female" else 0
Embarked = {"S":0, "C":1, "Q":2}[Embarked]

# 🔹 Feature Engineering
FamilySize = SibSp + Parch + 1

# 🔹 Final Input
input_data = pd.DataFrame({
    'Pclass':[Pclass],
    'Sex':[Sex],
    'Age':[Age],
    'SibSp':[SibSp],
    'Parch':[Parch],
    'Fare':[Fare],
    'Embarked':[Embarked],
    'FamilySize':[FamilySize]
})

# 🔹 Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.success("Passenger Survived !!")
    else:
        st.error("Passenger Did Not Survive !!!")