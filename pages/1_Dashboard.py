import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

df = pd.read_csv("data/customers.csv")

# Filters

st.sidebar.header("Dashboard Filters")

city = st.sidebar.selectbox(
    "City",
    ["All"] + sorted(df["city"].unique())
)

gender = st.sidebar.selectbox(
    "Gender",
    ["All"] + sorted(df["gender"].unique())
)

if city != "All":
    df = df[df["city"] == city]

if gender != "All":
    df = df[df["gender"] == gender]

# Calculations

customers = len(df)

avg_income = int(
    df["income"].mean()
)

avg_spending = round(
    df["spending_score"].mean(),
    1
)

churn_rate = round(
    df["churn"].mean() * 100,
    2
)

df["revenue"] = (
    df["income"]
    * df["purchase_frequency"]
    * 0.05
)

revenue = int(
    df["revenue"].sum()
)

# Header

st.title("👑 AI Customer Intelligence Dashboard")

st.markdown("""

<div style="
border:2px solid #D4AF37;
padding:15px;
border-radius:15px;
background:#1B4332;
margin-bottom:20px;
">
<h3 style="color:#FFD700;">
Enterprise Customer Analytics Platform
</h3>

AI • Machine Learning • Business Intelligence

</div>
""", unsafe_allow_html=True)

# KPI CARDS

c1,c2,c3,c4,c5 = st.columns(5)

with c1:
    st.markdown(f"""
    <div style="
    background:#1B4332;
    border:2px solid #D4AF37;
    border-radius:12px;
    padding:20px;
    text-align:center;
    ">
    <h4 style="color:#FFD700;">👥 Customers</h4>
    <h2>{customers}</h2>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div style="
    background:#1B4332;
    border:2px solid #D4AF37;
    border-radius:12px;
    padding:20px;
    text-align:center;
    ">
    <h4 style="color:#FFD700;">💰 Income</h4>
    <h2>₹{avg_income:,}</h2>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div style="
    background:#1B4332;
    border:2px solid #D4AF37;
    border-radius:12px;
    padding:20px;
    text-align:center;
    ">
    <h4 style="color:#FFD700;">🛒 Spending</h4>
    <h2>{avg_spending}</h2>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div style="
    background:#1B4332;
    border:2px solid #D4AF37;
    border-radius:12px;
    padding:20px;
    text-align:center;
    ">
    <h4 style="color:#FFD700;">⚠️ Churn</h4>
    <h2>{churn_rate}%</h2>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown(f"""
    <div style="
    background:#1B4332;
    border:2px solid #D4AF37;
    border-radius:12px;
    padding:20px;
    text-align:center;
    ">
    <h4 style="color:#FFD700;">💵 Revenue</h4>
    <h2>₹{revenue:,}</h2>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Charts

left,right = st.columns(2)

with left:
    fig1 = px.histogram(
        df,
        x="age",
        title="Customer Age Distribution"
    )
    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with right:
    fig2 = px.pie(
        df,
        names="gender",
        hole=0.45,
        title="Gender Distribution"
    )
    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.markdown("---")

left,right = st.columns(2)

with left:
    fig3 = px.scatter(
        df,
        x="income",
        y="spending_score",
        color="gender",
        size="purchase_frequency",
        hover_name="name",
        title="Income vs Spending Score"
    )
    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with right:
    city_income = (
        df.groupby("city")["income"]
        .mean()
        .reset_index()
    )
    fig4 = px.bar(
        city_income,
        x="city",
        y="income",
        color="city",
        title="Average Income By City"
    )
    st.plotly_chart(
        fig4,
        use_container_width=True
    )

st.markdown("---")

st.subheader("📋 Customer Dataset")

st.dataframe(
df.head(30),
use_container_width=True
)

st.markdown("---")

st.markdown("""

<div style="
background:#1B4332;
border:2px solid #D4AF37;
padding:20px;
border-radius:15px;
">

<h3 style="color:#FFD700;">
🧠 AI Business Insights
</h3>

✅ Premium customers contribute most revenue

✅ High spending scores indicate strong purchase intent

✅ Customer retention programs can reduce churn

✅ Personalized recommendations improve conversion rates

✅ Monthly visits correlate with purchase frequency

</div>
""", unsafe_allow_html=True)
