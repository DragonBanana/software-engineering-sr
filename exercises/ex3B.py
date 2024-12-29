from abc import ABC, abstractmethod


# Abstract state class
class NotificationMode(ABC):
    @abstractmethod
    def notify(self, message):
        pass


# Concrete state classes
class SilentMode(NotificationMode):
    def notify(self, message):
        print(f"Silent Mode: {message} (notification on screen)")


class AirplaneMode(NotificationMode):
    def notify(self, message):
        print("Airplane Mode: No notification displayed.")


class OutdoorMode(NotificationMode):
    def notify(self, message):
        print(f"Outdoor Mode: {message} (with sound alert)")


class NoisyMode(NotificationMode):
    def notify(self, message):
        print(f"Noisy Mode: {message} (with sound alert and flashing light)")


# Context class
class Smartphone:
    def __init__(self):
        self.mode = None

    def set_mode(self, mode: NotificationMode):
        self.mode = mode

    def notify(self, message):
        if self.mode:
            self.mode.notify(message)
        else:
            print("No mode is set. Unable to send notification.")


# Example usage
if __name__ == "__main__":
    phone = Smartphone()

    # Set to silent mode
    phone.set_mode(SilentMode())
    phone.notify("You have a new message.")

    # Set to airplane mode
    phone.set_mode(AirplaneMode())
    phone.notify("You have a new message.")

    # Set to outdoor mode
    phone.set_mode(OutdoorMode())
    phone.notify("You have a new message.")

    # Set to noisy mode
    phone.set_mode(NoisyMode())
    phone.notify("You have a new message.")
