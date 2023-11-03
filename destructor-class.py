
class MyClass:
    def __init__(self,value):
        self.value = value

    def show(self):
        print(f"{self.value}")
    
    def __del__(self):
        print("delete object")

obj = MyClass("Hello")

obj.show()