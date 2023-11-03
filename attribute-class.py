
class MyClass:
    def __init__(self,name):
        # * แอตทริบิวต์ name
        self.name = name
    
    def __del__(self):
        pass

obj = MyClass("Alice")
print(obj.name)