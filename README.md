🚢 Titanic Survival Prediction



Project Overview



This is an end-to-end Machine Learning project that predicts whether a passenger survived the Titanic disaster or not.

The project includes data preprocessing, feature engineering, model training, and deployment using Streamlit.



\---



Dataset



The dataset contains information about passengers such as:



\- Pclass (Passenger Class)

\- Sex

\- Age

\- Fare

\- Embarked

\- SibSp \& Parch



\---



&#x20;Steps Performed



\- Data Cleaning \& Preprocessing

\- Handling Missing Values

\- Feature Engineering (FamilySize, IsAlone)

\- Exploratory Data Analysis (EDA)

\- Model Training using Gradient Boosting

\- Model Evaluation



\---



Model Used



\- Gradient Boosting Classifier



\---



Model Performance



\- Accuracy: \~80%+

\- ROC-AUC Score: \~0.77



\---



Deployment



The model is deployed using Streamlit to create an interactive web application.



\---



How to Run Locally



1\. Clone the repository

2\. Install dependencies

3\. Run the app



pip install -r requirements.txt

streamlit run app.py



\---



Project Structure



titanic-ml-project/

│

├── app.py

├── model.pkl

├── train.csv

├── requirements.txt

└── README.md



\---



&#x20;Key Insights



\- Female passengers had higher survival rates

\- Passengers in higher classes were more likely to survive

\- Fare and family size influenced survival



\---



Author



* Syed Kaysan Ul Islam

