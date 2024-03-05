import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
day = pd.read_csv("https://raw.githubusercontent.com/SweetieblueberryDart/bikesharing/main/day.csv")
hour = pd.read_csv("https://raw.githubusercontent.com/SweetieblueberryDart/bikesharing/main/hour.csv")

# Data preprocessing
day["dteday"] = pd.to_datetime(day["dteday"])
hour["dteday"] = pd.to_datetime(hour["dteday"])

day.rename(columns={
    "dteday": "dateday",
    "yr": "year",
    "mnth": "month",
    "temp": "temperature",
    "hum": "humidity",
    "cnt": "count"
}, inplace=True)

hour.rename(columns={
    "dteday": "dateday",
    "yr": "year",
    "mnth": "month",
    "temp": "temperature",
    "hum": "humidity",
    "cnt": "count",
    "hr": "hour"
}, inplace=True)

# Data visualization
st.title("Data Visualization of Bike Sharing Dataset")

# Sidebar
st.sidebar.title("Options")
plot_options = st.sidebar.selectbox("Choose a plot", ["Peminjaman Sepeda Per Jam (Holiday)", "Peminjaman Sepeda Per Jam (Non-Holiday)", "Peminjaman Sepeda Per Bulan", "Peminjaman Sepeda Tiap Jam"])

# Plotting
if plot_options == "Peminjaman Sepeda Per Jam (Holiday)":
    st.subheader("Total Peminjaman Sepeda Perjam (Holiday)")
    holiday_df = hour[hour['holiday'] == 1].groupby('hour')['count'].sum()
    plt.figure(figsize=(10, 6))
    plt.plot(holiday_df.index, holiday_df.values, marker='o', color='red')
    plt.title('Total Peminjaman Sepeda Perjam (Holiday)', fontsize=15)
    plt.xlabel('Jam', fontsize=12)
    plt.ylabel('Total Peminjaman Sepeda', fontsize=12)
    plt.xticks(range(24), fontsize=10)
    plt.grid(True)
    st.pyplot(plt)

elif plot_options == "Peminjaman Sepeda Per Jam (Non-Holiday)":
    st.subheader("Total Peminjaman Sepeda Perjam (Non-Holiday)")
    non_holiday_df = hour[hour['holiday'] == 0].groupby('hour')['count'].sum()
    plt.figure(figsize=(10, 6))
    plt.plot(non_holiday_df.index, non_holiday_df.values, marker='o', color='purple')
    plt.title('Total Peminjaman Sepeda Perjam (Non-Holiday)', fontsize=15)
    plt.xlabel('Jam', fontsize=12)
    plt.ylabel('Total Peminjaman Sepeda', fontsize=12)
    plt.xticks(range(24), fontsize=10)
    plt.grid(True)
    st.pyplot(plt)

elif plot_options == "Peminjaman Sepeda Per Bulan":
    st.subheader("Total Peminjaman Sepeda Per Bulan")
    monthly_counts = day.groupby('month')['count'].sum()
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_counts.index, monthly_counts.values, marker='o', color='purple')
    plt.title('Total Peminjaman Sepeda Per Bulan', fontsize=15)
    plt.xlabel('Bulan', fontsize=12)
    plt.ylabel('Total Peminjaman Sepeda', fontsize=12)
    plt.xticks(range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
    plt.grid(True)
    st.pyplot(plt)

elif plot_options == "Peminjaman Sepeda Tiap Jam":
    st.subheader("Total Peminjaman Sepeda Tiap Jam")
    hourly_counts = hour.groupby('hour')['count'].sum()
    plt.figure(figsize=(10, 6))
    plt.plot(hourly_counts.index, hourly_counts.values, marker='o', color='purple')
    plt.title('Total Peminjaman Sepeda Tiap Jam', fontsize=15)
    plt.xlabel('Jam', fontsize=12)
    plt.ylabel('Total Peminjaman Sepeda', fontsize=12)
    plt.xticks(range(24), fontsize=10)
    plt.grid(True)
    st.pyplot(plt)