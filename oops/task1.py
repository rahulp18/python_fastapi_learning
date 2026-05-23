# class Car:
#     def __init__(self,brand,model,speed):
#         self.brand=brand
#         self.model=model
#         self.speed=speed
#     def __str__(self):
#         return f"Car {self.brand} model {self.model} {self.speed}"
#     def accelerate(self):
#         print(f"{self.brand} car is accelerating")

# audi=Car("Audi","A2",500)
# audi.accelerate()

# TASK2 Create Bank account

# class Bank:
#     def __init__(self,name,accountNumber,bankBalance):
#         self.name=name
#         self.__accountNumber=accountNumber
#         self.__bankBalance=bankBalance
    
#     def deposit(self,amount:int):
#         self.__bankBalance+=amount
#     def withdraw(self,amount:int):
#         self.__bankBalance-=amount
#     def balance(self):
#         return self.__bankBalance
    

# bank1=Bank("Rahul Pradhan",124421,100)
# bank1.deposit(12)

# print(bank1.balance())

# TASK 3
class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print("Animals can bark")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    
    def sound(self):
        print(f"{self.name} is a DOG , Vow vow")

dog=Dog("Dhoni")

dog.sound()

