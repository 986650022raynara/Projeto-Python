import pandas as pd
import streamlit as st

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


