import streamlit as st
import pandas as pd

data_youtube = pd.read_csv("data.csv")
data_youtube.rename(columns={'channel name': 'Creator Name'}, inplace=True)
# Define a function to suggest YouTube creators based on input category and country
def suggest_creators(category, country):
    filtered_data = data_youtube[(data_youtube['Category'] == category) & (data_youtube['Audience Country'] == country)]
    suggested_creators = filtered_data['Creator Name'].tolist()
    if suggested_creators:
        return suggested_creators
    else:
        return ['No creators found for the selected category and country.']

# Streamlit app
st.title("YouTube Creator Collaboration Suggestions")

# Select category and country
category = st.selectbox("Select Category:", data_youtube['Category'].unique())
country = st.selectbox("Select Country:", data_youtube['Audience Country'].unique())

# Button to suggest creators
if st.button("Suggest Creators"):
    suggested_creators = suggest_creators(category, country)
    if suggested_creators:
        st.write("Suggested YouTube Creators:")
        for creator in suggested_creators:
            st.write(f"- {creator}")
    else:
        st.write("No creators found for the selected category and country.")
