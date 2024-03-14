# Create a class called Employee with private attributes __name, __id, and __salary. Implement methods to set and get these attributes.
#  Then, create another class Manager which inherits from Employee. Override the salary method to calculate the manager's salary with an additional bonus.
#   Test these classes by creating instances of both Employee and Manager and demonstrating encapsulation and polymorphism principles.

class employee:
    def __init__(self,name,id,salary):
        self.__name = name
        self.__id = id
        self.__salary=salary
    def set_attribute(self,name,id,salary):
        self.__name = name
        self.__id = id
        self.__salary =salary

    def get_attribute(self):
        print(f'name = {self.__name} , id = {self.__id}, salary = {self.__salary}')

    def get_salary(self):
        return self.__salary

    def __str__(self):
        return f'name = {self.__name} , id = {self.__id}, salary = {self.__salary}'
    
class manager(employee):
    def __init__(self,name,id,salary,bonus):
        employee.__init__(self,name,id,salary)
        self.__bonus=bonus
    
    def calculate_salary(self):
        base=self.get_salary()
        print(f'salary = {base+self.__bonus}')
        

print("before set the attribute ")
a=employee('m',1,20000)
print(a)
print("after set the attribute through set attribute method ")
a.set_attribute('l',2,40000)
print(a)
print("before set the attribute of manager class ")
m=manager('k',44,20000,400)
print(f"salary of manager ")
m.calculate_salary()
print(m)
print("after set the attribute through set attribute method ")

m.set_attribute('m',1,20050)
print(m)
