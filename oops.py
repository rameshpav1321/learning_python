class Employee:
    raise_amout=1.04

    def __init__(self,first,last,pay) -> None:
        self.first=first
        self.last=last
        self.pay=pay
        # self.email=self.first+'.'+self.last+'@company.com'
#property decorator allows us to use getter,setter,delter methods in
# a class as just attributes instead of methods 
    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"
    
    def full_name(self):
        return self.first+' '+self.last
#syntax for setter & deleter decorator 
    @full_name.setter
    def full_name(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last

    @full_name.deleter
    def full_name(self):
        self.first=None
        self.last=None
        print("name deleted")

    
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)

# class methods are also used as alternate constructors
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amout=amount
# static methods unlike instance & class methods dont get any default argument
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
# magic/dunder methods
    def __repr__(self) -> str:
        return f"{self.first} {self.last},{self.pay}"
# str method uses repr method as fallback
    def __str__(self) -> str:
        return f"{self.full_name()}-{self.email}"

# class Developer(Employee):
#     def __init__(self, first, last, pay,prog_lang) -> None:
#         super().__init__(first, last, pay)
#         self.prog_lang=prog_lang

# class Manager(Employee):
    # def __init__(self, first, last, pay,employees=None) -> None:
    #     super().__init__(first, last, pay)
    #     self.employees=[] if employees is None else employees
    
    # def add_emp(self,emp):
    #     if emp not in self.employees:
    #         self.employees.append(emp)
    
    # def remove_emp(self,emp):
    #     if emp in self.employees:
    #         self.employees.remove(emp)

    # def print_emps(self):
    #     for emp in self.employees:
    #         print('-->',emp.full_name())

# employee class
emp1=Employee('Ramesh','Pothamsetty',100000)
print(emp1.full_name())
print(emp1.email)
# developer class
# dev1=Developer('Pavan','Pothamsetty','100000','Python')
# print(dev1.email,dev1.prog_lang)
# manager class
# man1=Manager('Sue','Smith',150000,[dev1])
# print(man1.email)
# dev2=Developer('Andy','Zing','10000','JavaScript')
# man1.add_emp(dev2)
# print(man1.print_emps())

# help method allows us to see the details of a class
# print(help(Developer))