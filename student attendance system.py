from datetime import datetime

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.attendance = []  # List of (date, status)

    def mark_attendance(self, status):
        date = datetime.now().strftime("%Y-%m-%d")
        self.attendance.append((date, status))

    def get_attendance(self):
        return self.attendance


class AttendanceSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} added.")
        else:
            print("Student already exists.")

    def mark_attendance(self, student_id, status="Present"):
        if student_id in self.students:
            self.students[student_id].mark_attendance(status)
            print(f"Attendance marked for {self.students[student_id].name}.")
        else:
            print("Student not found.")

    def view_attendance(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"\nAttendance record for {student.name}:")
            for date, status in student.get_attendance():
                print(f"{date} - {status}")
        else:
            print("Student not found.")

    def list_students(self):
        print("\nAll Students:")
        for sid, student in self.students.items():
            print(f"{sid}: {student.name}")


# Example usage:
if __name__ == "__main__":
    system = AttendanceSystem()

    # Add some students
    system.add_student(1, "Taukir")
    system.add_student(2, "Arka")
    system.add_student(3, "Tuhin")
    system.add_student(4, "kuddus")
    system.add_student(5,"Digonto")
    system.add_student(6, "Tazmirul")

    # Mark attendance
    system.mark_attendance(1, "Present")
    system.mark_attendance(2, "Absent")
    system.mark_attendance(3, "Present")
    system.mark_attendance(4, "Absent")
    system.mark_attendance(5, "Present")
    system.mark_attendance(6, "Absent")

    # View attendance
    system.view_attendance(1)
    system.view_attendance(2)
    system.view_attendance(3)
    system.view_attendance(4)
    system.view_attendance(5)
    system.view_attendance(6)

    # List all students
    system.list_students()
