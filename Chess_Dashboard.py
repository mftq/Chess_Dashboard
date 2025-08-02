import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set the page title
st.title("Chess Games Dashboard")

# Load dataset
df = pd.read_csv('games.csv')  # Adjust path if needed

# Data preparation
df['rated'] = df['rated'].astype(str)
df['time_control'] = df['increment_code'].fillna('Unknown')

# Set Style
plt.style.use('ggplot')
sns.set_palette('pastel')

# 1. Game Outcome Distribution
plt.figure(figsize=(6, 4))
df['winner'].value_counts().plot(kind='bar', color=['skyblue', 'salmon', 'gray'])
plt.title('1. Game Outcome Distribution')
plt.xlabel('Winner')
plt.ylabel('Number of Games')
plt.tight_layout()
st.pyplot(plt)

# 2. Victory Status Distribution
plt.figure(figsize=(6, 6))
df['victory_status'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('2. Victory Status Distribution')
plt.ylabel('')
plt.tight_layout()
st.pyplot(plt)

# 3. Distribution of Game Length (Turns)
plt.figure(figsize=(6, 4))
df['turns'].plot(kind='hist', bins=30, color='purple', edgecolor='black')
plt.title('3. Distribution of Game Length (in Turns)')
plt.xlabel('Number of Turns')
plt.ylabel('Game Count')
plt.tight_layout()
st.pyplot(plt)

# 4. Most Played Openings
plt.figure(figsize=(8, 5))
df['opening_name'].value_counts().head(10).sort_values().plot(kind='barh', color='teal')
plt.title('4. Most Played Openings')
plt.xlabel('Number of Games')
plt.ylabel('Opening Name')
plt.tight_layout()
st.pyplot(plt)

# 5. Rated vs Unrated Games
plt.figure(figsize=(5, 5))
df['rated'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue'])
plt.title('5. Rated vs Unrated Games')
plt.ylabel('')
plt.tight_layout()
st.pyplot(plt)

# 6. Most Played Time Controls
plt.figure(figsize=(8, 5))
df['time_control'].value_counts().head(10).sort_values(ascending=True).plot(kind='barh', color='steelblue')
plt.title('6. Most Played Time Controls')
plt.xlabel('Number of Games')
plt.ylabel('Time Control Format')
plt.tight_layout()
st.pyplot(plt)

# 7. Game Length Vs Victory Method
plt.figure(figsize=(8, 5))
median_turns = df.groupby('victory_status')['turns'].median().sort_values()
median_turns.plot(kind='bar', color='steelblue')
plt.title('7. Game Length Vs Victory Method')
plt.xlabel('Victory Method')
plt.ylabel('Median Number of Turns')
plt.tight_layout()
st.pyplot(plt)




