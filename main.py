
class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

    def __str__(self):
        return f"{self.name} (Passport: {self.passport_number})"


class Ticket:
    def __init__(self, passenger, seat_number, flight):
        self.passenger = passenger
        self.seat_number = seat_number
        self.flight = flight

    def __str__(self):
        return f"Ticket: {self.passenger.name}, Seat: {self.seat_number}, Flight: {self.flight.flight_number}"


class Flight:
    def __init__(self, flight_number, capacity):
        self.flight_number = flight_number
        self.capacity = capacity
        self.seats = [None] * capacity  # None means empty seat
        self.waitlist = []

    def book_ticket(self, passenger):
        for i in range(self.capacity):
            if self.seats[i] is None:
                ticket = Ticket(passenger, i + 1, self)
                self.seats[i] = ticket
                print(f"✅ Ticket booked for {passenger.name} | Seat {i + 1}")
                return ticket

        # If no seats available → waitlist
        self.waitlist.append(passenger)
        print(f"⚠️ No seats available. {passenger.name} added to waitlist.")
        return None

    def cancel_ticket(self, seat_number):
        if 1 <= seat_number <= self.capacity and self.seats[seat_number - 1] is not None:
            canceled_ticket = self.seats[seat_number - 1]
            print(f"❌ Ticket for {canceled_ticket.passenger.name} (Seat {seat_number}) canceled.")
            self.seats[seat_number - 1] = None

            # If waitlist exists, assign seat to next passenger
            if self.waitlist:
                next_passenger = self.waitlist.pop(0)
                self.book_ticket(next_passenger)
        else:
            print("⚠️ Invalid seat number or seat already empty.")

    def show_details(self):
        print(f"\n--- Flight {self.flight_number} Details ---")
        for i, seat in enumerate(self.seats, start=1):
            if seat:
                print(f"Seat {i}: {seat.passenger.name}")
            else:
                print(f"Seat {i}: [Empty]")
        if self.waitlist:
            print("\nWaitlist:", ", ".join(p.name for p in self.waitlist))
        else:
            print("\nWaitlist: None")

    def print_boarding_pass(self, seat_number):
        if 1 <= seat_number <= self.capacity and self.seats[seat_number - 1]:
            ticket = self.seats[seat_number - 1]
            print("\n🎟️ --- Boarding Pass ---")
            print(f"Passenger: {ticket.passenger.name}")
            print(f"Passport: {ticket.passenger.passport_number}")
            print(f"Flight: {self.flight_number}")
            print(f"Seat: {ticket.seat_number}")
            print("-----------------------\n")
        else:
            print("⚠️ Invalid seat number or no ticket assigned.")


class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = {}

    def add_flight(self, flight_number, capacity):
        if flight_number not in self.flights:
            self.flights[flight_number] = Flight(flight_number, capacity)
            print(f"✈️ Flight {flight_number} added with {capacity} seats.")
        else:
            print("⚠️ Flight already exists.")

    def get_flight(self, flight_number):
        return self.flights.get(flight_number, None)


# =========================
# Main Program
# =========================
def main():
    airline = Airline("Ontario Tech Airlines")

    while True:
        print("\n--- Airline Reservation Menu ---")
        print("1. Add Flight")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Show Flight Details")
        print("5. Print Boarding Pass")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            flight_number = input("Enter flight number: ")
            capacity = int(input("Enter flight capacity: "))
            airline.add_flight(flight_number, capacity)

        elif choice == "2":
            flight_number = input("Enter flight number: ")
            flight = airline.get_flight(flight_number)
            if flight:
                name = input("Enter passenger name: ")
                passport = input("Enter passport number: ")
                passenger = Passenger(name, passport)
                flight.book_ticket(passenger)
            else:
                print("⚠️ Flight not found.")

        elif choice == "3":
            flight_number = input("Enter flight number: ")
            flight = airline.get_flight(flight_number)
            if flight:
                seat_number = int(input("Enter seat number to cancel: "))
                flight.cancel_ticket(seat_number)
            else:
                print("⚠️ Flight not found.")

        elif choice == "4":
            flight_number = input("Enter flight number: ")
            flight = airline.get_flight(flight_number)
            if flight:
                flight.show_details()
            else:
                print("⚠️ Flight not found.")

        elif choice == "5":
            flight_number = input("Enter flight number: ")
            flight = airline.get_flight(flight_number)
            if flight:
                seat_number = int(input("Enter seat number: "))
                flight.print_boarding_pass(seat_number)
            else:
                print("⚠️ Flight not found.")

        elif choice == "6":
            print("👋 Exiting Airline Reservation System. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
