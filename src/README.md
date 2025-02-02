# Banking Data Analysis Project – American Express

## 🎯 Project Objectives
- Analyze customer spending patterns.
- Detect fraudulent transactions using a machine learning model.
- Visualize data with SQL queries and dashboards in Power BI/Tableau.

## 📂 Project Structure
| Component | Description |
|-----------|------------|
| `data_preparation.py` | Cleans and preprocesses the transaction dataset. |
| `eda_analysis.py` | Analyzes trends, spending habits, and fraud patterns. |
| `ml_model.py` | Builds a fraud detection model to classify transactions. |
| `sql_queries.sql` | SQL queries to extract insights. |
| `banking_transactions.csv` | Synthetic dataset of banking transactions. |

## 🛠 How to Run the Project
### 1️⃣ Install Required Libraries
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```
### 2️⃣ Run Python Scripts in Order
```bash
python data_preparation.py
python eda_analysis.py
python ml_model.py
```
### 3️⃣ Run SQL Queries
Use any SQL database system to execute the queries from `sql_queries.sql`.

## 📌 Uploading to GitHub
```bash
git init
git add .
git commit -m "Banking Data Analysis Project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Banking-Data-Analysis.git
git push -u origin main
```

## 🚀 Next Steps
- Create a Power BI / Tableau Dashboard.
- Improve fraud detection accuracy with XGBoost.
- Deploy as a web app using Flask.

