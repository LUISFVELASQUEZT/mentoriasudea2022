# Python program to demonstrate
# use of class method and static method.

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age=age
                    
    def __str__(self):
        return f"{self.name.capitalize()} is {self.age} years old!"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError(" Missing name")
        self._name = name
    
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        if not age > 0:
            raise ValueError(" Missing age")
        if not age < 99:
            raise ValueError("Too high")
        self._age = age
    
        
    @classmethod
    def get(cls):
        name = input("Name: ")
        age = int(input ("Age: "))
        return cls(name, age)
    
    @classmethod
    def get_fecha(cls):
        name = input("Name: ")
        year = int(input ("Year: "))
        return cls(name, year)  

	
    @classmethod
    
    def porFecha(cls, name, year):
        return cls(name, date.today().year - year)

	# a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
        
    

def main():
    person1 = Person.get()
    person2 = Person.porFecha('Luis', 1951)

    print(person1)
    print(person2)

    # print the result
    print(Person.isAdult(17))
    
    
if __name__ == "__main__":
    main()
