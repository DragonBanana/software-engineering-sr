class Doctor:
    def __init__(self, name, staff_id, specialization):
        self.name = name
        self.staff_id = staff_id
        self.specialization = specialization

    def get_details(self):
        return f"Doctor {self.name} (ID: {self.staff_id}) - Specialization: {self.specialization}"


class Nurse:
    def __init__(self, name, staff_id, department):
        self.name = name
        self.staff_id = staff_id
        self.department = department

    def get_details(self):
        return f"Nurse {self.name} (ID: {self.staff_id}) - Department: {self.department}"


class HospitalStaffFactory:
    @staticmethod
    def create_staff(staff_type, **kwargs):
        if staff_type == "doctor":
            return Doctor(kwargs["name"], kwargs["staff_id"], kwargs["specialization"])
        elif staff_type == "nurse":
            return Nurse(kwargs["name"], kwargs["staff_id"], kwargs["department"])
        else:
            raise ValueError(f"Unknown staff type: {staff_type}")


# Client Code
staff = HospitalStaffFactory.create_staff(
    "doctor", name="Alice", staff_id=101, specialization="Cardiology"
)
print(staff.get_details())
