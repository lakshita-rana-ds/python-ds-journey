# ================
# DAY 14 - Week 2 Project - Full EDA on IPL Dataset
# DATE - 13 July, 2026
# STATUS - Done
# ================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ================================
# STEP 1: Load and inspect
# ================================
df = pd.read_csv("week2/matches.csv")

print(df.shape)
print(df.columns)
print(df.head())
df.info()
print(df.isnull().sum())

# ================================
# STEP 2: Investigate missing values before cleaning
# ================================
print(df[df["winner"].isnull()][["id", "season", "team1", "team2", "result"]])
print(df["method"].value_counts())
print(df[df["city"].isnull()][["id", "season", "venue"]].head(10))

# ================================
# STEP 3: Clean the data
# ================================
df.loc[df["venue"] == "Sharjah Cricket Stadium", "city"] = "Sharjah"
df.loc[df["venue"] == "Dubai International Cricket Stadium", "city"] = "Dubai"
print(df["city"].isnull().sum())

df["method"] = df["method"].fillna("Normal")
df["winner"] = df["winner"].fillna("No Result")
df["player_of_match"] = df["player_of_match"].fillna("No Result")

print(df.isnull().sum())
# result_margin, target_runs, target_overs left as NaN intentionally -
# they genuinely don't exist for no-result/tied matches

# ================================
# STEP 4: Analysis
# ================================

# Analysis 1: Most successful teams
top_teams = df["winner"].value_counts().head(10)
print(top_teams)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_teams.values, y=top_teams.index)
plt.title("Top 10 Teams by Number of Wins")
plt.xlabel("Wins")
plt.ylabel("Team")
plt.show()

# Analysis 2: Matches played per season
matches_per_season = df["season"].value_counts().sort_index()
print(matches_per_season)

plt.figure(figsize=(12, 5))
matches_per_season.plot(kind="bar", color="teal")
plt.title("Matches Played per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.xticks(rotation=45)
plt.show()

# Analysis 3: Does winning the toss help you win the match?
df["toss_match_same"] = df["toss_winner"] == df["winner"]
toss_win_rate = df["toss_match_same"].value_counts(normalize=True)
print(toss_win_rate)

# Analysis 4: Toss decision - bat or field first
toss_decision_counts = df["toss_decision"].value_counts()
print(toss_decision_counts)

sns.countplot(data=df, x="toss_decision")
plt.title("Toss Decision: Bat vs Field")
plt.show()

# Analysis 5: Top venues by matches hosted
top_venues = df["venue"].value_counts().head(10)
print(top_venues)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_venues.values, y=top_venues.index)
plt.title("Top 10 Venues by Matches Hosted")
plt.xlabel("Number of Matches")
plt.ylabel("Venue")
plt.tight_layout()
plt.show()

# ================================
# FINAL SUMMARY
# ================================
print("\n===== IPL EDA SUMMARY =====")
print(f"Total matches analyzed: {df.shape[0]}")
print(f"Seasons covered: {df['season'].nunique()}")
print(f"Most successful team: {df['winner'].value_counts().index[0]} ({df['winner'].value_counts().values[0]} wins)")
print(f"Most used venue: {df['venue'].value_counts().index[0]}")
print(f"Toss winner also match winner: {round(toss_win_rate[True]*100, 1)}% of matches")
print(f"Preferred toss decision: {toss_decision_counts.index[0]} ({toss_decision_counts.values[0]} times)")