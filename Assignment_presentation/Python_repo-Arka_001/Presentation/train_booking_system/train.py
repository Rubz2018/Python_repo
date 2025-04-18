# train.py

class Train:
    def __init__(self, train_no, name, seats):
        self.train_no = train_no
        self.name = name
        self.seats = seats
        self.booked_seats = []

    def display_info(self):
        print(f"\nTrain No: {self.train_no}")
        print(f"Train Name: {self.name}")
        print(f"Available Seats: {self.seats - len(self.booked_seats)}")

    def book_seat(self, passenger_name):
        if len(self.booked_seats) < self.seats:
            self.booked_seats.append(passenger_name)
            print(f"✅ Ticket booked successfully for {passenger_name}")
        else:
            print("❌ No seats available.")

    def cancel_seat(self, passenger_name):
        if passenger_name in self.booked_seats:
            self.booked_seats.remove(passenger_name)
            print(f"✅ Ticket cancelled for {passenger_name}")
        else:
            print("❌ No booking found for this name.")
