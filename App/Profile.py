import csv

# Function to edit user profile
def edit_profile(user, csv_path="Data/Users.csv"):
    print("\n=== Edit Profile ===")
    print("Press Enter to keep the current value.\n")

    # Get new values, defaulting to current ones if Enter is pressed
    new_first_name = input(f"First Name ({user['first_name']}): ") or user['first_name']
    new_last_name = input(f"Last Name ({user['last_name']}): ") or user['last_name']
    new_dob = input(f"DOB ({user['DOB']}): ") or user['DOB']
    new_email = input(f"Email ({user['email']}): ") or user['email']
    new_phone = input(f"Phone Number ({user['phone_number']}): ") or user['phone_number']

    # Update user dictionary
    user['first_name'] = new_first_name
    user['last_name'] = new_last_name
    user['DOB'] = new_dob
    user['email'] = new_email
    user['phone_number'] = new_phone

    # Read all users, update the current user's info, and write back to CSV
    rows = []
    # Load existing users and update the relevant one, then save back
    with open(csv_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        #read every row in the file check if the username matches the current user
        for row in reader:
            if row["username"] == user["username"]:
                row.update(user)
            rows.append(row)
    # Write updated rows back to CSV
    with open(csv_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("\nProfile updated successfully!\n")

# Function to display user profile
def Profile(user):
    while True:
        #Check the role of the user to display appropriate profile header
        if user['role'] == 1:
            print("\n==== Staff Profile ====")
        else:
            print("\n==== User Profile ====")
        print(f"Username: {user['username']}")
        print(f"Name: {user['first_name']} {user['last_name']}")
        print(f"DOB: {user['DOB']}")
        print(f"Email: {user['email']}")
        print(f"Phone: {user['phone_number']}")
        print("======================")
        
        print("\n1. Edit Profile")
        print("2. Back")
        choice = input("Choose an option: ")

        #ask user if they want to edit profile or go back
        if choice == "1":
            edit_profile(user)
        elif choice == "2":
            return
        else:
            print("Invalid choice. Try again.")
