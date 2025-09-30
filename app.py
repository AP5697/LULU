# app.py - Streamlit LULU Sales Dashboard

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="LULU UAE — Sales Dashboard", layout="wide")

@st.cache_data
def load_data(path="data/lulu_transactions_sample.csv"):
    df = pd.read_csv(path, parse_dates=["date"])
    return df

# Load
st.title("LULU UAE — Sales & Loyalty Analytics")
st.markdown("Interactive prototype dashboard: transactional + demographics + loyalty + ad-budget analysis.")

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
min_date = df.date.min()
max_date = df.date.max()
date_range = st.sidebar.date_input("Date range", [min_date, max_date])
selected_cities = st.sidebar.multiselect("Store city", sorted(df.store_city.unique()), default=sorted(df.store_city.unique()))
selected_categories = st.sidebar.multiselect("Product categories", sorted(df.product_category.unique()), default=sorted(df.product_category.unique()))
selected_loyalty = st.sidebar.multiselect("Loyalty tier", sorted(df.loyalty_tier.unique()), default=sorted(df.loyalty_tier.unique()))

# Apply filters
start_dt, end_dt = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
mask = (
    (df.date >= start_dt) &
    (df.date <= end_dt) &
    (df.store_city.isin(selected_cities)) &
    (df.product_category.isin(selected_categories)) &
    (df.loyalty_tier.isin(selected_loyalty))
)
filtered = df.loc[mask].copy()

# KPIs
st.subheader("Key metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Transactions", filtered.shape[0])
col2.metric("Total Sales (AED)", f"{filtered.total_amount.sum():,.2f}")
col3.metric("Avg. Order Value (AED)", f"{filtered.total_amount.mean():,.2f}")
col4.metric("Unique Customers", filtered.customer_id.nunique())

# Sales by category
st.subheader("Sales by Product Category")
sales_cat = filtered.groupby('product_category', as_index=False).total_amount.sum().sort_values('total_amount', ascending=False)
fig1 = px.bar(sales_cat, x='product_category', y='total_amount', title='Total Sales by Category', labels={'total_amount':'Sales (AED)'})
st.plotly_chart(fig1, use_container_width=True)

# Demographics: age and gender
st.subheader("Customer demographics")
col5, col6 = st.columns([2,3])
with col5:
    age_dist = filtered.age.dropna()
    if len(age_dist):
        fig_age = px.histogram(filtered, x='age', nbins=10, title='Age distribution')
        st.plotly_chart(fig_age, use_container_width=True)
    else:
        st.info("No age data for selected filters")

with col6:
    gender_counts = filtered.gender.value_counts().reset_index()
    gender_counts.columns = ['gender','count']
    if not gender_counts.empty:
        fig_gender = px.pie(gender_counts, names='gender', values='count', title='Gender split')
        st.plotly_chart(fig_gender, use_container_width=True)

# Loyalty analysis
st.subheader("Loyalty program overview")
loyalty_summary = filtered.groupby('loyalty_tier', as_index=False).agg(
    customers=('customer_id','nunique'),
    total_sales=('total_amount','sum'),
    avg_points=('loyalty_points','mean')
).sort_values('total_sales', ascending=False)
st.dataframe(loyalty_summary)

# Ad budget vs sales
st.subheader("Ad budget (by category) vs Sales")
ad_summary = filtered.groupby('ad_category', as_index=False).agg(
    ad_budget_spend_sum=('ad_budget_spend','sum'),
    sales=('total_amount','sum')
)
if not ad_summary.empty:
    fig_ad = px.scatter(ad_summary, x='ad_budget_spend_sum', y='sales', size='sales', text='ad_category', title='Ad budget vs Sales by Ad Category')
    st.plotly_chart(fig_ad, use_container_width=True)

# Transaction table + download
st.subheader("Transactions (sample)")
st.dataframe(filtered.reset_index(drop=True))

@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df_to_csv(filtered)
st.download_button("Download filtered data as CSV", data=csv, file_name='lulu_filtered.csv', mime='text/csv')

# Simple recommendation panel
st.sidebar.header("Quick recommendations")
if st.sidebar.button("Generate recommendations"):
    recs = []
    ad_vs_sales = ad_summary.set_index('ad_category') if not ad_summary.empty else None
    if ad_vs_sales is not None:
        for cat in ad_vs_sales.index:
            bud = ad_vs_sales.loc[cat,'ad_budget_spend_sum']
            sal = ad_vs_sales.loc[cat,'sales']
            if bud>5000 and sal<1000:
                recs.append(f"{cat}: High ad spend but low sales — consider review campaign creative or target.")
    if not recs:
        recs = ["No automated flags for current filter selection."]
    for r in recs:
        st.sidebar.write("- ", r)

st.markdown("---")
st.caption("Prototype app — extend with real data connection, authentication, and richer analyses (RFM, CLTV, uplift modeling, etc.)")
