import os
import pandas as pd
from PredictedCalculation import calculate_movie_score

# Define the path to the CSV file
csv_file = "Data/Predicted.csv"

# Function to get movie input from user
def get_movie_input():
    print("\nEnter movie information:")
    #Create the movie dictionary to hold movie details
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
    #return the movie dictionary
    return movie

# Main function to add movie and calculate prediction
def main():
    # Get movie details from user
    movie = get_movie_input()
    
    # Call calculate_movie_score to get predicted success score, then add it to the movie dictionary, rounding to 2 decimal places.
    predicted = calculate_movie_score(movie)
    movie["predicted_score"] = round(predicted, 2)

    # Save to CSV
    df = pd.DataFrame([movie])

    # Append to CSV if it exists, else create new file
    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_file, index=False)
    # Confirmation message
    print("\nMovie successfully added!")
    print(f"Predicted Success Score: {movie['predicted_score']}/100")
