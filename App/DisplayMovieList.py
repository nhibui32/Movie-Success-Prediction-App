#display list of predicted movies for all user roles
import pandas as pd
import os

csv_file = "Data/Predicted.csv"

def display_movies():
    print("Looking for file at:", os.path.abspath(csv_file))  # Debug line

    if not os.path.exists(csv_file):
        print("No movie data found yet. Please add movies first.")
        return
    
    df = pd.read_csv(csv_file)
    
    if df.empty:
        print("No movie data found.")
        return

    print("\n--- Movie List ---\n")
    print(df.to_string(index=False))

