# This is a simple team building system
# Class 1: Declaring the employee class
class Employee:

    # Initializing the employee class and adding both first name, last name and also salary
    def __init__(self, fname, lname, sal):
        self.firstname = fname
        self.lastname = lname

        # You can see here that the employee salary is made privated
        self.__salary = sal

    def combinename(self):
        return self.firstname + ' ' + self.lastname

    def employesal(self):
        print(self.combinename(), " Salary is ", self.__salary)

# Class 2: Declaring the class developer
# Single inheritance is being implemented here. You can see employee class being inherited by developer class.

class Developer(Employee):
    # Initializing the developer class
    def __init__(self, firname, lastname, sal, language):
        Employee.__init__(self, firname, lastname, sal)
        self.programminglanguage=language
    # Access the developer's name
    def getdevop(self):
        return self.firstname + ' ' + self.lastname
    # Access programming language of the developer
    def getprogramminglanguage(self):
        return self.programminglanguage

#Class 3: Declaring the manager class
class Manager():

    #Initializing the manager class
    def __init__(self, managername, msurname, managersal, bu):
        self.fn = managername
        self.ln = msurname
        self.msal = managersal
        self.bu=bu

    # returning the manager name
    def mangrnme(self):
        return self.fn + ' ' + self.ln

    def getbu(self):
        return self.bu

# Class 4: Declaring the client class
class Clients():

    # Initializing the client class using self
    def __init__(self, cname):
        self.clientnm= cname

    def accessclientname(self):
        return self.clientnm

#  Class 5: Declaring team class and we are using the concept of multiple inheritance
class Team(Developer, Manager, Clients):

    def __init__(self, dfname, dlname, dsalary, dproglang, managername, msurname, managersal, mbu, cname):
            # Manager class being instantiated
            Manager.__init__(self, managername, msurname, managersal, mbu)
            # Client class being instantiated
            Clients.__init__(self, cname)
            # Developer class being instantiated
            Developer.__init__(self,dfname,dlname,dsalary,dproglang) #instance of developer class


print(" THIS IS SOFTWARE TEAM ESTABLISHMENT SYSTEM")
print("Enter the software developer details")
devopfirst = input("Enter first name here:")
devoplast = input(" Enter last name here:")
devoppay = input("Salary of the developer")
devoplanguage = input("Programming language that is developer intrested in:")

print("\n"," Enter the manager's details:")
managerf = input("Enter First name here:")
managerl = input("Enter Last name here:")
managerpay = input("Manager Earnings:")
managerbusiness = input("Area of business:")
client = input(" Enter the name of the client:")
teambuild = Team(devopfirst, devoplast, devoppay, devoplanguage, managerf, managerl, managerpay, managerbusiness, client)#instance of team class

print(" Now let us look at the whole team that is built as part of the project:")
print(" :::Client details:::")
print("Name of the client", teambuild.accessclientname(), "\n")

print(":::Team Manager details:::")
print("Manager name:", teambuild.mangrnme())
print(" Area of business: ", teambuild.getbu(), "\n")


print(":::Developer details:::")
print(" Name of developer: ",teambuild.getdevop())
print(" Area of programming: ",teambuild.getprogramminglanguage())
