
class MyClass:
    def __init__(self, name):
        # * ตัวแปร protected
        self._name = name  

    def _get_name(self):
        return self._name

    def _set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print("ชื่อควรเป็นสตริง")

    def display_name(self):
        print(f"ชื่อ: {self._name}")

# * สร้างอ็อบเจ็กต์ของคลาส MyClass
obj = MyClass("John")

# * เรียกใช้เมท็อด protected
obj._set_name("Alice")  # * แก้ไขชื่อโดยใช้ _set_name
obj.display_name()  # * แสดงชื่อโดยใช้ display_name
