class Passenger:
    def __init__(self, name, passport_id):
        self.name = name
        self.passport_id = passport_id

    def __str__(self):
        return f"{self.name} (Passport: {self.passport_id})"
