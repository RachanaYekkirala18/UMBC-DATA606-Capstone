# Stock Price Prediction Project

## Title and Author

**Project Title:** Stock Price Prediction

**Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang

**Author Name:** Your Name

**GitHub Profile:** [Link to your GitHub profile](#)

**LinkedIn Profile:** [Link to your LinkedIn profile](#)

**PowerPoint Presentation File:** [Link to the presentation file you created earlier](#)

**YouTube Video:** [Link to your YouTube video](#)

## Background

### What is it about?
This project aims to analyze stock price data and build a predictive model to forecast future stock prices based on historical data.

### Why does it matter?
Predicting stock prices is crucial for investors, traders, and financial analysts to make informed decisions, manage risks, and maximize returns.

### Research Questions:
- How can historical stock data be used to predict future stock prices?
- Which features are most influential in predicting stock prices?
- How accurate can our predictive model be?

## Data

### Data Sources:
The dataset is sourced from historical stock price records and trading data.

### Data Size:
Varies based on the dataset used; typically in the range of tens to hundreds of megabytes.

### Data Shape:
- Number of Rows: Example - 1,000
- Number of Columns: Example - 17

### Time Period:
The dataset may cover a specific range of dates, such as from 2010 to 2020.

### What does each row represent?
Each row represents a trading record for a specific stock at a particular time.

### Data Dictionary:
- `stock_id`: Integer, Identifier for the stock
- `date_id`: Integer, Date identifier
- `seconds_in_bucket`: Integer, Time in seconds within a minute
- `imbalance_size`: Float, Size of the order imbalance
- `imbalance_buy_sell_flag`: Integer, Flag for buy/sell imbalance (0 or 1)
- `reference_price`: Float, Reference price of the stock
- `matched_size`: Float, Size of matched orders
- `far_price`: Float, Far price
- `near_price`: Float, Near price
- `bid_price`: Float, Bid price
- `bid_size`: Float, Bid size
- `ask_price`: Float, Ask price
- `ask_size`: Float, Ask size
- `wap`: Float, Weighted average price
- `time_id`: Integer, Time identifier
- `row_id`: Integer, Row identifier
- `currently_scored`: Integer, Scoring flag (0 or 1)

### Target Variable:
The target variable for the ML model is `reference_price`.

### Features/Predictors:
Potential features include `stock_id`, `seconds_in_bucket`, `imbalance_size`, `imbalance_buy_sell_flag`, `matched_size`, `far_price`, `near_price`, `bid_price`, `bid_size`, `ask_price`, `ask_size`, `wap`.

## Exploratory Data Analysis (EDA)

### Data Exploration Steps:
- Focus on the target variable (`reference_price`) and the selected features.
- Produce summary statistics of key variables.
- Create visualizations using libraries such as Plotly Express.

### Data Cleansing:
- Check for missing values and handle them appropriately.
- Check for duplicate rows and remove them.
- Consider splitting, merging, pivoting, or melting data if necessary.
- Evaluate the need for additional data sources to augment the dataset.

### Tidy Data:
- Ensure each row represents one observation.
- Ensure each column rep
