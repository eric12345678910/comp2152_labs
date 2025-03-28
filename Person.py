class Person:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height
        self.public_prop = "I'm public"

        print("Constructing the Person object")


    def __del__(self):
        print("About to delete the person object")
        

    # Baisc Getters / Setters
    #def get_name(self):
    #    return self.__name
    
    #def set_name(self, name):
    #    self.__name = name

    # Magic Getters / Setters
    # NAME
    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, name):
        self.__name = name

    #AGE
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    # HEIGHT
    @property
    def height(self):
        return self.__height
    
    @age.setter
    def height(self, height):
        self.__height = height

    

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

