import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sidebar
st.sidebar.title("Welcome to Streamlit")
st.sidebar.text_input("Email Address")
st.sidebar.text_input("Password")
st.sidebar.button("Submit")
st.sidebar.radio("Professional Expert", ["Student", "Employee", "Other"])

# Load movies data into a DataFrame
movies_data = pd.read_csv("movies.csv") 

# Set page title and header
st.title("Movies Data Visualization")
st.header("Exploring movies data")

# Display the loaded movies data
st.subheader("Movies Data")
st.dataframe(movies_data)

# Visualize movie genres using a bar chart
genre_counts = movies_data["Genre"].value_counts()
st.subheader("Movie Genres using bar chart")
st.bar_chart(genre_counts)

# Visualize movie genres using a line chart
genre_counts = movies_data["Genre"].value_counts()
st.subheader("Movie Genres using line chart")
st.line_chart(genre_counts)

# Visualize movie genres using a area chart
genre_counts = movies_data["Genre"].value_counts()
st.subheader("Movie Genres using area chart")
st.area_chart(genre_counts)

# Show raw data as an option
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(movies_data)

# Visualize movie ratings using a histogram
st.subheader("Movie Ratings")
st.hist(movies_data["Rating"], bins=10)

# Visualize movie duration using a line chart
st.subheader("Movie Durations")
st.line_chart(movies_data["Duration"])
