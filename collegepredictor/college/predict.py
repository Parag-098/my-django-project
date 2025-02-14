import pandas as pd

# Load the CSV file
df = pd.read_csv('all_regions_combined_tech_branches_final.csv')

def predict(rank, region):
    filtered_df = df[(df['Cutoff'] >= rank) & (df['Location'].str.lower() == region.lower())]
    sorted_df = filtered_df.sort_values(by='Cutoff', ascending=True).drop_duplicates(subset=["College Name"], keep='last')
    return sorted_df
