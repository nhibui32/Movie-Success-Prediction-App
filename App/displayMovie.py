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

    print("\n--- Summary ---")
    print(f"Total movies: {len(df)}")
    print(f"Average Predicted Score: {df['predicted_score'].mean():.2f}/100")

if __name__ == "__main__":
    display_movies()
