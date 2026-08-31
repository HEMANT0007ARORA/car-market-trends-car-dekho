"""
Car Market Trends Analysis - Car Dekho
Reproducible EDA using Pandas, NumPy and Matplotlib.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data/car_data.csv"

df = pd.read_csv(DATA_PATH)

# Basic inspection
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Frequency analysis
print("\nVehicle model counts:")
print(df["Car_Name"].value_counts())

print("\nFuel type counts:")
print(df["Fuel_Type"].value_counts())

# Derived metrics
df["Depreciation"] = df["Present_Price"] - df["Selling_Price"]
df["Retention"] = df["Selling_Price"] / df["Present_Price"]

print("\nHighest depreciation:")
print(df.loc[df["Depreciation"].idxmax()])

print("\nLowest depreciation:")
print(df.loc[df["Depreciation"].idxmin()])

print("\nPrice/year correlation:", df["Selling_Price"].corr(df["Year"]))
print("Price/km correlation:", df["Selling_Price"].corr(df["Kms_Driven"]))

# Core visualizations
plt.figure(figsize=(8, 4))
df["Year"].value_counts().sort_index().plot(kind="bar")
plt.title("Vehicles by Manufacturing Year")
plt.xlabel("Year")
plt.ylabel("Records")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
plt.scatter(df["Year"], df["Selling_Price"], alpha=0.6)
plt.title("Selling Price vs Manufacturing Year")
plt.xlabel("Year")
plt.ylabel("Selling Price (lakh)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
plt.scatter(df["Kms_Driven"], df["Selling_Price"], alpha=0.6)
plt.title("Selling Price vs Kilometres Driven")
plt.xlabel("Kilometres Driven")
plt.ylabel("Selling Price (lakh)")
plt.tight_layout()
plt.show()
