# Demand Forecasting & Inventory Optimization System #

## Project Overview ##

This project implements an end-to-end demand forecasting and inventory optimization system for product-level stock planning.
It combines machine learning-based demand forecasting with classical inventory management models to generate actionable reorder decisions, and presents the results through an interactive Streamlit dashboard.

The goal is to move beyond forecasting alone and create a decision-support system that helps determine when to reorder and how much to reorder for each product.

# Key Features #
- Product-level demand forecasting using XGBoost
- Time-series feature engineering (lags, rolling statistics, calendar effects)
- Inventory optimization using:
   - Average Daily Demand
   - Safety Stock
   - Reorder Point
   - Economic Order Quantity (EOQ)
   - Max Stock Level
   - ABC Classification
- Automated reorder decision engine
- Interactive Streamlit dashboard for inventory monitoring and decision support

## Methodology ##

- Demand Forecasting: Built an XGBoost regression model for daily product-level demand forecasting, achieving ~32% MAPE on the test set.
- Inventory Optimization: Used forecasted demand to calculate key metrics like Safety Stock, Reorder Point, and Economic Order Quantity (EOQ).
- Inventory Decision Engine: Developed a rule-based engine that triggers reorder decisions when inventory falls below the reorder point and recommends optimal order quantities.
- Streamlit Dashboard: Created an interactive dashboard for monitoring inventory status and reorder recommendations.


## Tech Stack ##

- Programming Language: Python
- Libraries: Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Plotly
- Dashboard: Streamlit
- Environment: Jupyter Notebook, Anaconda

  ## Project Structure ##

  Personal Project
  ->Codes
    ->datapreprocess_model.ipynb
    ->inventory.ipynb
    ->decision_rule.ipynb
    ->frontend.py
  -> Datasets

## How to run ##

Install necessary dependencies: pip install pandas numpy scikit-learn xgboost streamlit matplotlib plotly
Run the Streamlit App: python -m streamlit run app.py
Open localhost: http://localhost:8501

## Results ##

- Achieved ~32% MAPE on demand forecasting
- Successfully translated forecasts into real-time inventory decisions
- Built a complete pipeline from data → model → optimization → dashboard
