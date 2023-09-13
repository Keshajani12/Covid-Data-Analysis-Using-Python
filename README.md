# COVID-19 Data Analysis with Python

This Python script analyzes COVID-19 data using the Pandas, NumPy, Matplotlib, Seaborn, and scikit-learn libraries. It loads COVID-19 data from a CSV file, cleans and preprocesses the data, performs exploratory data analysis (EDA), visualizes the data using various plots, and demonstrates a linear regression model to predict COVID-19 recovery rates.

# Table of Contents
1. Introduction
2. Installation
3. Usage
4. Data Source
5. Analysis and Visualization
6. Linear Regression Model
7. Screenshots

# Introduction
The COVID-19 pandemic has generated a vast amount of data, and this script allows you to explore and analyze COVID-19 data for different states/union territories in India. It covers the following tasks:

● Loading data from a CSV file.
● Data cleaning and preprocessing.
● Calculating active cases, death rates, and cured rates.
● Creating various plots using Matplotlib and Seaborn for data visualization.
● Implementing a linear regression model to predict COVID-19 recovery rates.

# Installation

1. Clone this repository:
git clone https://github.com/Keshajani12/Covid-Analysis-Using-Python.git

2. Navigate to the project directory:
cd covid-analysis

3. Install the required Python packages using pip:
pip install pandas numpy matplotlib seaborn scikit-learn

# Or

Download Zip and Install requirements.txt write command :
pip install -r requirements.txt

# Usage

1. Run the Python script:
python covid_analysis.py

2. The script will load the COVID-19 data, perform analysis, generate plots, and display them.

# Data Source

The COVID-19 data is loaded from the 'covid_19_india.csv' file. Ensure that the data file is present in the same directory as the script.

# Analysis and Visualization

● The script calculates active cases, death rates, and cured rates for each state/union territory.
● It creates line plots, bar plots, and scatter plots to visualize the data using Seaborn and Matplotlib.

# Linear Regression Model

● The script demonstrates a linear regression model using scikit-learn.
● It predicts COVID-19 recovery rates based on the number of deaths.
● Mean squared error (MSE) is calculated to evaluate the model's performance.

# Screenshots

