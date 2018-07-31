""" 1.0 Load and clean historical BTC-EUR price data """
import pandas as pd
import numpy as np
import calendar
import datetime
import math 

# Set column names for btc-eur price and volume data import
coinbase_btc_eur_cols = ['Time',
                   'BTC_price_EUR',
                   'Volume_BTC',
                    ]

# File source is 'http://api.bitcoincharts.com/v1/csv/' (14million rows)
# skiprows=10m for Jan '18, 8m for 22nd Dec '17, 4m for 12th Sep '17
coinbase_btc_eur = pd.read_csv('coinbase_BTC_EUR.csv', header=0, names=coinbase_btc_eur_cols, skiprows=0)

# Write a function to transform UNIX Timestamp into datetime format
# Note, could change strftime('%Y-%m-%d %H') to reduce granularity of data and not show minutes

def unix_to_datetime(i):
    u = datetime.datetime.fromtimestamp(
        int(i)
    ).strftime('%Y/%m/%d %H:%M')
    return u

# Apply unix_to_datetime function to every row in the coinbase_btc_eur dataframe
coinbase_btc_eur['Timestamp'] = coinbase_btc_eur["Time"].apply(lambda row: unix_to_datetime(row))

# Convert date in 'Timestamp' column from strftime to datetime (and set as index)
coinbase_btc_eur['Timestamp'] = pd.to_datetime(coinbase_btc_eur['Timestamp'], format="%Y/%m/%d %H:%M")
coinbase_btc_eur.index = coinbase_btc_eur['Timestamp']

""" 1.1 Convert data to OHLC """
# Convert point data into OHLC data 
ticks = coinbase_btc_eur.loc[:, ['BTC_price_EUR', 'Volume_BTC']]

# By 1h
bars_1h = ticks.BTC_price_EUR.resample('1h').ohlc()
volumes_1h = ticks.Volume_BTC.resample('1h').sum()

# By 4h
bars_4h = ticks.BTC_price_EUR.resample('4h').ohlc()
volumes_4h = ticks.Volume_BTC.resample('4h').sum()

# By 1d
bars_1d = ticks.BTC_price_EUR.resample('1d').ohlc()
volumes_1d = ticks.Volume_BTC.resample('1d').sum()

# Concatenate price (OHLC) and volume data

# By 1h
btc_eur_ohlc_1h = pd.concat([bars_1h, volumes_1h], axis=1)
btc_eur_ohlc_1h.dropna(inplace=True) 

# By 4h
btc_eur_ohlc_4h = pd.concat([bars_4h, volumes_4h], axis=1)
btc_eur_ohlc_4h.dropna(inplace=True)

# By 1d
btc_eur_ohlc_1d = pd.concat([bars_1d, volumes_1d], axis=1)
# btc_eur_ohlc_1d['Timestamp'] = btc_eur_ohlc_1d.index
btc_eur_ohlc_1d.dropna(inplace=True)

# Output files to csv
btc_eur_ohlc_1h.to_csv('btc_eur_ohlc_1h.csv')
btc_eur_ohlc_4h.to_csv('btc_eur_ohlc_4h.csv')
btc_eur_ohlc_1d.to_csv('btc_eur_ohlc_1d.csv')

print('Available datasets: \nbtc_eur_ohlc_1h\nbtc_eur_ohlc_4h\nbtc_eur_ohlc_1d')