from Person import Person

class Student(Person):
    def __init__(self, name, age, height, major):
        super().__init__(self, name, age, height, major)
        self.major = major

    def __del__(self):
        print("Deleting the student object")
        

s1 = Student("Maria, 22, 6, Computer Science")
print(s1.name)

