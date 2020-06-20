import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple stock price app
""")
tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = 'id' , start = '2010-6-20' , end='2020-6-20')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
