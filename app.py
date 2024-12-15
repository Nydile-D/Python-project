import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set up the Streamlit app
st.title("Network Intrusion Detection Data Visualization")

# File uploader for CSV files
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read the dataset
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df.head())  # Show the first few rows of the dataframe

    # Show basic statistics
    st.write("Basic Statistics:")
    st.write(df.describe())

    # Select a numerical column for plotting
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    selected_num_column = st.selectbox("Select a numerical column for visualization:", numerical_columns)

    # Histogram for the selected numerical column
    st.subheader(f"Histogram of {selected_num_column}")
    fig, ax = plt.subplots()
    ax.hist(df[selected_num_column], bins=30, color='blue', alpha=0.7)
    ax.set_title(f"Histogram of {selected_num_column}")
    ax.set_xlabel(selected_num_column)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    # Pie chart for the 'attack_cat' column (if it exists)
    if 'attack_cat' in df.columns:
        attack_counts = df['attack_cat'].value_counts()
        st.subheader("Attack Category Distribution")
        fig, ax = plt.subplots()
        ax.pie(attack_counts, labels=attack_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
        st.pyplot(fig)

    # Optionally, you can add more visualizations or analysis here
