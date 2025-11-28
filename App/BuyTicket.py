import os 
import pandas as pd

# Define the path to the CSV file
csv_file = "Data/Ticket.csv.csv"

# Function to handle ticket purchasing
def BuyTicket(user, movie_title):
    # Prompt user to buy ticket, .lower() to handle case insensitivity.
    answer = input("Do you want to buy the ticket for this movie? (Y/N)").lower()

    # If user wants to buy ticket, gather ticket details
    if answer == 'y':
        #create the ticket dictionary to hold ticket details
        ticket = {}
        ticket['movie_title'] = movie_title
        ticket['user'] = user
        ticket['adult_quantity']= int(input("How many tickets would you like to buy for adult? "))
        # make sure that adult quantity is a positive number
        while ticket['adult_quantity'] < 0:
            print("Please enter a positive number")
            ticket['adult_quantity']= int(input("How many tickets would you like to buy for adult? "))
        ticket['children_quantity'] = int(input("How many tickets would you like to buy for children? "))
        # make sure that children quantity is a positive number
        while ticket['children_quantity'] <= 0:
            print("Please enter a positive number")
            ticket['children_quantity'] = int(input("How many tickets would you like to buy for children? "))
        #adult ticket price is $12.99, children ticket price is $9.99
        ticket['total'] = 12.99 * ticket['adult_quantity'] + 9.99 * ticket['children_quantity']
        print("\n🎫 Successfully Booked! Enjoy your movie!")
        #display total price with 2 decimal places
        print(f"Your total is: ${ticket['total']:.2f}\n")
        #   RETURN ticket dictionary
        return ticket
    else:
        print("Maybe next time.")

