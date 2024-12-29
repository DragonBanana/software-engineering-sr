class Subject:
    """Base class for a subject."""
    def __init__(self):
        self._observers = []  # List of observers

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)


class Pharmacy:
    """Observer: Pharmacy department."""
    def update(self, data):
        print(f"Pharmacy notified: New patient admitted - {data}")

class Billing:
    """Observer: Billing department."""
    def update(self, data):
        print(f"Billing notified: Generate bill for patient - {data}")

class Reception:
    """Observer: Reception department."""
    def update(self, data):
        print(f"Reception notified: Prepare room for patient - {data}")



class HospitalManagementSystem(Subject):
    """Concrete subject: Manages patient admissions."""
    def __init__(self):
        super().__init__()
        self.patients = []

    def admit_patient(self, patient_name):
        self.patients.append(patient_name)
        print(f"Patient {patient_name} admitted.")
        self.notify(patient_name)


# Create subject (observable)
hospital = HospitalManagementSystem()

# Create observers
pharmacy = Pharmacy()
billing = Billing()
reception = Reception()

# Attach observers to the subject
hospital.attach(pharmacy)
hospital.attach(billing)
hospital.attach(reception)

# Admit a new patient
hospital.admit_patient("John Doe")

# Output:
# Patient John Doe admitted.
# Pharmacy notified: New patient admitted - John Doe
# Billing notified: Generate bill for patient - John Doe
# Reception notified: Prepare room for patient - John Doe
