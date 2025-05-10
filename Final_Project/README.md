## 🗂️ NYC Crime Analysis — Final Project (2025)

Welcome to the final machine learning and clustering project under the repository Algorithms_DS. This notebook explores and analyzes NYC's crime patterns using arrest data to identify spatial hotspots and build predictive models for crime severity.

## 🎯 Objective

Predict the severity of crime (Felony, Misdemeanor, Violation) using classification models.

Discover crime hotspots using unsupervised KMeans clustering.

Perform in-depth analysis across age groups, boroughs, offense types, and temporal trends.

## 📂 Project Structure

![image](https://github.com/user-attachments/assets/d1daf96f-bb3e-4c29-b0d4-fb9b67cced88)


## 🔧 Technologies Used

Python

Pandas, NumPy, Matplotlib, Seaborn

Scikit-learn (Classification & Clustering)

Google Colab / Jupyter Notebook

## ⚙️ ML Workflow Summary

📌 Data Preprocessing

Dropped irrelevant columns (like ID keys and redundant fields).

Filtered nulls and cleaned age groups (e.g., <18 → 0-17).

Encoded categorical variables (sex, race, borough, age group).

## ✅ Supervised Learning

Models Used:

Decision Tree Classifier

Random Forest Classifier

Target: Crime severity (LAW_CAT_CD)

Evaluation: Accuracy, F1-score, Confusion Matrix, Class Report

## 🔍 Unsupervised Learning (KMeans Clustering)

Clustered arrests using Latitude and Longitude → spatial hotspots

Analyzed clusters by:

Borough dominance

Crime severity and offense type distribution

Monthly and weekday arrest trends

Age group breakdown

## 📊 Key Insights

Misdemeanors dominate the dataset, especially in Brooklyn and Queens.

Cluster 3 had the highest arrest volume across all views.

25–44 age group was most involved in crimes.

Crimes peaked on Wednesdays and Thursdays, dipped on weekends.

Random Forest achieved >92% F1-score and outperformed Decision Tree.

## 🌐 Future Deployment

To make this project accessible to departments:

📈 Deploy dashboard via Streamlit or Dash

🌍 Host APIs for real-time predictions using FastAPI

🔁 Connect to NYC Open Data APIs for live updates

🔒 Apply secure authentication & training documentation for usage

## 🚀 How to Run Locally

Clone the repo and navigate to the Final_Project/ folder

git clone https://github.com/Bhairavi-avt/Algorithms_DS.git
cd Algorithms_DS/Final_Project

Install dependencies:

pip install -r requirements.txt

Launch the notebook:

jupyter notebook Algo_for_DS_Final_Project.ipynb

📄 Dataset Source

https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc/about_data
