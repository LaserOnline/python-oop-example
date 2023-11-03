
class MyClass:
    def __init__(self,name):
        self._name = name
    # * decorator 
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if value.isalpha():
            self._name = value
        else:
            print("Name must contain only letters")

obj = MyClass("Alice")
# * เข้าถึงโพรพเพอร์ตี้ name โดยใช้ @property
print(obj.name)  
# * กำหนดค่าโพรพเพอร์ตี้ name โดยใช้ @name.setter
obj.name = "123"  
