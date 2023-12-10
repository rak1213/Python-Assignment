import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Question 3')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if 'Name' in df.columns and 'Age' in df.columns:
        st.write("Histogram of Ages:")
        fig, ax = plt.subplots()
        ax.hist(df['Age'], bins=10, edgecolor='black')
        ax.set_xlabel('Age')
        ax.set_ylabel('Frequency')
        ax.set_title('Age Distribution')
        st.pyplot(fig)
    else:
        st.error("Please upload a CSV file with 'Name' and 'Age' columns.")
