
# * สร้างคลาสหลักชื่อ "Animal"
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# * สร้างคลาสย่อยชื่อ "Dog" ซึ่งสืบทอดคุณสมบัติจากคลาส "Animal"
class Dog(Animal):
    def speak(self):
        return f"{self.name} ส่งเสียง: บ๊วบ๊ว"

# * สร้างคลาสย่อยชื่อ "Cat" ซึ่งสืบทอดคุณสมบัติจากคลาส "Animal"
class Cat(Animal):
    def speak(self):
        return f"{self.name} ส่งเสียง: แมววว"

# * สร้างอ็อบเจ็กต์ของคลาส "Dog" และ "Cat" และเรียกใช้งานเมท็อด "speak"
dog = Dog("Fido")
cat = Cat("Whiskers")

print(dog.speak())  # * แสดงผลลัพธ์ "Fido ส่งเสียง: บ๊วบ๊ว"
print(cat.speak())  # * แสดงผลลัพธ์ "Whiskers ส่งเสียง: แมววว"
