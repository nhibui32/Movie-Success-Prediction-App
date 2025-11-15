import json
import pandas as pd
import os

# --- Load the scoring system from JSON ---
with open('Data/Score.json', 'r', encoding='utf-8') as f:
    scores = json.load(f)["Scores"]

# --- Function to calculate movie success ---
def calculate_movie_score(movie, scores):
    total_score = 0
    
    # Actors and Actresses
    total_score += scores["actors"].get(movie["actor"], 70)
    total_score += scores.get("actresses", {}).get(movie["actress"], 70)
    
    # Director
    total_score += scores["directors"].get(movie["director"], 70)
    
    # Genre
    total_score += scores["genres"].get(movie["genre"], 70)
    
    # Release Month
    total_score += scores["release_month"].get(movie["release_month"], 70)
    
    # Rating
    total_score += scores["rating"].get(movie["rating"], 70)
    
    # Budget
    total_score += scores["budget"].get(movie["budget"], 70)
    
    # Country
    total_score += scores["country"].get(movie["country"], 70)
    
    # Runtime
    total_score += scores["runtime"].get(movie["runtime"], 70)
    
    # Average score
    predicted_score = total_score / 9  # 9 factors
    return predicted_score

# --- Function to ask staff for movie info ---
def get_movie_input():
    print("Enter movie information:")
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
    movie["runtime"] = input("Runtime (Short (<90 min), Medium (90–120 min), Long (>120 min)): ")
    return movie

# --- CSV File ---
csv_file = "Data/Predicted.csv"

# --- Main Program ---
def main():
    # Ask for movie info
    movie = get_movie_input()
    
    # Calculate predicted score
    movie["predicted_score"] = round(calculate_movie_score(movie, scores), 2)
    
    # Convert to DataFrame
    df = pd.DataFrame([movie])
    
    # Check if CSV exists
    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_file, index=False)
    
    print("\nMovie added successfully!")
    print(f"Predicted Success Score: {movie['predicted_score']}/100")
    print(f"Data saved to {csv_file}")

# --- Run ---
if __name__ == "__main__":
    main()
