class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}  # A dictionary to store grades by subject
    
    # Method to add a grade for a specific subject
    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:
            self.grades[subject] = grade
            print(f"Added grade {grade} for {subject}.")
        else:
            print("Grade must be between 0 and 100.")
    
    # Method to calculate the average grade
    def get_average_grade(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        return 0
    
    # Method to get the grade for a specific subject
    def get_subject_grade(self, subject):
        return self.grades.get(subject, None)
    
    # Method to get the full report card
    def get_report_card(self):
        return self.grades
    
    # Class method to create a student from a dictionary
    @classmethod
    def create_from_dict(cls, data):
        student = cls(data['name'], data['student_id'])
        student.grades = data.get('grades', {})
        return student

# Example usage
# Create a student instance
student1 = Student("Alice", "S001")
student1.add_grade("Math", 85)
student1.add_grade("Science", 90)
student1.add_grade("History", 78)

# Display average grade and report card
print(f"{student1.name}'s Average Grade:", student1.get_average_grade())
print(f"{student1.name}'s Report Card:", student1.get_report_card())

# Create another student from a dictionary
data = {
    "name": "Bob",
    "student_id": "S002",
    "grades": {"Math": 88, "Science": 76}
}
student2 = Student.create_from_dict(data)
print(f"{student2.name}'s Report Card:", student2.get_report_card())