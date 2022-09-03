class Wizard():
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    @property
    def __str__(self,name):
        return f" The wizard is : {name}"
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    @property
    def __str__(self,name, house):
        super().__str__(name)
        return f" The student is : {self.name} living in {self.house}"
    
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    @property
    def __str__(self,name, subject):
        super().__str__(name)
        return f" The professor is : {self.name} teaching {self.subject}"
    

    
    
if __name__ == "__main__":
    student = Student("Luis","Envigado")
    print(student.name, student.house)
    professor = Professor("Luis","DB2")
    print(professor.name, professor.subject)
    wizard = Wizard("Peter")
    print(wizard)