import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set the page layout to wide
st.set_page_config(layout="wide")
st.title("Chess Games Dashboard")

# Load dataset
df = pd.read_csv('games.csv')  # Adjust path if needed

# Data preparation
df['rated'] = df['rated'].astype(str)
df['time_control'] = df['increment_code'].fillna('Unknown')

# Set Style
plt.style.use('ggplot')
sns.set_palette('pastel')

# Create 7 side-by-side columns
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    plt.figure(figsize=(3.5, 2.5))
    df['winner'].value_counts().plot(kind='bar', color=['skyblue', 'salmon', 'gray'])
    plt.title('1. Outcome')
    plt.xlabel('Winner')
    plt.ylabel('Games')
    plt.tight_layout()
    st.pyplot(plt)

with col2:
    plt.figure(figsize=(3.5, 2.5))
    df['victory_status'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('2. Victory Status')
    plt.ylabel('')
    plt.tight_layout()
    st.pyplot(plt)

with col3:
    plt.figure(figsize=(3.5, 2.5))
    df['turns'].plot(kind='hist', bins=30, color='purple', edgecolor='black')
    plt.title('3. Turns Distribution')
    plt.xlabel('Turns')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)

with col4:
    plt.figure(figsize=(3.5, 2.5))
    df['opening_name'].value_counts().head(10).sort_values().plot(kind='barh', color='teal')
    plt.title('4. Top Openings')
    plt.xlabel('Games')
    plt.ylabel('Opening')
    plt.tight_layout()
    st.pyplot(plt)

with col5:
    plt.figure(figsize=(3.5, 2.5))
    df['rated'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue'])
    plt.title('5. Rated vs Unrated')
    plt.ylabel('')
    plt.tight_layout()
    st.pyplot(plt)

with col6:
    plt.figure(figsize=(3.5, 2.5))
    df['time_control'].value_counts().head(10).sort_values(ascending=True).plot(kind='barh', color='steelblue')
    plt.title('6. Time Controls')
    plt.xlabel('Games')
    plt.ylabel('Format')
    plt.tight_layout()
    st.pyplot(plt)

with col7:
    plt.figure(figsize=(3.5, 2.5))
    median_turns = df.groupby('victory_status')['turns'].median().sort_values()
    median_turns.plot(kind='bar', color='steelblue')
    plt.title('7. Length vs Victory')
    plt.xlabel('Method')
    plt.ylabel('Median Turns')
    plt.tight_layout()
    st.pyplot(plt)

plt.show()
