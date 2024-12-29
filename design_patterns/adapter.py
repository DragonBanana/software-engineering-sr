# Existing classes in the hospital system
class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def get_details(self):
        return f"Doctor {self.name} - Specialization: {self.specialization}"


# Third-party library class
class ExternalNurse:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def details(self):
        return f"Nurse {self.name} - Department: {self.department}"


# Hospital management system expecting `get_details`
class HospitalManagementSystem:
    def __init__(self):
        self.staff_list = []

    def add_staff(self, staff):
        self.staff_list.append(staff)

    def show_all_staff(self):
        for staff in self.staff_list:
            print(staff.get_details())

# Adapter class to translate the `details` method to `get_details`
class ExternalNurseAdapter:
    def __init__(self, external_nurse):
        self.external_nurse = external_nurse

    def get_details(self):
        return self.external_nurse.details()


# Hospital management system remains unchanged
hospital = HospitalManagementSystem()

# Adding Doctor works as before
doctor = Doctor("Alice", "Cardiology")
hospital.add_staff(doctor)

# Use the adapter to integrate ExternalNurse
nurse = ExternalNurse("Bob", "Emergency")
nurse_adapter = ExternalNurseAdapter(nurse)
hospital.add_staff(nurse_adapter)

hospital.show_all_staff()

# Output:
# Doctor Alice - Specialization: Cardiology
# Nurse Bob - Department: Emergency


# Client code
hospital = HospitalManagementSystem()

# Adding Doctor works fine
doctor = Doctor("Alice", "Cardiology")
hospital.add_staff(doctor)

# Adding ExternalNurse will break the code
nurse = ExternalNurse("Bob", "Emergency")
# hospital.add_staff(nurse)  # Uncommenting this will raise an AttributeError

hospital.show_all_staff()

# Output (if nurse is added):
# AttributeError: 'ExternalNurse' object has no attribute 'get_details'
