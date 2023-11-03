
class Student:
    def __init__(self, name, student_id):
        self.name = name  # * public member
        self._student_id = student_id  # * protected member
        self.__grades = []  # * private member

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f"เพิ่มเกรด {grade} ให้กับ {self.name}")
        else:
            print("เกรดไม่ถูกต้อง")

    def display_grades(self):
        print(f"เกรดของ {self.name}: {self.__grades}")

# * สร้างอ็อบเจ็กต์ของคลาส Student
student1 = Student("Alice", "S12345")

# * เพิ่มเกรดให้กับนักเรียน
student1.add_grade(90)
student1.add_grade(85)

# * แสดงเกรด
student1.display_grades()

# * แสดงข้อมูลสมาชิก public, protected, และ private
print(student1.name)  # * public
print(student1._student_id)  # * protected
# * จะเกิดข้อผิดพลาดเนื่องจากเราไม่สามารถเข้าถึง __grades จากภายนอกคลาสได้
# print(student1.__grades)  
