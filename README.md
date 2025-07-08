# Business Pulse – Executive Intelligence Dashboard

## 📊 Overview

This project simulates an executive-level business intelligence system for a multi-channel retail company using synthetic data. It covers full-stack analytics — from raw data ingestion to KPI generation and dashboard creation.

---

## 🎯 Project Objectives

* Create an end-to-end data pipeline using SQL + Python for analysis.
* Build a robust data model that supports executive insights.
* Enable dynamic visualization using Power BI/Tableau.
* Segment customers for targeting using RFM analysis.

---

## 📁 Repository Structure

```bash
BusinessPulse/
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── monthly_sales_summary.csv
│   └── rfm_summary.csv
├── scripts/
│   ├── data_cleaning_and_analysis.py
│   └── business_pulse_analysis.sql
├── visuals/
│   ├── dashboard_mockup_sales_by_region.png
│   ├── dashboard_mockup_rfm_segmentation.png
│   └── dashboard_mockup_executive_summary.png
├── README.md
└── requirements.txt
```

---

## 📦 Requirements

All dependencies can be installed via pip:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```
pandas==1.5.3
numpy==1.21.6
matplotlib==3.7.1
seaborn==0.12.2
sqlalchemy==1.4.46
```

---

## 🧠 Key Features

* Full ETL: Extract from CSV, clean & transform data
* RFM Segmentation logic for customer profiling
* Revenue analysis by region, time, and product
* SQL script for BI-style metrics & joins
* Mockup dashboards for Power BI/Tableau structure

---

## 🔧 Installation

1. Clone the repo

```bash
git clone https://github.com/anushkapatil0727/Business-Pulse-Executive-Intelligence-Dashboard.git
cd Business-Pulse-Executive-Intelligence-Dashboard
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run analysis scripts

```bash
python scripts/data_cleaning_and_analysis.py
```

---

## 🚀 Usage

* Use Python script to clean, merge, and engineer features.
* SQL queries can be used to run in PostgreSQL/Snowflake for BI pipelines.
* Visualizations created using matplotlib can be replicated in Tableau/Power BI.

---

## 📈 KPIs Tracked

* Total Monthly Revenue
* Revenue by Region
* Revenue by Product Category
* Customer Segments (via RFM)
* Repeat Purchase Rate
* Average Order Value (AOV)

---

## 📊 Dashboard Mockups

* `dashboard_mockup_sales_by_region.png`
* `dashboard_mockup_rfm_segmentation.png`
* `dashboard_mockup_executive_summary.png`

---

## ❓ Business Questions Answered

* What are the top-performing regions by revenue?
* Are there revenue dips or seasonal patterns over the year?
* Who are our most loyal customers?
* Which categories are driving the most sales?
* How many customers are repeat buyers?

---

## 🔍 Example Output

* Bar chart of Total Sales by Region
* RFM scatter plot colored by Frequency
* Monthly revenue time-series line chart

---

## 👩‍💻 Author

Anushka Patil
Data Analyst | Python | SQL | Data Cleaning | Data Wrangling 
[LinkedIn Profile](https://www.linkedin.com/in/anushkapatil272000/)

---

## 📬 Contributions Welcome

Feel free to fork this repo, raise issues or submit pull requests!



