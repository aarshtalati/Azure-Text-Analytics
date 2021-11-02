# Azure Text Analytics


## Objective
In e-Commerce, customer reviews are crucial. Analyzing customer feedback and in turn, listening to customers can help increase upselling and cross-selling success rates substantially. It helps achieve better customer retention, improves net promotor score. Also, it reduces resources required to gain/maintain customers (e.g. advertising). Most importantly, it improves customer experience. This project aims to get rich insights from customer feedback.


## Introduction
This project reads data from csv file, translates text to English, removes personally identifiable information (PII) and performs sentiment analysis on customer reviews.


## _[Future state]_ Exploratory Data Analysis
- Understand seasonality
- Demand prediction


## _[Future state]_] Insights for business
- We could include the geolocation, timestamp of the review, price of the product, star rating etc. fields to get better insights into customer satisfaction.
- Interpolate customer ratings with business domains e.g. technical issue, purchase, transport, delivery, ease of use, etc.
- Could be useful to predict review score (star rating) for the customer's next purchase.


## _[Future state]_ Performance Metrics
- F1 score
- confusion matrix


## Challenges
- Pre-processing
    - Data Deduplication & record linkage
- Sarcasm in review might increase false negatives.

# Set up

## Create Virtual Python environment

```
$ cd setup
$ conda env create --file anaconda_azure_python.yml
$ conda activate azure_py9
```
## Generate Input CSV Data File
```
$ cd ../utils
$ python data_generator.py
```