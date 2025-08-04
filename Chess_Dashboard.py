import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set the page title
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

# Row 1: Outcome & Victory Status
col1, col2 = st.columns(2)

with col1:
    plt.figure(figsize=(6, 4))
    df['winner'].value_counts().plot(kind='bar', color=['skyblue', 'salmon', 'gray'])
    plt.title('1. Game Outcome Distribution')
    plt.xlabel('Winner')
    plt.ylabel('Number of Games')
    plt.tight_layout()
    st.pyplot(plt)

with col2:
    plt.figure(figsize=(6, 6))
    df['victory_status'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('2. Victory Status Distribution')
    plt.ylabel('')
    plt.tight_layout()
    st.pyplot(plt)

# Row 2: Turns Histogram & Most Played Openings
col3, col4 = st.columns(2)

with col3:
    plt.figure(figsize=(6, 4))
    df['turns'].plot(kind='hist', bins=30, color='purple', edgecolor='black')
    plt.title('3. Distribution of Game Length (in Turns)')
    plt.xlabel('Number of Turns')
    plt.ylabel('Game Count')
    plt.tight_layout()
    st.pyplot(plt)

with col4:
    plt.figure(figsize=(8, 5))
    df['opening_name'].value_counts().head(10).sort_values().plot(kind='barh', color='teal')
    plt.title('4. Most Played Openings')
    plt.xlabel('Number of Games')
    plt.ylabel('Opening Name')
    plt.tight_layout()
    st.pyplot(plt)

# Row 3: Rated vs Unrated & Time Controls
col5, col6 = st.columns(2)

with col5:
    plt.figure(figsize=(5, 5))
    df['rated'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue'])
    plt.title('5. Rated vs Unrated Games')
    plt.ylabel('')
    plt.tight_layout()
    st.pyplot(plt)

with col6:
    plt.figure(figsize=(8, 5))
    df['time_control'].value_counts().head(10).sort_values(ascending=True).plot(kind='barh', color='steelblue')
    plt.title('6. Most Played Time Controls')
    plt.xlabel('Number of Games')
    plt.ylabel('Time Control Format')
    plt.tight_layout()
    st.pyplot(plt)

# Row 4: Game Length vs Victory Method (full width)
st.markdown("---")
st.subheader("Game Length vs Victory Method")
plt.figure(figsize=(8, 5))
median_turns = df.groupby('victory_status')['turns'].median().sort_values()
median_turns.plot(kind='bar', color='steelblue')
plt.title('7. Game Length Vs Victory Method')
plt.xlabel('Victory Method')
plt.ylabel('Median Number of Turns')
plt.tight_layout()
st.pyplot(plt)

plt.show()
