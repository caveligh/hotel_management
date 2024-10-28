# Module: rooms.py
class Room:
    def __init__(self, room_number: int, room_type: str, price: float):
        if room_type not in ["Single", "Double", "Suite"]:
            raise ValueError("El tipo de habitación debe ser 'Single', 'Double' o 'Suite'.")
        if price <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.available = True


class RoomManagement:
    def __init__(self):
        self.rooms: Dict[int, Room] = {}

    def add_room(self, room: Room) -> None:
        if room.room_number in self.rooms:
            raise ValueError(f"La habitación {room.room_number} ya existe.")
        self.rooms[room.room_number] = room
        print(f"Habitación {room.room_number} agregada.")

    def check_availability(self, room_number: int) -> bool:
        room = self.rooms.get(room_number)
        if room and room.available:
            print(f"Habitación {room_number} está disponible.")
            return True
        print(f"Habitación {room_number} no está disponible.")
        return False

    def set_availability(self, room_number: int, available: bool) -> None:
        room = self.rooms.get(room_number)
        if room:
            room.available = available

    def list_rooms(self) -> None:
        for room in self.rooms.values():
            status = "disponible" if room.available else "no disponible"
            print(f"Habitación {room.room_number}, Tipo: {room.room_type}, Precio: ${room.price}, Estado: {status}")
