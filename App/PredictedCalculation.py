import json 

with open('Data/Score.json', 'r', encoding='utf-8') as f:
    scores = json.load(f)["Scores"] 

def calculate_movie_score(movie):
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
    
    # Average score
    predicted_score = total_score / 8  # 8 factors
    return predicted_score