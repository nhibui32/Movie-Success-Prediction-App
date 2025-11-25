import csv

def edit_profile(user, csv_path="Data/Users.csv"):
    print("\n=== Edit Profile ===")
    print("Press Enter to keep the current value.\n")

    new_first_name = input(f"First Name ({user['first_name']}): ") or user['first_name']
    new_last_name = input(f"Last Name ({user['last_name']}): ") or user['last_name']
    new_dob = input(f"DOB ({user['DOB']}): ") or user['DOB']
    new_email = input(f"Email ({user['email']}): ") or user['email']
    new_phone = input(f"Phone Number ({user['phone_number']}): ") or user['phone_number']

    user['first_name'] = new_first_name
    user['last_name'] = new_last_name
    user['DOB'] = new_dob
    user['email'] = new_email
    user['phone_number'] = new_phone

    rows = []
    with open(csv_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        for row in reader:
            if row["username"] == user["username"]:
                row.update(user)
            rows.append(row)

    with open(csv_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("\nProfile updated successfully!\n")

def Profile(user):
    while True:
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

        if choice == "1":
            edit_profile(user)
        elif choice == "2":
            return
        else:
            print("Invalid choice. Try again.")
