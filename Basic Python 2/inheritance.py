class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"Name: {self.name} is walking"


class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def work(self):
        return f"{self.name} is working at {self.company}."


class Manager(Employee):
    def __init__(self, name, company, department):
        super().__init__(name, company)
        self.department = department

    def manage(self):
        return f"{self.name} is managing the {self.department}"


class Developer(Employee):
    def __init__(self, name, company, product):
        super().__init__(name, company)
        self.product = product

    def coding(self):
        return f"{self.name} is developing the {self.product}."


class Buyer(Person):
    def __init__(self, name):
        super().__init__(name)

    def buy(self, product):
        return f"{self.name} is buying {product}"


# Example usage:
person = Person("John Doe")
print(person.walk())

employee = Employee("Jane Doe", "KodingAkaedmi")
print(employee.work())

manager = Manager("Alice Smith", "KodingAkademi", "Sales")
print(manager.manage())
print(manager.work())

developer = Developer("Bob Brown", "KodingAkademi", "Website")
print(developer.work())
print(developer.coding())

buyer = Buyer("Jim Beam")
print(buyer.walk())
print(buyer.buy("Python Beginner 2"))
