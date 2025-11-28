import csv
import pandas as pd 
import os 
from BuyTicket import BuyTicket
from DisplayMovieList import display_movies

# Define the path to the CSV file
csv_file = "Data/Predicted.csv"

# Function to search for a movie by title       
def search_movie(role, user):
    print('.\nEnter movie title:')  
    #get title input from user
    title = input("Title: ")

    # Check if file exists
    if not os.path.exists(csv_file):
        print("CSV file not found!")
        return
    
    # Read CSV using pandas
    df = pd.read_csv(csv_file)

    #user may enter title in different cases(capslk), so use .str.lower() to make it case insensitive
    movie = df[df['title'].str.lower() == title.lower()]

    #if movie is empty, prompt user to try again until a valid movie is found
    while movie.empty:
        print("Movie not found. Please try again.")
        print("This is a list of available movies:\n")
        display_movies()
        title = input("Title: ")
        movie = df[df['title'].str.lower() == title.lower()]
    #if movie is found, display movie details
    if not movie.empty:
        print("\nMovie found:")
        print(movie.to_string(index=False))
    else:
        print("\nMovie not found.")
    
    #get the movie title from the dataframe
    movie_title = movie.iloc[0]['title']
    
    # If the user is a regular user(role 2), prompt them to buy ticket
    if role == 2 and not movie.empty:
        #call BuyTicket function from BuyTicket.py
        ticket = BuyTicket(user, movie_title)
        #If user bought ticket, save ticket to Ticket.csv
        if ticket:
            save_ticket_to_csv(ticket)

# Function to save ticket data to Ticket.csv
def save_ticket_to_csv(data):
    csv_file = "Data/Ticket.csv"
    df = pd.DataFrame([data])

    # If file does NOT exist OR file is empty → write header
    write_header = not os.path.exists(csv_file) or os.stat(csv_file).st_size == 0
    # Append to CSV
    df.to_csv(csv_file, mode='a', header=write_header, index=False)
