class SingletonMeta(type):
    """Metaclass for implementing Singleton pattern."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print("Initializing Hospital Management System...")
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class HospitalManagementSystem(metaclass=SingletonMeta):
    """Singleton class to manage hospital resources."""
    def __init__(self):
        self.records = []  # Shared resource for patient records

    def add_record(self, record):
        self.records.append(record)

    def get_records(self):
        return self.records


# Singleton usage
hospital1 = HospitalManagementSystem()
hospital2 = HospitalManagementSystem()

hospital1.add_record("Patient A")
hospital2.add_record("Patient B")

print(hospital1.get_records())  # Output: ['Patient A', 'Patient B']
print(hospital2.get_records())  # Output: ['Patient A', 'Patient B']

print(hospital1 is hospital2)  # Output: True
