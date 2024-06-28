class Animal:
    def __init__(self, name):
        print("constructor invoked")
        self.__name = name

    def eat(self):
        print(self.__name)
        print("I can eat")

    def sleep(self):
        print("I can sleep")

    def get_name(self):
        return self.__name

class Dog(Animal):
    def bark(self):
        print("Dog can bark")

dog1 = Dog('Pug')
print(dog1.get_name())
dog1.eat() 
dog1.sleep()
dog1.bark()


class Bankaccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
        print(f"deposit sucessful. new balance : ${self._balance}")

    def check_balance(self):
        print(f"current balance : {self._balance}")

    def withdraw (self, amount):
        self._balance -= amount
        print(f"withdraw sucessful. new balance : ${self._balance}")

account = Bankaccount('1234', 1000)
account.deposit(100)
account.withdraw(1500)
account.check_balance()

#class employee:
 #   def __init__(self,name,emp_id,salary):
  #      self._name = name
   #     self._emp_id = emp_id
    #    self._salary = salary

    #def calculate_bonus(self):
     #   return self.salary * 0.1
    
    #def display_info(self):
     #   print(f"name : $ {self._name}")
      #  print(f"employee : ${self._emp_id}")
       # print(f"salary : $ {self._salary}")

#employee = employee('gu',1, 10000)
#employee.display_info()
#bonus = employee.calculate_bonus()


class Father:
    def __init__(self, child):
        self.child = child
        
    def talk(self):
        print("Father is talking")

class Ram(Father):
    def talk(self):
        print("Ram is talking")

class Shyam(Father):
    def talk(self):
        print("Shyam is talking")

father = Father("Child")
ram = Ram("Ram")
shyam = Shyam("Shyam")

father.talk()  
ram.talk()     
shyam.talk()  



class emplyee:
    def __init__(self, name ,emp_id):
        self.name = name
        self._emp_id = emp_id

    def display_info(self):
        print(f'name : {self.name}')
        print(f'employee Id : {self.emp_id}')

class manager(emplyee):
    def __init__(self,name,emp_id,department):
        super().__init__(name,emp_id)
        self.department = department
    
    def display_info(self):
        super().display_info()
        print(f'Department : {self,department}')

class developer(emplyee):
    def __init__(self,name,emp_id,programming_language):
        super().__init__(name,emp_id)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f'programming language : {self.programming_language}')

manager = manager('gu',1,'engeenerar')
manager.display_info()

developer = developer('hello',1,'gukodalla')
developer.display_info()