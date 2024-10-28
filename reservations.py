# Module Reservations.py
from datetime import datetime
from collections import defaultdict

class Reservation:
    def __init__(self, reservation_id: int, customer_name: str, room_number: int, check_in: datetime, check_out: datetime):
        if check_out <= check_in:
            raise ValueError("La fecha de check-out debe ser posterior a la fecha de check-in.")
        self.reservation_id = reservation_id
        self.customer_name = customer_name
        self.room_number = room_number
        self.check_in = check_in
        self.check_out = check_out

class ReservationSystem:
    def __init__(self):
        self.reservations: Dict[int, List[Reservation]] = defaultdict(list)

    def add_reservation(self, reservation: Reservation) -> None:
        # Check if room is available for the given period
        for existing_reservation in self.reservations[reservation.room_number]:
            if (reservation.check_in < existing_reservation.check_out and reservation.check_out > existing_reservation.check_in):
                raise ValueError(f"La habitación {reservation.room_number} no está disponible en las fechas seleccionadas.")
        
        self.reservations[reservation.room_number].append(reservation)
        print(f"Reserva creada para {reservation.customer_name} en la habitación {reservation.room_number}")

    def cancel_reservation(self, reservation_id: int) -> None:
        for room, reservations in self.reservations.items():
            for r in reservations:
                if r.reservation_id == reservation_id:
                    reservations.remove(r)
                    print(f"Reserva {reservation_id} cancelada")
                    return
        raise ValueError("Reserva no encontrada")

    def list_reservations(self) -> None:
        for room, reservations in self.reservations.items():
            for r in reservations:
                print(f"Reserva ID: {r.reservation_id}, Cliente: {r.customer_name}, Habitación: {r.room_number}, Check-in: {r.check_in}, Check-out: {r.check_out}")
                