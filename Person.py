class Person:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

        self.public_prop = "I'm public"

        print("Constructing the Person object")


    def __del__(self):
        print("About to delete the person object")
        

    # Getter
    def get_name(self):
        return self.__name
    
    # Setter
    def set_name(self, name):
        self.__name = name

    # Magic Getter
    def get_name(self):
        return self.__name
    
    # Magic Setter
    def set_name(self, name):
        self.__name = name

    

a = 5
p1  = Person("Mark", 20, 6)
#print(p1.__height)
#print(p1.public_prop)
print(p1.public_prop)

print(p1.get_name()) 

p1.set_name("Jane")
print(p1.get_name()) 

p1.name = "jake"
print(p1.name)

print("script is ending")

