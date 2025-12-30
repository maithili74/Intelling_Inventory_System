# Intelligent Inventory System

## Project Overview

This project implements an end-to-end demand forecasting and inventory optimization system for product-level stock planning.
It combines machine learning-based demand forecasting with classical inventory management models to generate actionable reorder decisions, and presents the results through an interactive Streamlit dashboard.
The goal is to move beyond forecasting alone and create a decision-support system that helps determine when to reorder and how much to reorder for each product.

## Key Features

Product-level demand forecasting using XGBoost
Time-series feature engineering (lags, rolling statistics, calendar effects)
Inventory optimization using:
* Average Daily Demand
* Safety Stock
* Reorder Point
* Economic Order Quantity (EOQ)
* Max Stock Level
* ABC Classification
Automated reorder decision engine
Interactive Streamlit dashboard for inventory monitoring and decision support

## Methodology

1) Demand Forecasting
* Built an XGBoost regression model to forecast daily demand at the product level
* Engineered lag features, rolling averages, and date-based features
* Achieved approximately 32% MAPE on the test dataset

2️) Inventory Optimization

* Forecasted demand is used to compute:
* Average Daily Demand
* Demand Variability (Standard Deviation)
* Safety Stock
* Reorder Point
* Economic Order Quantity (EOQ)
* Maximum Stock Level
* ABC Classification based on demand contribution

3️) Inventory Decision Engine

A rule-based decision system determines:
* Whether a product needs to be reordered
* The recommended order quantity (EOQ)

Decision Logic:
If Current Inventory ≤ Reorder Point → REORDER NOW
Else → OPTIMAL

4️) Streamlit Dashboard

The dashboard allows users to:
* Select a product (single-store setup)
* View current inventory status
* See reorder recommendations
* Monitor safety stock, reorder point, and EOQ visually

## Tech Stack

* Programming Language: Python
* Libraries: Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Plotly
* Dashboard: Streamlit
* Environment: Jupyter Notebook, Anaconda
