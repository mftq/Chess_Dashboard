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

### --- ROW 1: Charts 1, 2, 3 --- ###
col1, col2, col3 = st.columns(3)

with col1:
    plt.figure(figsize=(4.5, 3))
    df['winner'].value_counts().plot(kind='bar', color=['skyblue', 'salmon', 'gray'])
    plt.title('1. Game Outcome Distribution')
    plt.xlabel('Winner')
    plt.ylabel('Number of Games')
    plt.tight_layout()
    st.pyplot(plt)

with col2:
    plt.figure(figsize=(4.5, 3))
    df['victory_status'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('2. Victory Status Distribution')
    plt.ylabel('')
    plt.tight_layout()
    st.pyplot(plt)

with col3:
    plt.figure(figsize=(4.5, 3))
    df['turns'].plot(kind='hist', bins=30, color='purple', edgecolor='black')
    plt.title('3. Distribution of Game Length (in Turns)')
    plt.xlabel('Number of Turns')
    plt.ylabel('Game Count')
    plt.tight_layout()
    st.pyplot(plt)

### --- ROW 2: Charts 4, 5, 6 --- ###
col4, col5, col6 = st.columns(3)

with col4:
    plt.figure(figsize=(4.5, 3))
    df['opening_name'].value_counts().head(10).sort_values().plot(kind='barh', color='teal')
    plt.title('4. Most Played Openings')
    plt.xlabel('Number of Games')
    plt.ylabel('Opening Name')
    plt.tight_layout()
    st.pyplot(plt)

with col5:
    plt.figure(figsize=(4.5, 3))
    df['rated'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue'])
    plt.title('5. Rated vs Unrated Games')
    plt.ylabel('')
    plt.tight_layout()
    st.pyplot(plt)

with col6:
    plt.figure(figsize=(4.5, 3))
    df['time_control'].value_counts().head(10).sort_values(ascending=True).plot(kind='barh', color='steelblue')
    plt.title('6. Most Played Time Controls')
    plt.xlabel('Number of Games')
    plt.ylabel('Time Control Format')
    plt.tight_layout()
    st.pyplot(plt)

### --- ROW 3: Chart 7 full width --- ###
st.markdown("---")
st.subheader("7. Game Length Vs Victory Method")
plt.figure(figsize=(8, 4))
median_turns = df.groupby('victory_status')['turns'].median().sort_values()
median_turns.plot(kind='bar', color='steelblue')
plt.xlabel('Victory Method')
plt.ylabel('Median Number of Turns')
plt.tight_layout()
st.pyplot(plt)

plt.show()
