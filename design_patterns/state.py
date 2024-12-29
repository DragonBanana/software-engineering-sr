from abc import ABC, abstractmethod

# State interface
class RoomState(ABC):
    @abstractmethod
    def book(self, room):
        pass

    @abstractmethod
    def release(self, room):
        pass


# Concrete states
class AvailableState(RoomState):
    def book(self, room):
        print(f"Room {room.room_number} booked successfully.")
        room.set_state(room.occupied_state)

    def release(self, room):
        print(f"Room {room.room_number} is already available!")


class OccupiedState(RoomState):
    def book(self, room):
        print(f"Room {room.room_number} is already occupied!")

    def release(self, room):
        print(f"Room {room.room_number} is now available.")
        room.set_state(room.available_state)


class MaintenanceState(RoomState):
    def book(self, room):
        print(f"Room {room.room_number} is under maintenance, cannot be booked!")

    def release(self, room):
        print(f"Room {room.room_number} is under maintenance, cannot be released!")


# Context class
class HospitalRoom:
    def __init__(self, room_number):
        self.room_number = room_number
        self.available_state = AvailableState()
        self.occupied_state = OccupiedState()
        self.maintenance_state = MaintenanceState()
        self.current_state = self.available_state  # Initial state

    def set_state(self, state):
        self.current_state = state

    def book(self):
        self.current_state.book(self)

    def release(self):
        self.current_state.release(self)


# Client code
room = HospitalRoom(101)

room.book()     # Room 101 booked successfully.
room.book()     # Room 101 is already occupied!
room.release()  # Room 101 is now available.
room.release()  # Room 101 is already available!

# Switch to Maintenance
room.set_state(room.maintenance_state)
room.book()     # Room 101 is under maintenance, cannot be booked!
room.release()  # Room 101 is under maintenance, cannot be released!
