import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
url = "https://raw.githubusercontent.com/shivamgoswami05/Netflix-Data-Analysis/main/netflix_titles.csv"
df = pd.read_csv(url)

# Display basic info
print("Initial Data:")
print(df.head())
print("\nData Info:")
print(df.info())

# Drop duplicates and handle nulls
df.drop_duplicates(inplace=True)
df.dropna(subset=['type', 'title', 'country', 'release_year', 'rating', 'duration'], inplace=True)

# Movies vs TV Shows
type_counts = df['type'].value_counts()
plt.figure(figsize=(6, 6))
type_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#99ff99'])
plt.title("Movies vs TV Shows")
plt.ylabel("")
plt.show()

# Top 10 countries by content
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(10, 5))
top_countries.plot(kind='bar', color='skyblue')
plt.title("Top 10 Countries by Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Content added over years
df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year
yearly_content = df['year_added'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
plt.plot(yearly_content.index, yearly_content.values, marker='o', color='orange')
plt.title("Content Added to Netflix Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()
plt.show()

# Most common durations (for movies only)
movies_df = df[df['type'] == 'Movie']
plt.figure(figsize=(10, 5))
movies_df['duration'].value_counts().head(10).plot(kind='bar', color='purple')
plt.title("Top 10 Most Common Movie Durations")
plt.xlabel("Duration")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
