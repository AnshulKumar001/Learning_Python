class Student:
    def __init__(self, name, total_marks, obtained_marks):
        self.name = name
        self.total_marks = total_marks
        self.obtained_marks = obtained_marks

    @property
    def percentage(self):
        return (self.obtained_marks / self.total_marks) * 100

# Example usage
student1 = Student("John", 500, 450)
print(f"Student Name: {student1.name}")
print(f"Percentage: {student1.percentage}%")
