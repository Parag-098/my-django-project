from django.shortcuts import render
import pandas as pd

# Load and clean the dataset
df = pd.read_csv("all_regions_combined_tech_branches_final_cleaned.csv")

# Standardize column names
df.columns = df.columns.str.strip().str.replace(" ", "_")  # Remove spaces and replace with "_"

def homepage(request):
    return render(request, 'homepage.html')

def predict_college(rank, region, branch):
    try:
        rank = int(rank)
        region = region.strip()
        branch = branch.strip()

        # Standardizing column names
        filtered_df = df[
            (df["Cutoff"] >= rank) & 
            (df["Location"].str.contains(region, case=False, na=False)) & 
            (df["Branch"].str.contains(branch, case=False, na=False))
        ]

        # Sorting and removing duplicate colleges
        sorted_df = filtered_df.sort_values(by="Cutoff", ascending=True).drop_duplicates(subset=["College_Name"], keep="last")

        return sorted_df.to_dict(orient="records")
    
    except Exception as e:
        return {"error": str(e)}

def result(request):
    if request.method == 'POST':
        rank = request.POST.get('rank')
        region = request.POST.get('region')
        branch = request.POST.get('branch')

        results = predict_college(rank, region, branch)

        return render(request, 'results.html', {'values': results})

    return render(request, 'results.html')

def about(request):
    return render(request, 'about.html')
