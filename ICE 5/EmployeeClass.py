class Employee():
    empCount=0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount = Employee.empCount + 1

    def countEmp(self):
        return Employee.empCount

    def getEmpName(self):
        return self.name

    def getEmpSalary(self):
        return self.salary

class Manager(Employee):
    def __init__(self,name,salary):
        super(Manager,self).__init__(name,salary)


emp = Employee('Ram',6000)
print("Name:"+emp.getEmpName())
print("Salary:%d"%(emp.getEmpSalary()))

emp = Employee('Pooja',8100)
print("Name:"+emp.getEmpName())
print("Salary:%d"%(emp.getEmpSalary()))

manager = Manager('Karan',3600)
print("Name:"+manager.getEmpName())
print("Salary:%d"%(manager.getEmpSalary()))

print("Number of employees:%d"%(emp.countEmp()))
