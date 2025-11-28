#display list of predicted movies for all user roles
import pandas as pd
import os

# Define the path to the CSV file
csv_file = "Data/Predicted.csv"

# Function to display movies
def display_movies():
    # Check if file exists
    if not os.path.exists(csv_file):
        print("No movie data found yet. Please add movies first.")
        return
    
    # Read CSV using pandas
    df = pd.read_csv(csv_file)

    # Check if DataFrame is empty
    if df.empty:
        print("No movie data found.")
        return
    
    # Display the movies in a formatted way
    print("\n--- Movie List ---\n")
    print(df.to_string(index=False))

