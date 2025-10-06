# Q7) Hotel Booking System:
# Design a system to manage hotel rooms, reservations, guests, and bookings. 
# Implement classes for rooms, guests, reservations, bookings, and 
# availability management.

class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = True

    def printData(self):
        status = "Available" if self.is_available else "Booked"
        print(f"Room {self.room_number}: {self.room_type}, Price: ${self.price}, Status: {status}")


class Guest:
    def __init__(self, name, guest_id):
        self.name = name
        self.guest_id = guest_id

    def printData(self):
        print(f"Guest {self.guest_id}: {self.name}")


class Reservation:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def printData(self):
        print(f"Reservation: Room {self.room.room_number} for {self.guest.name} from {self.check_in_date} to {self.check_out_date}")


class Hotel:
    def __init__(self):
        self.rooms = []
        self.guests = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def add_guest(self, guest):
        self.guests.append(guest)

    def check_availability(self):
        print("\nAvailable Rooms:")
        available = False
        for room in self.rooms:
            if room.is_available:
                room.printData()
                available = True
        if not available:
            print("No rooms available.")

    def make_reservation(self, guest, room_number, check_in_date, check_out_date):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_available:
                    room.is_available = False
                    reservation = Reservation(guest, room, check_in_date, check_out_date)
                    self.reservations.append(reservation)
                    print(f"Reservation successful for {guest.name} in Room {room_number}.")
                    return
                else:
                    print(f"Room {room_number} is already booked.")
                    return
        print(f"Room {room_number} not found.")

    def show_reservations(self):
        print("\nAll Reservations:")
        if not self.reservations:
            print("No reservations yet.")
            return
        for res in self.reservations:
            res.printData()


hotel = Hotel()

#Add rooms
hotel.add_room(Room(101, "Single", 100))
hotel.add_room(Room(102, "Double", 150))
hotel.add_room(Room(103, "Single", 100))

#Add guests
g1 = Guest("Suhana", 201)
g2 = Guest("Aman", 202)
hotel.add_guest(g1)
hotel.add_guest(g2)

#Check available rooms
hotel.check_availability()

#Make reservations
hotel.make_reservation(g1, 101, "2025-09-25", "2025-09-27")
hotel.make_reservation(g2, 102, "2025-09-26", "2025-09-28")
hotel.make_reservation(g2, 101, "2025-09-28", "2025-09-30")

#Show reservations
hotel.show_reservations()

#Check available rooms again
hotel.check_availability()
