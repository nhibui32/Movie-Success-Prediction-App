from LogIn import Login

# Movie Success Prediction App Workflow
# Step 1: Display login options: log in, continue as guest or exit =
def main():
    Login()
#   Step 2: Show Staff Menu:
#       1. Add Movie
#       2. View Predicted Movies
#       3. Logout

#   Step 3: If Add Movie selected:
#       - Prompt staff to enter movie information
#       - Calculate predicted success score
#       - Save movie details + predicted score into CSV file

#   Step 4: If View Predicted Movies selected:
#       - Read movie list from CSV file
#       - Display all movies with predicted scores

#   Step 5: If Logout selected:
#       - Return to Login Screen

# If User:
#   Display User Menu:
#       1. View Predicted Movies
#       2. Search Movies
#       3. Logout

#   If View Predicted Movies:
#       - Read and display movies from CSV file

#   If Search Movies:
#       - Ask for search criteria (title, genre, actor, etc.)
#       - Display matching movies from CSV file

#   After viewing a movie:
#       - Ask whether to book ticket or return to User Menu

#   If Logout:
#       - Return to Login Screen


# If Guest:
#   Display Guest Menu:
#       1. View Predicted Movies
#       2. Exit

#   - Guests can only view movies, no search or booking


if __name__ == "__main__":
    main()
