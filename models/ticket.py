class Ticket:
    def __init__(self, ticket_id, passenger, flight, seat, status):
        self.ticket_id = ticket_id
        self.passenger = passenger
        self.flight = flight
        self.seat = seat
        self.status = status

    def __str__(self):
        if self.status == "Confirmed":
            return (f"🎟️ Boarding Pass\n"
                    f"Ticket ID: {self.ticket_id}\n"
                    f"Passenger: {self.passenger.name}\n"
                    f"Flight: {self.flight.flight_number} → {self.flight.destination}\n"
                    f"Seat: {self.seat}\n"
                    f"Status: {self.status}")
        else:
            return (f"🎟️ Ticket\n"
                    f"Ticket ID: {self.ticket_id}\n"
                    f"Passenger: {self.passenger.name}\n"
                    f"Flight: {self.flight.flight_number} → {self.flight.destination}\n"
                    f"Status: WAITLISTED")
