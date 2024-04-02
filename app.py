import streamlit as st
import seaborn as sns
import yfinance as yf
import pandas as pd
import datetime

st.set_page_config(
    page_title="Stock Data Analysis",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="auto",
)

#title
st.title("Stock Data Analysis")
# Introduction
st.write("""
This web application allows users to explore stock prices and volumes. 
Select a stock symbol and a date range to see the closing prices and volumes.
""")

# Widget to select a stock symbol
ticker_symbol = st.selectbox("Select a Stock Symbol", ["AAPL", "GOOGL", "MSFT", "AMZN"])

# Widget to select a date range
start_date = st.date_input("Start Date", datetime.date(2020, 1, 1))
end_date = st.date_input("End Date", datetime.date.today())

# Check if the date range is valid
if start_date < end_date:
    # Use yfinance to fetch the stock data
    ticker_data = yf.Ticker(ticker_symbol)
    ticker_df = ticker_data.history(period='1d', start=start_date, end=end_date)

    # Display the closing prices and volume using line charts
    st.write("## Closing Price")
    st.line_chart(ticker_df.Close)
    
    st.write("## Volume")
    st.line_chart(ticker_df.Volume)

    st.write("## Raw Data")
    st.dataframe(ticker_df)
else:
    st.error("Error: End date must be after start date.")

