import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# --------------------------------------------------

# PAGE CONFIG

# --------------------------------------------------

st.set_page_config(
    page_title="Churn Analytics",
    page_icon="⚠️",
    layout="wide"
)

# --------------------------------------------------

# HEADER

# --------------------------------------------------

st.title("⚠️ Customer Churn Analytics")

st.markdown("""
Analyze customer retention risk using Machine Learning.

This module predicts whether a customer is likely to leave and provides retention recommendations.
""")

st.markdown("---")

# --------------------------------------------------

# LOAD MODEL

# --------------------------------------------------

try:
    model = joblib.load(
        "models/churn_model.pkl"
    )

except Exception as e:
    st.error(
        f"Model Loading Error: {e}"
    )

    st.stop()

# --------------------------------------------------

# INPUT SECTION

# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    age = st.slider(
        "Customer Age",
        18,
        70,
        30
    )

    income = st.slider(
        "Customer Income",
        20000,
        150000,
        50000,
        step=1000
    )

    spending = st.slider(
        "Spending Score",
        1,
        100,
        50
    )

with col2:
    tenure = st.slider(
        "Customer Tenure (Years)",
        1,
        10,
        5
    )

    visits = st.slider(
        "Monthly Visits",
        1,
        50,
        10
    )

    purchase_frequency = st.slider(
        "Purchase Frequency",
        1,
        30,
        10
    )

st.markdown("---")

# --------------------------------------------------

# PREDICTION

# --------------------------------------------------

if st.button(
    "🔍 Analyze Churn Risk",
    use_container_width=True
):
    features = np.array([
        [
            age,
            income,
            spending,
            tenure,
            visits,
            purchase_frequency
        ]
    ])

    prediction = model.predict(
        features
    )[0]

    probability = model.predict_proba(
        features
    )[0][1]

    churn_score = round(
        probability * 100,
        2
    )

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=churn_score,
        title={
            "text":"Churn Risk (%)"
        },
        gauge={
            "axis":{
                "range":[0,100]
            }
        }
    ))

    fig.update_layout(
        height=400
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.metric(
        "Predicted Churn Probability",
        f"{churn_score}%"
    )

    st.progress(
        float(probability)
    )

    st.markdown("---")

    if prediction == 1:
        st.error(
            f"⚠️ HIGH CHURN RISK ({churn_score}%)"
        )

        st.warning("""
### Retention Recommendations

• Offer personalized discounts

• Provide loyalty rewards

• Send retention emails

• Conduct customer feedback surveys

• Assign relationship manager
""")

    else:
        st.success(
            f"✅ CUSTOMER LIKELY TO STAY ({100-churn_score:.2f}%)"
        )

        st.info("""
### Growth Recommendations

• Upsell premium products

• Offer membership plans

• Introduce referral programs

• Cross-sell related products

• Encourage long-term subscriptions
""")

    st.markdown("---")

    summary = pd.DataFrame({
        "Feature":[
            "Age",
            "Income",
            "Spending Score",
            "Tenure",
            "Monthly Visits",
            "Purchase Frequency"
        ],
        "Value":[
            age,
            income,
            spending,
            tenure,
            visits,
            purchase_frequency
        ]
    })

    st.subheader(
        "📋 Customer Analysis Summary"
    )

    st.dataframe(
        summary,
        use_container_width=True
    )

    st.success(
        "Churn Analysis Completed Successfully"
    )

