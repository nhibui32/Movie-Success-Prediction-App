import csv
from AddMovie import main as add_movie
from DisplayMovieList import display_movies
from SearchMovie import search_movie
from Profile import Profile

#The function to validate user credentials against the users.csv file.
def validate_user(username, password):
    # Read users.csv and validate credentials
    try:
        with open("Data/users.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username and row["password"] == password:
                    # Convert role to int for consistency
                    row["role"] = int(row["role"])
                    return row  # Return the full user info as a dictionary
        return None  # User not found or wrong password
    except FileNotFoundError:
        print("Error: users.csv not found!")
        return None

# Display menu for staff users
def display_menu_as_staff(current_user):
    print("\nStaff Menu:")
    print("1. Profile")
    print("2. Add Movie")
    print("3. View Movie List")
    print("4. Logout")
    staff_choice = input("Enter your choice (1-4): ")
    # Handle staff choices, calling appropriate functions
    if staff_choice == '1':
        #if staff selects profile, show profile details, then return to staff menu
        Profile(current_user)
        display_menu_as_staff(current_user)
    if staff_choice == '2':
        #if staff selects add movie, call add_movie function, then return to staff menu
        add_movie()
        display_menu_as_staff(current_user)
    elif staff_choice == '3':
        #if staff selects view movie list, display movies, then return to staff menu
        display_movies()
        display_menu_as_staff(current_user)
    else:
        print("Logging out...")
        return

# Display menu for regular users
def display_menu_as_user(current_user):
    print("\nUser Menu:")
    print("1. Profile")
    print("2. View Movies List")
    print("3. Search Movies")
    print("4. Logout")
    user_choice = input("Enter your choice (1-4): ")
    if user_choice == '1':
        #if user selects profile, show profile details, then return to user menu
        Profile(current_user)
        display_menu_as_user(current_user)
    elif user_choice == '2':
        #if user selects view movies list, display movies, then return to user menu
        display_movies()
        display_menu_as_user(current_user)
    elif user_choice == '3':
        #if user selects search movies, call search_movie function, then return to user menu
        search_movie(current_user['role'], current_user['first_name'])
        display_menu_as_user(current_user)
    else:
        #if user selects logout, print logging out message and return to main menu
        print("Logging out...")
        return

# Display menu for guest users
def display_menu_as_guest():
    print("\nGuest Menu:")
    print("1. View Movies List")
    print("2. Search Movies")
    print("3. Exit")
    guest_choice = input("Enter your choice (1-3): ")
    if guest_choice == '1':
        #if guest selects view movies list, then display movies, then return to guest menu
        display_movies()
        display_menu_as_guest()
    elif guest_choice == '2':
        #if guest selects search movies, call search_movie function with None parameters, then return to guest menu
        search_movie(None, None) 
        display_menu_as_guest()
    else:
        #if guest selects exit, print exiting message and exit application
        print("Exiting the application. Goodbye!")
        exit()
