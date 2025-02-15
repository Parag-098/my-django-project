import pandas as pd

# Load the dataset
df = pd.read_csv('all_regions_combined_tech_branches_final_cleaned.csv')

def predict(rank, region, branch):
    # Convert rank to integer
    rank = int(rank)

    # Filter dataset based on rank, region, and branch
    filtered_df = df[
        (df["Cutoff"] >= rank) & 
        (df["Location"].str.contains(region, case=False, na=False)) & 
        (df["Branch"].str.contains(branch, case=False, na=False))
    ]

    # Sort by cutoff in ascending order and remove duplicate colleges
    sorted_df = filtered_df.sort_values(by='Cutoff', ascending=True).drop_duplicates(subset=["College Name"], keep='last')

    return sorted_df.to_dict(orient="records")
