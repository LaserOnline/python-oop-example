
class MyClass:
    # * Method
    # * เมื่อทำการ ประกาศ Method จะต้อง ระบุบ self 
    # * Python เข้าใจว่าเมทอดนี้เป็นเมทอดของคลาสและสามารถเรียกใช้ได้
    def show(self):
        print("HelloWorld")


obj = MyClass()

obj.show()