import yfinance as yf 
import streamlit as st
import pandas as pd 

st.write(
"""
# Simple Stock Prize

Shown are stock **closing price** and ***volume*** of google!

"""

)

# define the ticker symmbol of google

tickerSymbool = 'GOOGL'   # 'AAPL' for apple

# get datas from this ticker
tickerData = yf.Ticker(tickerSymbool)

# get the historical prices for these ticker
tickerDF = tickerData.history(period='1d' , start='2014-1-12' , end = '2024-1-12')

# open high low close volume didvidends stock splits
st.write("""
## Closing Price
""")
st.line_chart(tickerDF.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDF.Volume)