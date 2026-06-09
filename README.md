# 🤖 AI Customer Intelligence Platform

An AI-powered Customer Intelligence Platform built using **Python, Streamlit, Machine Learning, Pandas, Plotly, and Scikit-Learn**.

This platform helps businesses analyze customer behavior, predict churn risk, generate personalized recommendations, segment customers, and derive business insights using AI-driven analytics.

---

# 📌 Problem Statement

Businesses generate large amounts of customer data but often struggle to extract meaningful insights from it.

Traditional reporting systems provide static reports that fail to answer critical business questions such as:

* Which customers are likely to leave?
* Which customers generate the most revenue?
* What products should be recommended?
* How can customer retention be improved?
* Which customer groups require special attention?

This project addresses these challenges through Machine Learning and Interactive Business Analytics.

---

# 🚀 Features

## 📊 Dashboard

* Customer Analytics Dashboard
* Revenue Analysis
* Customer Demographics
* Spending Analytics
* Customer Category Analysis
* Interactive Charts
* KPI Cards
* Business Insights

---

## 🧠 Purchase Prediction

Predict customer purchase probability using:

* Customer Income
* Spending Score
* Monthly Visits
* Age

Features:

* Purchase Probability Analysis
* Product Recommendations
* Customer Summary
* AI Insights

---

## ⚠️ Churn Analytics

Machine Learning based churn prediction using:

* Random Forest Classifier

Features:

* Churn Risk Prediction
* Customer Retention Analysis
* Risk Visualization
* Retention Recommendations
* Customer Summary Report

---

## 👥 Customer Segmentation

Customer clustering using:

* K-Means Clustering

Features:

* Dynamic Segmentation
* Customer Group Identification
* Segment Visualization
* Download Segmentation Reports

---

## 🎁 Recommendation Engine

Generate personalized recommendations based on:

* Customer Income
* Spending Score
* Monthly Visits
* Customer Profile

Features:

* VIP Customer Recommendations
* Premium Customer Recommendations
* Budget Customer Recommendations
* AI Product Suggestions

---

## 📈 Insights Dashboard

Advanced analytics dashboard providing:

* Correlation Heatmaps
* Revenue Analysis
* City-Wise Analytics
* Customer Category Analysis
* Business Intelligence Reports
* AI Generated Insights

---

# 🛠 Technologies Used

| Technology   | Purpose                    |
| ------------ | -------------------------- |
| Python       | Core Programming           |
| Streamlit    | Web Application            |
| Pandas       | Data Processing            |
| NumPy        | Numerical Operations       |
| Plotly       | Interactive Visualizations |
| Scikit-Learn | Machine Learning           |
| Seaborn      | Heatmaps                   |
| Matplotlib   | Analytics Charts           |
| Joblib       | Model Serialization        |

---

# 📂 Project Structure

```text
AI_CUSTOMER_INTELLIGENCE_PLATFORM

│
├── .streamlit
│   └── config.toml
│
├── assets
│   └── styles.css
│
├── data
│   └── customers.csv
│
├── models
│   └── churn_model.pkl
│
├── outputs
│
├── pages
│   ├── 1_Dashboard.py
│   ├── 2_Purchase_Prediction.py
│   ├── 3_Churn_Analytics.py
│   ├── 4_Customer_Segmentation.py
│   ├── 5_Recommendation_Engine.py
│   └── 6_Insights_Dashboard.py
│
├── app.py
├── generate_dataset.py
├── train_models.py
├── requirements.txt
│
└── README.md
```

---

# 📊 Dataset Features

| Feature            | Description             |
| ------------------ | ----------------------- |
| customer_id        | Unique Customer ID      |
| name               | Customer Name           |
| age                | Customer Age            |
| gender             | Customer Gender         |
| city               | Customer City           |
| income             | Annual Income           |
| spending_score     | Spending Behavior Score |
| tenure             | Customer Loyalty        |
| monthly_visits     | Website Visits          |
| favorite_product   | Favorite Product        |
| favorite_category  | Preferred Category      |
| purchase_frequency | Purchase Count          |
| churn              | Churn Label             |

---

# 🤖 Machine Learning Models

## Random Forest Classifier

Used for:

* Customer Churn Prediction
* Customer Retention Analysis
* Risk Classification

---

## K-Means Clustering

Used for:

* Customer Segmentation
* Behavioral Analysis
* Customer Category Discovery

---

# ⚙ Installation

## Step 1: Clone Repository

```bash
git clone <repository-url>
```

## Step 2: Navigate to Project

```bash
cd AI_CUSTOMER_INTELLIGENCE_PLATFORM
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📊 Generate Dataset

Run:

```bash
python generate_dataset.py
```

This creates:

```text
data/customers.csv
```

containing customer analytics data.

---

# 🤖 Train Machine Learning Model

Run:

```bash
python train_models.py
```

This creates:

```text
models/churn_model.pkl
```

---

# ▶ Run Application

Start Streamlit:

```bash
streamlit run app.py
```

---

# 🎨 UI Features

* Premium Dark Theme
* Green & Gold Dashboard Design
* Interactive Plotly Charts
* AI Analytics Panels
* Sidebar Navigation
* Responsive Layout
* Downloadable Reports

---

# 📈 Business Benefits

This platform helps businesses:

* Understand customer behavior
* Predict customer purchases
* Reduce customer churn
* Improve customer retention
* Generate product recommendations
* Increase customer engagement
* Improve revenue opportunities

---

# 🔮 Future Enhancements

* Real-Time Database Integration
* Deep Learning Models
* Customer Sentiment Analysis
* Email Marketing Automation
* Cloud Deployment
* REST API Integration
* Live Customer Monitoring

---

# 👨‍💻 Developed By

**SAMEERA.SHAIK**

AI Customer Intelligence Platform

Built with:

* Artificial Intelligence
* Machine Learning
* Business Intelligence
* Customer Analytics
* Streamlit

---

# 📌 Conclusion

The AI Customer Intelligence Platform provides businesses with intelligent customer analytics through Machine Learning, Data Visualization, and Predictive Analytics.

The platform enables organizations to:

* Analyze customer behavior
* Predict future purchases
* Identify churn risks
* Generate recommendations
* Discover customer segments
* Improve business decision-making

By combining AI and Business Intelligence, organizations can make data-driven decisions that improve customer engagement and business growth.
