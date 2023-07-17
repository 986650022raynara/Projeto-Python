import pandas as pd
import streamlit as st
import plotly

df = pd.DataFrame({
    'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2010-01-11', '2011-02-18', '2012-03-12', '2013-03-12', '2014-03-14', '2015-03-20', '2021-06-17']),
    'adjusted': [100, 101, 102, 50, 47, 39, 48, 75, 12, 35]
})

df.to_csv('prices.csv')

# Load the CSV file
df = pd.read_csv('prices.csv')

# Select the `date` and `adjusted` columns
df = df[['date', 'adjusted']]

# Plot the data
st.plotly_chart(df.plot.line(x='date', y='adjusted'))

# Select a stock
stock = st.selectbox('Select a stock:', df['symbol'].unique())

# Plot the data for the selected stock
st.plotly_chart(df[df['symbol'] == stock].plot.line(x='date', y='adjusted'))

# Show the table of data
st.table(df)


