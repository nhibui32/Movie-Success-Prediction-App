import csv
from AddMovie import main as add_movie
from DisplayMovieList import display_movies
def validate_user(username, password):
    try:
        with open("Data/users.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username and row["password"] == password:
                    return int(row["role"])  # return 1 or 2
        return None
    except FileNotFoundError:
        print("Error: users.csv not found!")
        return None

def display_menu_as_staff():
    print("\nStaff Menu:")
    print("1. Add Movie")
    print("2. View Movie List")
    print("3. Logout")
    staff_choice = input("Enter your choice (1-3): ")
    if staff_choice == '1':
        add_movie()
    elif staff_choice == '2':
        display_movies()
    else:
        print("Logging out...")
        return
    
def display_menu_as_user():
    print("\nUser Menu:")
    print("1. View Movies List")
    print("2. Search Movies")
    print("3. Logout")
    user_choice = input("Enter your choice (1-3): ")
    if user_choice == '1':
        display_movies
    elif user_choice == '2':
        search_movies()
    else:
        print("Logging out...")
        return
    
def display_menu_as_guest():
    print("\nGuest Menu:")
    print("1. View Movies List")
    print("2. Exit")
    guest_choice = input("Enter your choice (1-2): ")
    if guest_choice == '1':
        display_movies()
    else:
        print("Exiting the application. Goodbye!")
        exit()