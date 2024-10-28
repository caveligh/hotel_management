# test_hotel_management
import asyncio
from hotel_reservation import Customer, CustomerManagement, Room, RoomManagement, Reservation, ReservationSystem, process_payment
from datetime import datetime
from payments import process_payment
from collections import defaultdict

async def test_hotel_management():
    # Instanciar los sistemas
    customer_mgmt = CustomerManagement()
    room_mgmt = RoomManagement()
    reservation_system = ReservationSystem()

    # 1. Agregar clientes
    print("\n--- Agregar Clientes ---")
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer2 = Customer(2, "Bob", "bob@example.com")
    customer3 = Customer(3, "Charlie", "charlie@example.com")

    customer_mgmt.add_customer(customer1)
    customer_mgmt.add_customer(customer2)
    customer_mgmt.add_customer(customer3)

    # 2. Listar clientes
    print("\n--- Listar Clientes ---")
    customer_mgmt.list_customers()

    # 3. Eliminar un cliente
    print("\n--- Eliminar Cliente (ID: 2) ---")
    try:
        customer_mgmt.remove_customer(2)
    except ValueError as e:
        print(f"Error: {e}")

    # 4. Listar clientes nuevamente
    print("\n--- Listar Clientes (Después de Eliminar) ---")
    customer_mgmt.list_customers()

    # 5. Agregar habitaciones
    print("\n--- Agregar Habitaciones ---")
    room1 = Room(101, "Single", 100)
    room2 = Room(102, "Double", 150)
    room3 = Room(103, "Suite", 300)

    room_mgmt.add_room(room1)
    room_mgmt.add_room(room2)
    room_mgmt.add_room(room3)

    # 6. Listar habitaciones
    print("\n--- Listar Habitaciones ---")
    room_mgmt.list_rooms()

    # 7. Hacer una reserva
    # 7. Hacer una reserva
    print("\n--- Hacer una Reserva ---")
    try:
        if room_mgmt.check_availability(101):
            reservation1 = Reservation(1, "Alice", 101, datetime.now(), datetime.now().replace(day=datetime.now().day + 1))
            reservation_system.add_reservation(reservation1)
            room_mgmt.set_availability(101, False)
            await process_payment("Alice", 100)
    except ValueError as e:
        print(f"Error: {e}")

    # 8. Hacer otra reserva
    print("\n--- Hacer Otra Reserva ---")
    try:
        if room_mgmt.check_availability(102):
            reservation2 = Reservation(2, "Charlie", 102, datetime.now(), datetime.now().replace(day=datetime.now().day + 1))
            reservation_system.add_reservation(reservation2)
            room_mgmt.set_availability(102, False)
            await process_payment("Charlie", 150)
    except ValueError as e:
        print(f"Error: {e}")

    # 8. Hacer otra reserva
    print("\n--- Hacer Otra Reserva ---")
    try:
        if room_mgmt.check_availability(102):
            reservation2 = Reservation(2, "Charlie", 102, datetime.now(), datetime.now())
            reservation_system.add_reservation(reservation2)
            room_mgmt.set_availability(102, False)
            await process_payment("Charlie", 150)
    except ValueError as e:
        print(f"Error: {e}")

    # 9. Listar reservas
    print("\n--- Listar Reservas ---")
    reservation_system.list_reservations()

    # 10. Cancelar una reserva
    print("\n--- Cancelar Reserva (ID: 1) ---")
    try:
        reservation_system.cancel_reservation(1)
        room_mgmt.set_availability(101, True)
    except ValueError as e:
        print(f"Error: {e}")

    # 11. Listar reservas nuevamente
    print("\n--- Listar Reservas (Después de Cancelar) ---")
    reservation_system.list_reservations()

    # 12. Listar habitaciones nuevamente
    print("\n--- Listar Habitaciones (Después de Cancelar Reserva) ---")
    room_mgmt.list_rooms()

if __name__ == "__main__":
    asyncio.run(test_hotel_management())
