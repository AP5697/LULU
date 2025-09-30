# LULU Streamlit App — Files & Instructions

This textdoc contains a ready-to-use mini-project for a Streamlit web application (Python) simulating LULU UAE sales analytics. It includes:

* A sample synthetic dataset (`data/lulu_transactions_sample.csv`) — transactional, demographic, loyalty, and ad-budget fields (including ad categories: clothing, grocery, electronic).
* A Streamlit app (`app.py`) that loads the dataset, provides filters, KPIs, charts, and simple segmentation/loyalty analyses.
* `requirements.txt`, `.gitignore`, and a `README.md` with GitHub and Streamlit deployment instructions and commands.

> **How to use:** copy the file contents below into the files in a new repo and run the steps in `README.md`.

---

## File: data/lulu_transactions_sample.csv

```
transaction_id,date,store,store_city,customer_id,age,gender,nationality,loyalty_tier,loyalty_points,product_category,product_subcategory,quantity,unit_price,total_amount,payment_method,ad_campaign,ad_category,ad_budget_spend
T0001,2025-09-01,Al Barsha, Dubai,C001,28,F,India,Gold,1200,Grocery,Bakery,2,15.50,31.00,Credit Card,Back to School,Clothing,1200
T0002,2025-09-01,Abu Dhabi Mall, Abu Dhabi,C002,45,M,UAE,Silver,400,Clothing,Women Dresses,1,89.99,89.99,Cash,September Sale,Clothing,3000
T0003,2025-09-02,Sharjah City,C003,33,F,Philippines,Gold,900,Electronics,Headphones,1,59.99,59.99,Card,Audio Promo,Electronic,5000
T0004,2025-09-02,Al Barsha, Dubai,C004,22,M,India,Bronze,60,Grocery,Fresh Produce,5,3.40,17.00,Cash,Weekly Fresh,Grocery,800
T0005,2025-09-03,Al Ain,C005,39,F,Sri Lanka,Silver,520,Clothing,Men Shirts,2,25.00,50.00,Credit Card,Corporate Offer,Clothing,1500
T0006,2025-09-03,Abu Dhabi Mall, Abu Dhabi,C006,55,M,UAE,Platinum,2500,Electronics,Smartphone,1,499.00,499.00,Card,New Launch,Electronic,12000
T0007,2025-09-04,Al Barsha, Dubai,C001,28,F,India,Gold,1210,Grocery,Beverages,6,2.50,15.00,Credit Card,Back to School,Grocery,1200
T0008,2025-09-04,Sharjah City,C007,19,F,Jordan,Bronze,30,Clothing,Accessories,1,12.00,12.00,Cash,Student Discount,Clothing,400
T0009,2025-09-05,Al Ain,C008,46,M,Philippines,Silver,600,Electronics,TV,1,799.00,799.00,Card,TV Fest,Electronic,15000
T0010,2025-09-05,Al Barsha, Dubai,C009,31,M,India,Gold,1100,Grocery,Household,3,10.00,30.00,Card,Home Essentials,Grocery,1000
T0011,2025-09-06,Abu Dhabi Mall, Abu Dhabi,C010,27,F,Nepal,Silver,480,Clothing,Women Tops,2,29.99,59.98,Card,September Sale,Clothing,3000
T0012,2025-09-06,Al Barsha, Dubai,C011,63,M,UAE,Platinum,3200,Grocery,Medicinal,1,9.99,9.99,Cash,Senior Offer,Grocery,700
T0013,2025-09-07,Sharjah City,C012,24,F,India,Bronze,90,Electronics,Power Bank,1,19.50,19.50,Card,Accessories Week,Electronic,600
T0014,2025-09-07,Al Ain,C013,36,M,Pakistan,Silver,540,Grocery,Snacks,4,2.25,9.00,Cash,Snack Promo,Grocery,500
T0015,2025-09-08,Al Barsha, Dubai,C014,41,F,Sri Lanka,Gold,980,Clothing,Men Trousers,1,39.99,39.99,Card,Autumn Collection,Clothing,4000
T0016,2025-09-08,Abu Dhabi Mall, Abu Dhabi,C015,29,M,India,Silver,430,Electronics,Camera,1,299.99,299.99,Card,Photo Week,Electronic,8000
T0017,2025-09-09,Sharjah City,C016,52,F,Sudan,Gold,1300,Grocery,Dairy,2,4.75,9.50,Cash,Daily Dairy,Grocery,900
T0018,2025-09-09,Al Barsha, Dubai,C017,34,M,Philippines,Bronze,75,Clothing,Kids Wear,3,8.50,25.50,Card,Kids Promo,Clothing,1100
T0019,2025-09-10,Al Ain,C018,48,M,India,Silver,600,Electronics,Speaker,1,89.99,89.99,Cash,Audio Promo,Electronic,5000
T0020,2025-09-10,Abu Dhabi Mall, Abu Dhabi,C019,26,F,Jordan,Bronze,40,Grocery,Bakery,2,6.50,13.00,Card,Weekend Treats,Grocery,700
T0021,2025-09-11,Al Barsha, Dubai,C020,37,M,Pakistan,Gold,1005,Clothing,Sportswear,2,45.00,90.00,Card,Sports Week,Clothing,3500
T0022,2025-09-11,Sharjah City,C021,21,F,India,Bronze,25,Electronics,Accessories,2,7.99,15.98,Cash,Student Discount,Electronic,400
T0023,2025-09-12,Al Ain,C022,30,M,Sri Lanka,Silver,470,Grocery,Household,5,6.00,30.00,Card,Home Essentials,Grocery,1000
T0024,2025-09-12,Abu Dhabi Mall, Abu Dhabi,C023,44,F,Philippines,Gold,1100,Clothing,Women Shoes,1,79.99,79.99,Card,September Sale,Clothing,3000
T0025,2025-09-13,Al Barsha, Dubai,C024,58,M,UAE,Platinum,4000,Grocery,Premium Meat,2,25.00,50.00,Cash,Festive Meat,Grocery,2000
T0026,2025-09-13,Sharjah City,C025,32,F,Pakistan,Silver,500,Electronics,Wearable,1,149.99,149.99,Card,Health Tech,Electronic,6000
T0027,2025-09-14,Al Ain,C026,23,M,India,Bronze,55,Clothing,Men Shorts,2,15.00,30.00,Card,Summer Clearout,Clothing,900
T0028,2025-09-14,Al Barsha, Dubai,C027,35,F,Sri Lanka,Gold,950,Grocery,Fresh Produce,6,4.00,24.00,Cash,Weekly Fresh,Grocery,800
T0029,2025-09-15,Abu Dhabi Mall, Abu Dhabi,C028,42,M,India,Silver,460,Electronics,Home Appliance,1,129.99,129.99,Card,Appliance Offer,Electronic,9000
T0030,2025-09-15,Sharjah City,C029,27,F,Jordan,Bronze,20,Grocery,Beverages,2,3.00,6.00,Cash,Weekend Treats,Grocery,700
```

---

## File: app.py

```python
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
    # If clothing ad budget high but sales low -> recommend promo
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
```

---

## File: requirements.txt

```
streamlit
pandas
plotly
```

---

## File: .gitignore

```
__pycache__/
*.pyc
.env
.env.*
data/*.csv

# If you create venv
venv/
```

---

## File: README.md

````
# LULU UAE — Streamlit Sales Dashboard (Prototype)

This repo contains a sample Streamlit dashboard for LULU UAE sales analytics. It uses a synthetic sample dataset and provides filtering, KPIs, demographic views, loyalty overview, and a simple ad-budget vs sales analysis.

## Files
- `data/lulu_transactions_sample.csv` — sample CSV data
- `app.py` — Streamlit application
- `requirements.txt` — Python dependencies
- `.gitignore`

## Run locally
1. Clone the repo
```bash
git clone <your-repo-url>
cd <repo-folder>
````

2. (Optional) Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # mac/linux
venv\Scripts\activate     # windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run Streamlit

```bash
streamlit run app.py
```

Open the URL shown in the terminal (usually [http://localhost:8501](http://localhost:8501)).

## Upload to GitHub

1. Initialize git, add files, commit, and push:

```bash
git init
git add .
git commit -m "Initial LULU Streamlit prototype"
git branch -M main
git remote add origin git@github.com:<your-username>/<repo-name>.git
git push -u origin main
```

If you prefer HTTPS:

```bash
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

## Deploy to Streamlit Community Cloud

1. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) and sign in with your GitHub account.
2. Click "New app" → choose the repo and branch `main` → entry point `app.py`.
3. Deploy. Streamlit will install `requirements.txt` and launch the app.

## Next steps / extensions

* Replace sample CSV with a secure connection to your production warehouse (e.g., Snowflake, BigQuery, Redshift).
* Add authentication and role-based access.
* Add RFM/CLTV calculations and retention cohort analysis.
* Add A/B testing / campaign attribution and uplift modeling.

```

---

## Notes & Suggestions
- The CSV is intentionally small and synthetic; replace with your real transactional export with matching columns.
- For production: secure credentials using secrets manager and avoid committing `data/*.csv` to public repos ( `.gitignore` includes `data/*.csv`).

---

End of package.

*If you want, I can now:*
- produce a ready-to-copy GitHub repo zip
- expand the dataset to N rows (give me N) or create more realistic distributions
- add additional analytics: RFM scoring, CLTV, cohort charts, or automated email content for loyalty tiers

```
