
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

user=User("Alice", 30)
user.display_info()

#inheritance
class Admin(User):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role
    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")


admin=Admin("Bob", 40, "Administrator")
admin.display_info()    

#inheritance with multiple classes
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id


class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def display_info(self):
                    print(f"Name: {self.name}, Employee ID: {self.employee_id}, Department: {self.department}")       

manager=Manager("Charlie", 12345, "Sales")
manager.display_info()

#abstraction
    

