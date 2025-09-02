class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def find_flight(self, flight_number):
        for f in self.flights:
            if f.flight_number == flight_number:
                return f
        return None

    def __str__(self):
        return f"{self.name} Airline | Flights: {len(self.flights)}"
