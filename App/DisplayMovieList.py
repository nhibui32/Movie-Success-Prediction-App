#display list of predicted movies for all user roles
import pandas as pd
import os

csv_file = "Data/Predicted.csv"

def display_movies():
    # Check if file exists
    if not os.path.exists(csv_file):
        print("No movie data found yet. Please add movies first.")
        return
    
    # Read CSV using pandas
    df = pd.read_csv(csv_file)
    
    if df.empty:
        print("No movie data found.")
        return

    print("\n--- Movie List ---\n")
    print(df.to_string(index=False))

