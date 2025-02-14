from django.shortcuts import render
import pandas as pd

# Load the dataset once
df = pd.read_csv("all_regions_combined_tech_branches_final.csv")

def homepage(request):
    return render(request, 'homepage.html')

def predict_college(rank, region):
    # Convert input to integer
    rank = int(rank)

    # Filter colleges based on cutoff rank and location
    filtered_df = df[(df["Cutoff"] >= rank) & (df["Location"].str.contains(region, case=False))]

    # Convert DataFrame to list of dictionaries
    return filtered_df.to_dict(orient="records")

def result(request):
    if request.method == 'POST':
        rank = request.POST.get('rank')
        region = request.POST.get('region')

        try:
            results = predict_college(rank, region)
            return render(request, 'results.html', {'values': results})
        except Exception as e:
            return render(request, 'results.html', {'error': str(e)})

    return render(request, 'results.html')