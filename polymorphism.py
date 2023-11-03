
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# * สร้างอ็อบเจ็กต์ของคลาสแต่ละคลาส
dog = Dog()
cat = Cat()
duck = Duck()

# * เรียกใช้เมท็อด speak บนอ็อบเจ็กต์แต่ละตัว
print(dog.speak())  # * ผลลัพธ์: Woof!
print(cat.speak())  # * ผลลัพธ์: Meow!
print(duck.speak())  # * ผลลัพธ์: Quack!
