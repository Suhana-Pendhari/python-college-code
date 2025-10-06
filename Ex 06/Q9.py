# Q9) Flight Booking System:
# Build a flight booking system with classes for flights, passengers, bookings, 
# seats, and itinerary management. Implement functionalities for flight scheduling, 
# reservations, and ticketing.

class Flight:
    def __init__(self, flight_number, origin, destination, seats):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.total_seats = seats
        self.available_seats = seats
        self.booked_passengers = []

    def printData(self):
        print(f"Flight {self.flight_number}: {self.origin} -> {self.destination} | Available Seats: {self.available_seats}")

    def book_seat(self, passenger):
        if self.available_seats > 0:
            self.available_seats -= 1
            self.booked_passengers.append(passenger)
            print(f"Seat booked for {passenger.name} on Flight {self.flight_number}")
            return True
        else:
            print(f"No seats available on Flight {self.flight_number}")
            return False


class Passenger:
    def __init__(self, name, passenger_id):
        self.name = name
        self.passenger_id = passenger_id

    def printData(self):
        print(f"Passenger {self.passenger_id}: {self.name}")


class Booking:
    booking_counter = 1

    def __init__(self, passenger, flight):
        self.booking_id = Booking.booking_counter
        Booking.booking_counter += 1
        self.passenger = passenger
        self.flight = flight

    def printData(self):
        print(f"Booking ID: {self.booking_id} | Passenger: {self.passenger.name} | Flight: {self.flight.flight_number}")


class FlightSystem:
    def __init__(self):
        self.flights = []
        self.passengers = []
        self.bookings = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def make_booking(self, passenger_id, flight_number):
        passenger = next((p for p in self.passengers if p.passenger_id == passenger_id), None)
        flight = next((f for f in self.flights if f.flight_number == flight_number), None)

        if passenger and flight:
            if flight.book_seat(passenger):
                booking = Booking(passenger, flight)
                self.bookings.append(booking)
        else:
            print("Passenger or Flight not found.")

    def show_flights(self):
        print("\nAvailable Flights:")
        for f in self.flights:
            f.printData()

    def show_bookings(self):
        print("\nAll Bookings:")
        if not self.bookings:
            print("No bookings yet.")
            return
        for b in self.bookings:
            b.printData()


system = FlightSystem()

#Add flights
f1 = Flight("AI101", "Mumbai", "Delhi", 3)
f2 = Flight("AI102", "Delhi", "Bangalore", 2)
system.add_flight(f1)
system.add_flight(f2)

#Add passengers
p1 = Passenger("Suhana", 201)
p2 = Passenger("Aman", 202)
p3 = Passenger("Zakriya", 203)
system.add_passenger(p1)
system.add_passenger(p2)
system.add_passenger(p3)

#Show available flights
system.show_flights()

#Make bookings
system.make_booking(201, "AI101")
system.make_booking(202, "AI101")
system.make_booking(203, "AI101")
system.make_booking(203, "AI102")

#Show bookings
system.show_bookings()

#Show flights after bookings
system.show_flights()
