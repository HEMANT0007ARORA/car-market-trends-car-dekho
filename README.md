# Car Market Trends Analysis — Car Dekho

A data-analysis case study based on the supplied **Car Dekho** dataset.

## Project objective

Analyze used-vehicle records to understand:

- manufacturing-year coverage
- selling-price range
- dataset size and missing values
- vehicle/model frequency
- fuel, seller and transmission mix
- depreciation and resale retention
- relationship between selling price, vehicle age/year and kilometres driven
- separate two-wheeler and car insights
- answers to the 25 questions in the original case study

## Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- PowerPoint

## Dataset snapshot

The supplied dataset contains **301 records and 9 original columns**. The source notebook shows:

- manufacturing years: **2003–2018**
- selling price: **₹0.10 lakh–₹35.00 lakh**
- present price: **₹0.32 lakh–₹92.60 lakh**
- kilometres driven: **500–500,000**
- missing values: **0**
- unique vehicle models: **98**
- fuel types: Petrol 239, Diesel 60, CNG 2
- most frequent model: **City (26 records)**

> Note: “98 different vehicles” in the original notebook is interpreted here as **98 unique vehicle models**, because the dataset includes cars, bikes and mopeds.

## Repository structure

```text
car-market-trends-car-dekho/
├── analysis.py
├── requirements.txt
├── data/
│   └── car_data.csv
├── notebook/
│   └── Car_Market_Trends_Analysis.ipynb
├── outputs/
│   └── charts/
├── presentation/
│   └── Car_Market_Trends_Analysis_Car_Dekho.pptx
└── screenshots/
    └── jupyter_analysis_*.png
```

## Run locally

```bash
pip install -r requirements.txt
python analysis.py
```

Or open the notebook:

```bash
jupyter notebook notebook/Car_Market_Trends_Analysis.ipynb
```

## Presentation

The `presentation/` folder contains the final case-study PPT covering the problem statement, methodology, analysis, visualizations, 25 case-study answers and conclusion.

## Data provenance

The CSV and Jupyter screenshots in this repository are the materials supplied for the case-study assignment. Analysis and presentation outputs were created from those materials.
