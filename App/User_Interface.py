from Menu import (
    display_menu_as_staff,
    display_menu_as_user,
    display_menu_as_guest,
    validate_user
)

def User_Interface():
    #when the application starts, it will display the welcome message and prompt the user to login or continue as guest.
    print("Welcome to the Movie Success Prediction App!")

    #Main loop to handle user choices, while allowing multiple attempts for login.
    while True:
        print("\nPlease select an option to continue:")
        print("1. Login")
        print("2. Continue as Guest")
        print("3. Exit")

        # Get user choice
        choice = input("Enter your choice (1-3): ")

        # Handle user choice
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")

            current_user = validate_user(username, password)

            # Allow multiple attempts for login
            while current_user is None:
                print("Invalid username or password. Please try again.")
                username = input("Enter username: ")
                password = input("Enter password: ")
                # Re-validate user credentials
                current_user = validate_user(username, password)
            #Check user role and display appropriate menu
            if current_user['role'] == 1:
                print("\nLogin successful! Welcome Staff.")
                #If user is staff, display staff menu, else display user menu. the parameter current_user is passed to the menu functions to provide user-specific options.
                display_menu_as_staff(current_user)

            elif current_user['role'] == 2:
                print("\nLogin successful! Welcome User.")
                display_menu_as_user(current_user)

        # Continue as Guest
        elif choice == '2':
            print("\nContinuing as Guest...")
            # Display guest menu
            display_menu_as_guest()

        # Exit the application
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            exit()
        # Handle invalid input
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
