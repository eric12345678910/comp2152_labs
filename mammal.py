from heart import Heart
# import Heart from heart module

class Mammal:
    def __init__(self, age):
        self.age = age
        self.heart = Heart() # Create a heart object and assign to heart property in the mammal

    def speak(self):
        print("Grr...")

    def __str__(self):
        return f"Mammal is {self.age} years old."
    