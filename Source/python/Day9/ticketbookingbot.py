import requests
import threading

# Shared variable for available tickets
available_tickets = 2
lock = threading.Lock()  # Lock for thread safety

def book_ticket(movie_name, theatre_name, show_time, no_of_tickets):
    global available_tickets

    # Acquire the lock before modifying the shared variable
    with lock:
        if no_of_tickets > 0 and available_tickets >= no_of_tickets:
            print(f"Ticket booked for {movie_name} at {theatre_name} for {show_time} show")
            available_tickets -= no_of_tickets
            print(f"Remaining tickets: {available_tickets}")
        else:
            print(f"Failed to book ticket for {movie_name}. Not enough tickets available.")

class TicketBookingBot:
    @staticmethod
    def book_ticket_thread(movie_name, theatre_name, show_time, no_of_tickets):
        thread = threading.Thread(target=book_ticket, args=(movie_name, theatre_name, show_time, no_of_tickets))
        thread.start()
        thread.join()
def main():
    TicketBookingBot.book_ticket_thread("Avengers", "PVR", "10:30 AM", 1)
    TicketBookingBot.book_ticket_thread("Joker", "Inox", "1:30 PM", 1)
    TicketBookingBot.book_ticket_thread("Spiderman", "Cinepolis", "4:30 PM", 1)
main()