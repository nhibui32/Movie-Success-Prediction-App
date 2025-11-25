import csv
import pandas as pd 
import os 
from BuyTicket import BuyTicket
csv_file = "Data/Predicted.csv"

def search_movie(role, user):
    print('.\nEnter movie title:')
    title = input("Title: ")

    # Check if file exists
    if not os.path.exists(csv_file):
        print("CSV file not found!")
        return
    
    # Read CSV using pandas
    df = pd.read_csv(csv_file)


    movie = df[df['title'].str.lower() == title.lower()]

    if not movie.empty:
        print("\nMovie found:")
        print(movie.to_string(index=False))
    else:
        print("\nMovie not found.")

    movie_title = movie.iloc[0]['title']

    if role == 2 and not movie.empty:
        ticket = BuyTicket(user, movie_title)
        
        if ticket:
            save_ticket_to_csv(ticket)

def save_ticket_to_csv(data):
    csv_file = "Data/Ticket.csv"
    df = pd.DataFrame([data])

    # If file does NOT exist OR file is empty → write header
    write_header = not os.path.exists(csv_file) or os.stat(csv_file).st_size == 0

    df.to_csv(csv_file, mode='a', header=write_header, index=False)
