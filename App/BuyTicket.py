import os 
import pandas as pd

csv_file = "Data/Ticket.csv.csv"

def BuyTicket(user, movie_title):
    answer = input("Do you want to buy the ticket for this movie? (Y/N)").lower()

    if answer == 'y':
        ticket = {}
        ticket['movie_title'] = movie_title
        ticket['user'] = user
        ticket['adult_quantity']= int(input("How many tickets would you like to buy for adult? "))
        while ticket['adult_quantity'] <=0:
            print("Please enter a positive number")
            ticket['adult_quantity']= int(input("How many tickets would you like to buy for adult? "))
        ticket['children_quantity'] = int(input("How many tickets would you like to buy for children? "))
        while ticket['children_quantity'] <=0:
            print("Please enter a positive number")
            ticket['children_quantity'] = int(input("How many tickets would you like to buy for children? "))
        ticket['total'] = 12.99 * ticket['adult_quantity'] + 9.99 * ticket['children_quantity']
        print("\n🎫 Successfully Booked! Enjoy your movie!")
        print(f"Your total is: ${ticket['total']:.2f}\n")
        return ticket
    else:
        print("Maybe next time.")

