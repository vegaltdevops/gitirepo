def greet(name):
    print(f"Hello {name}")
    
    
a = greet('Sagar')



class Greetings:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        
    def myInfo(self):
        return f"My info is \nNAME:{self.name + ' ' + self.surname} \n I am {self.age} years old."
    
    @classmethod
    def my_funct(cls, x):
          return x*x
      


a = Greetings('Sagr','Kthe', 29)

print(a.my_funct(5))
             