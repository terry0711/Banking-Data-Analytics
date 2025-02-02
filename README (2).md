# Banking Data Analysis Project – American Express

## 🎯 Project Objectives
This project focuses on analyzing customer transactions, detecting fraudulent activities, and understanding spending behavior—critical areas for financial institutions like American Express.

### * Key Goals:**
- Analyze **customer spending patterns** to provide insights into purchasing behavior.
- Detect **fraudulent transactions** using a machine learning model.
- Visualize data using **SQL queries, Power BI, and Tableau dashboards**.

---

## **📂 Project Structure**
| 📂 Folder | 📌 Description |
|-----------|--------------|
| `data/` | Contains the dataset and cleaned data |
| `scripts/` | Python scripts for data preprocessing, EDA, and machine learning |
| `sql/` | SQL queries for banking insights |
| `dashboards/` | Power BI & Tableau dashboards |
| `README.md` | Project documentation |
| `requirements.txt` | Dependencies for running the project |

---

## **1 Data Collection & Preparation**
### 📥 Dataset
- **File:** `banking_transactions.csv`
- **Columns:** `Customer_ID, Transaction_Amount, Transaction_Type, Merchant_Category, Location, Transaction_Timestamp, Is_Fraud`
- **Fraud Rate:** 3% of transactions are labeled as fraud.

### Steps Performed:
1. **Data Cleaning & Preprocessing** (`data_preparation.py`)
   - Normalized `Transaction_Amount`
   - Converted `Transaction_Timestamp` to datetime
   - Encoded categorical variables (`Transaction_Type, Merchant_Category, Location`)
2. **Stored cleaned data in** `cleaned_transactions.csv`.

---

## **2️ SQL Data Analysis**
### **Key SQL Queries (Stored in `sql_queries.sql`)**
1. **Top Spending Categories**
   ```sql
   SELECT Merchant_Category, SUM(Transaction_Amount) AS Total_Spending
   FROM Transactions
   GROUP BY Merchant_Category
   ORDER BY Total_Spending DESC;
   ```
2. **Fraud Distribution by Location**
   ```sql
   SELECT Location, COUNT(*) AS Fraud_Cases
   FROM Transactions
   WHERE Is_Fraud = 1
   GROUP BY Location
   ORDER BY Fraud_Cases DESC;
   ```
3. **Peak Fraud Transaction Hours**
   ```sql
   SELECT strftime('%H', Transaction_Timestamp) AS Hour, COUNT(*) AS Fraud_Cases
   FROM Transactions
   WHERE Is_Fraud = 1
   GROUP BY Hour
   ORDER BY Hour;
   ```

---

## **3️ Exploratory Data Analysis (EDA)**
- **Visualized spending patterns & fraud trends** (`eda_analysis.py`)
- **Charts Created:**
  - Fraud vs. Non-Fraud Transactions (Bar Chart)
  - Spending Trends by Merchant Category (Box Plot)
  - Fraud Cases by Location (Heatmap)
  - Fraudulent Transactions Over Time (Line Chart)

---

## **4️ Fraud Detection Model (Machine Learning)**
- **Model:** Random Forest & XGBoost (`ml_model.py`)
- **Performance Metrics:**
  - Precision, Recall, F1-score, and AUC-ROC
  - Fraud Detection Accuracy: **85%+**

---

## **5️ Power BI / Tableau Dashboard**
- **Dashboards Stored in `dashboards/`**
- **Visuals Included:**
  - Spending Trends by Merchant Category
  - Fraud Distribution by Location (Heatmap)
  - Peak Fraud Transaction Hours (Line Chart)
  - High-Risk Customers (Table View)
  - Total Transactions vs. Fraud Cases (Pie Chart)

---

## ** How to Run the Project**
###  **Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```
###  **Step 2: Run Python Scripts**
```bash
python scripts/data_preparation.py
python scripts/eda_analysis.py
python scripts/ml_model.py
```
###  **Step 3: Run SQL Queries**
```bash
sqlite3 banking.db < sql/sql_queries.sql
```
or execute queries in **MySQL/PostgreSQL**.

### **Step 4: Open Dashboard in Power BI / Tableau**
- Import `banking_transactions.csv`
- Use SQL query results to create visualizations.

---

