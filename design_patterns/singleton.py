class HospitalManagementSystem:
    """Singleton class to manage hospital resources."""
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print("Initializing Hospital Management System...")
            cls.__instance = super(HospitalManagementSystem, cls).__new__(cls)
            cls.__instance.records = []  # Initialize shared resources
        return cls.__instance

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
