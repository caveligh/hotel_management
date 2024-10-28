from collections import defaultdict
from datetime import datetime
import asyncio
import random
from typing import Dict, List, Optional, Callable
from customers import Customer, CustomerManagement
from rooms import Room, RoomManagement
from reservations import Reservation, ReservationSystem
from payments import process_payment

    
# Integrating the System
async def main():
    reservation_system = ReservationSystem()
    customer_mgmt = CustomerManagement()
    room_mgmt = RoomManagement()

    # Adding rooms
    room_mgmt.add_room(Room(101, "Single", 100))
    room_mgmt.add_room(Room(102, "Double", 150))
    room_mgmt.add_room(Room(103, "Suite", 300))

    # Adding customers
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer_mgmt.add_customer(customer1)

    customer2 = Customer(2, "Bob", "bob@example.com")
    customer_mgmt.add_customer(customer2)

    # Listing customers
    customer_mgmt.list_customers()

    # Removing a customer
    try:
        customer_mgmt.remove_customer(1)
    except ValueError as e:
        print(f"Error: {e}")

    # Listing rooms
    room_mgmt.list_rooms()

    # Making reservations and processing payments concurrently
    try:
        if room_mgmt.check_availability(101):
            reservation = Reservation(1, "Bob", 101, datetime.now(), datetime.now())
            reservation_system.add_reservation(reservation)
            room_mgmt.set_availability(101, False)
            await process_payment("Bob", 100)

        if room_mgmt.check_availability(102):
            reservation = Reservation(2, "Bob", 102, datetime.now(), datetime.now())
            reservation_system.add_reservation(reservation)
            room_mgmt.set_availability(102, False)
            await process_payment("Bob", 150)

    except ValueError as e:
        print(f"Error: {e}")

    # Listing reservations
    reservation_system.list_reservations()

if __name__ == "__main__":
    asyncio.run(main())

if __name__ == "__main__":
    asyncio.run(main())
