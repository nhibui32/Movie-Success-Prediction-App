# # Movie Success Prediction App Workflow

# # Step 1: Display login options:
# #   - Login as Staff
# #   - Login as User
# #   - Continue as Guest
# print("Welcome to the Movie Success Prediction App!")
# print("Please select an option to continue:")
# print("1. Login")
# print("2. Continue as Guest")
# print("3. Exit")
# choice = input("Enter your choice (1-3): ")
# if choice == '1':
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     # Here, you would normally validate the username and password
#     # For simplicity, let's assume any input is valid and determine role
# elif choice == '2':
    
# else:
#     print("Exiting the application. Goodbye!")
#     exit()

# # If Staff:
# #   Step 2: Show Staff Menu:
# #       1. Add Movie
# #       2. View Predicted Movies
# #       3. Logout

# #   Step 3: If Add Movie selected:
# #       - Prompt staff to enter movie information
# #       - Calculate predicted success score
# #       - Save movie details + predicted score into CSV file

# #   Step 4: If View Predicted Movies selected:
# #       - Read movie list from CSV file
# #       - Display all movies with predicted scores

# #   Step 5: If Logout selected:
# #       - Return to Login Screen


# # If User:
# #   Display User Menu:
# #       1. View Predicted Movies
# #       2. Search Movies
# #       3. Logout

# #   If View Predicted Movies:
# #       - Read and display movies from CSV file

# #   If Search Movies:
# #       - Ask for search criteria (title, genre, actor, etc.)
# #       - Display matching movies from CSV file

# #   After viewing a movie:
# #       - Ask whether to book ticket or return to User Menu

# #   If Logout:
# #       - Return to Login Screen


# # If Guest:
# #   Display Guest Menu:
# #       1. View Predicted Movies
# #       2. Exit

# #   - Guests can only view movies, no search or booking

from Menu import (
    display_menu_as_staff,
    display_menu_as_user,
    display_menu_as_guest,
    validate_user
)

def main():
    print("Welcome to the Movie Success Prediction App!")

    while True:
        print("\nPlease select an option to continue:")
        print("1. Login")
        print("2. Continue as Guest")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")

            role = validate_user(username, password)

            if role == 1:
                print("\nLogin successful! Welcome Staff.")
                display_menu_as_staff()

            elif role == 2:
                print("\nLogin successful! Welcome User.")
                display_menu_as_user()

            else:
                print("\nInvalid username or password. Try again.")

        elif choice == '2':
            print("\nContinuing as Guest...")
            display_menu_as_guest()

        elif choice == '3':
            print("Exiting the application. Goodbye!")
            exit()

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
