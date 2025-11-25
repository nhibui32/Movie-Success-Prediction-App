from Menu import (
    display_menu_as_staff,
    display_menu_as_user,
    display_menu_as_guest,
    validate_user
)
def User_Interface():
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

            if not current_user:  # Check if user exists
                print("\nInvalid username or password. Try again.")
                continue  # Go back to the main menu

            if current_user['role'] == 1:
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