from arthmetic import *

'''
Classes can represent real-world objects or abstract ideas. After defining a class, you use it by making an instance, or
object,of the class. You can make as many instances as you want from one class.
As an example, you might use a class to represent a website user. The class would have attributes associated with the 
user’s username, password, registration date, and more. Methods would define the actions the user could take, such as 
registering, authenticating, logging in, and logging out. You could then make one instance for each user who registers 
on the site.
Many external libraries are written as classes, so learn-ing to work with classes makes it easier to work with many 
existing projects.
'''

ar = Arithmetic()
print(ar.add())
print(ar.divide())
print(ar.remainder())
ar.print_self()

# TODO: create several more instance of the Arithmetic class and add different values


# redefined Arithmetic and added more objects so I would have more to work with than the provided 2 it started with...
class Arithmetic:

    def __init__(self, n1=1, n2=2, n3=3, n4=4, n5=5, n6=6, n7=7, n8=8, n9=9, n10=10):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.n6 = n6
        self.n7 = n7
        self.n8 = n8
        self.n9 = n9
        self.n10 = n10
# subtracts one from value input

    def oopslostone(self, x):
        return x - self.n1

# makes use of self.n2 which = 2 to square whatever the value entered into the function is
    def squared(self, x):
        return x**self.n2

# similar to last but cubed values
    def cubed(self, x):
        return x**self.n3

# chaos addition subtraction multiplication division and remainder calc calling on multiple class objects
    def chaos(self):
        return self.n1*self.n5-self.n10+self.n7/self.n2 % self.n4

# subtracts n2*2 from n4 the joke is it = 0... 0 ideas left
    def ideasleft(self):
        return self.n4-self.n2*2


ar = Arithmetic()
print(ar.oopslostone(10))
print(ar.squared(5))
print(ar.cubed(9))
print(ar.chaos())
print(str(ar.ideasleft()) + " ideas left")
