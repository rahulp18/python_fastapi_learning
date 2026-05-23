class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"I am {self.name}, ID={self.id}, age={self.age}"
    
class MarkEntry:
    def __init__(self, sub, mark):
        self.sub = sub
        self.mark = mark
    
class Student(Person):
    def __init__(self, roll_no, marks: list[MarkEntry], name, id, age):
        super().__init__(id, name, age)
        self.roll_no = roll_no
        self.marks = marks

    def add_marks(self, mark: MarkEntry):
        self.marks.append(mark)

    def calculate_average(self):
        if not self.marks: return 0
        total_marks = sum(m.mark for m in self.marks)
        return total_marks / len(self.marks)

    def introduce(self):
        return f"Hello I am a Student. " + super().introduce()

class Teacher(Person):
    def __init__(self, id, name, age, subject, salary):
        super().__init__(id, name, age)
        self.subject = subject
        self.__salary = salary

    def teach(self):
        return f"I teach {self.subject}"
    
    def get_salary(self):
        return self.__salary
    
class Classroom:
    def __init__(self, classroom_name, students: list[Student], teachers: list[Teacher]):
        self.classroom_name = classroom_name
        self.students = students
        self.teachers = teachers

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, student_id):
        for index, student in enumerate(self.students):
            if student.id == student_id:
                return self.students.pop(index)
        print("Invalid Student Id")

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def show_students(self):
        print(f"\n--- {self.classroom_name} Students ---")
        print(f"{'Name':<15} {'ID':<5} {'Age':<5} {'Roll':<8} {'Avg Marks'}")
        for s in self.students:
            print(f"{s.name:<15} {s.id:<5} {s.age:<5} {s.roll_no:<8} {s.calculate_average():.2f}")

# --- DATA PARSING ---

classroom_data = { 
    "students": [
      {"id": 1, "name": "Rahul Pradhan", "age": 24, "roll_no": 101, "marks": [{"phy": 85}, {"chem": 78}, {"math": 92}]},
      {"id": 2, "name": "Binita Das", "age": 22, "roll_no": 102, "marks": [{"phy": 70}, {"chem": 82}, {"math": 75}]}
    ],
    "teachers": [
      {"id": 10, "name": "Dr. Rakesh Iyer", "age": 45, "salary": 75000, "subject": "Physics"}
    ]
}

# Process Students
parsed_students = []
for s in classroom_data["students"]:
    student_marks = []
    for m_dict in s["marks"]:
        # Extract key and value from dict, e.g., {"phy": 85}
        for sub, score in m_dict.items():
            student_marks.append(MarkEntry(sub, score))
    
    new_student = Student(s["roll_no"], student_marks, s["name"], s["id"], s["age"])
    parsed_students.append(new_student)

# Process Teachers
parsed_teachers = []
for t in classroom_data["teachers"]:
    new_teacher = Teacher(t["id"], t["name"], t["age"], t["subject"], t["salary"])
    parsed_teachers.append(new_teacher)

# Create Classroom
class9 = Classroom("Class 9th", parsed_students, parsed_teachers)

# Display Result
class9.show_students()