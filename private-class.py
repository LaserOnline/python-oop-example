
class MyClass:
    def __init__(self):
        pass

    def show(self, message):
        self.__message = message
        print(self.__message)

obj = MyClass()
obj.show("Hello Python")

