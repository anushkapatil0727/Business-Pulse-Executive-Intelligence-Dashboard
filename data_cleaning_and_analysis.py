import pandas as pd

# Load CSVs
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

# Merge datasets
orders_full = orders.merge(customers, on="customer_id", how="left")

# Convert date fields
orders_full["order_date"] = pd.to_datetime(orders_full["order_date"])
customers["signup_date"] = pd.to_datetime(customers["signup_date"])

# Feature engineering
orders_full["month"] = orders_full["order_date"].dt.to_period("M")

# Monthly Sales Summary
monthly_sales = orders_full.groupby("month")["total_value"].sum().reset_index()
monthly_sales["month"] = monthly_sales["month"].astype(str)

# RFM Segmentation
from datetime import datetime
snapshot_date = orders_full["order_date"].max() + pd.Timedelta(days=1)
rfm = orders_full.groupby("customer_id").agg({
    "order_date": lambda x: (snapshot_date - x.max()).days,
    "order_id": "count",
    "total_value": "sum"
}).reset_index()
rfm.columns = ["customer_id", "recency", "frequency", "monetary"]

# Save outputs
monthly_sales.to_csv("monthly_sales_summary.csv", index=False)
rfm.to_csv("rfm_summary.csv", index=False)

print("Data processing completed. Files saved.")
