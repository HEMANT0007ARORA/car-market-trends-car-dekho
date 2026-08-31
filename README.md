# 🚗 Car Market Trends Analysis — Car Dekho

A data analysis case study using the **Car Dekho vehicle dataset** to explore used-vehicle pricing, depreciation, vehicle characteristics, and market trends with Python.

## 📌 Project Overview

This project analyzes a dataset containing used-vehicle records and answers the 25 questions provided in the original Car Dekho data-analysis case study.

The analysis focuses on:

- Manufacturing-year trends
- Selling-price and present-price analysis
- Vehicle/model frequency
- Fuel-type distribution
- Seller and transmission patterns
- Vehicle ownership
- Depreciation
- Relationship between vehicle age, kilometres driven, and selling price
- Separate analysis of cars and two-wheelers

## 🎯 Business Questions

The project investigates questions such as:

- What manufacturing years are represented?
- What are the minimum and maximum selling prices?
- How many records are present?
- Are there missing values?
- How many unique vehicle models are present?
- Which vehicle is most frequently listed?
- How many CNG vehicles are present?
- How many vehicles are sold directly by individuals?
- How many automatic-transmission vehicles are present?
- Which vehicles have the highest and lowest depreciation?
- Which brands/models are less affected by depreciation?
- Does vehicle age or kilometres driven affect selling price?
- How many newer vehicles are present?
- What can be learned specifically about two-wheelers and cars?

## 📊 Dataset

| Attribute | Value |
|---|---:|
| Records | 301 |
| Original columns | 9 |
| Manufacturing years | 2003–2018 |
| Minimum selling price | ₹0.10 lakh |
| Maximum selling price | ₹35.00 lakh |
| Minimum kilometres driven | 500 |
| Maximum kilometres driven | 500,000 |
| Missing values | 0 |
| Unique vehicle models | 98 |

### Main columns

- `Car_Name`
- `Year`
- `Selling_Price`
- `Present_Price`
- `Kms_Driven`
- `Fuel_Type`
- `Seller_Type`
- `Transmission`
- `Owner`

> **Note:** The original notebook describes 98 “different vehicles”. Here this is presented as **98 unique vehicle models**, because the dataset contains cars as well as two-wheelers.

## 🔎 Key Findings

### Fuel Type

The supplied analysis reports:

- Petrol: **239**
- Diesel: **60**
- CNG: **2**

Petrol vehicles dominate the dataset.

### Vehicle Models

There are **98 unique vehicle models**.

The most frequently occurring model is:

**City — 26 records**

### Data Quality

The analysis confirms:

- 301 non-null records across the original columns
- No missing/null values

📉 Depreciation Analysis

Depreciation is calculated as:

```python
Depreciation = Present_Price - Selling_Price

Then save and push

In PowerShell:
...

📚 Project Type

Data Analysis / Exploratory Data Analysis (EDA)**

This project was developed as a Car Dekho data-analysis case study using the supplied dataset and original case-study questions.

👤 Author

**Hemant Arora**

GitHub: [HEMANT0007ARORA](https://github.com/HEMANT0007ARORA)

---

⭐ Explore the notebook, analysis script and generated charts to understand the complete analysis.
