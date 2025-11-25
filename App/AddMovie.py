import os
import pandas as pd
from PredictedCalculation import calculate_movie_score

csv_file = "Data/Predicted.csv"

def get_movie_input():
    print("\nEnter movie information:")
    movie = {}
    movie["title"] = input("Title: ")
    movie["actor"] = input("Lead Actor: ")
    movie["actress"] = input("Lead Actress: ")
    movie["director"] = input("Director: ")
    movie["genre"] = input("Genre: ")
    movie["release_month"] = input("Release Month (e.g., July): ")
    movie["rating"] = input("MPAA Rating (G, PG, PG-13, R, NC-17): ")
    movie["budget"] = input("Budget (Low, Medium, High): ")
    movie["country"] = input("Country: ")
    return movie

def main():
    movie = get_movie_input()
    
    # Calculate prediction
    predicted = calculate_movie_score(movie)
    movie["predicted_score"] = round(predicted, 2)

    # Save to CSV
    df = pd.DataFrame([movie])

    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_file, index=False)

    print("\nMovie successfully added!")
    print(f"Predicted Success Score: {movie['predicted_score']}/100")
