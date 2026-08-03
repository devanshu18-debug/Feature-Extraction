import numpy as np
import pandas as pd

df = pd.read_csv('anime.csv')

def extract_episode(txt):
    check = False
    data = ""

    for i in txt:
        if i == "(":
            check = True

        if check:
            data += i

        if i == ")":
            break

    return data

df['Episodes'] = df['Title'].apply(extract_episode)

# Clean the text
df['Episodes'] = df['Episodes'].str.replace("(", "", regex=False)
df['Episodes'] = df['Episodes'].str.replace(")", "", regex=False)
df['Episodes'] = df['Episodes'].str.replace(" eps", "", regex=False)

# Convert to integer
df['Episodes'] = df['Episodes'].astype(int)
def extract_time(txt):
    check = False
    data = ""
    count = 0

    for i in txt:
        if i == ")":
            check = True
            continue

        if check and count < 19:
            data += i
            count += 1

    return data.strip()
df['Time'] = df['Title'].apply(extract_time)

print(df[['Title', 'Time']])

print(df.head())
a = df[df['Score'] == df['Score'].max()]['Title']
print(a)
b = df['Score'].head()
print(b)