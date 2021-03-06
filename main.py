
class Person:

    # protected class variable should remain the same for all objects of this class
    #indicated by a single underscore, your IDE will warn you if you try to access it
    _species = "Homo Sapiens"

    #Indicating a private variable is done with two underscores, python will hide it and make it
    #more difficult to acces this variable, however contrary to other programming lanuages it still
    #can be accessed with workarounds
    __dont_touch_this = "this is is a secret"

    #defining a constructor with two mandatory parameters
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    #overriding the __str__ function for a custom string representation of the object
    def __str__(self):
        return "First Name: {0}, Last Name: {1}".format(self.first_name, self.last_name)

    #functions for printing the names so we do not need to use the print function in main code
    def print_first_name(self):
        print(self.first_name)

    def print_last_name(self):
        print(self.last_name)

    def print_private_stuff(self):
        print("This is the something private from: {0}, you shouldn't be here! {1}".format(self.first_name,self.__dont_touch_this))

#child class inheriting from Person class
class Student(Person):

    def __init__(self, first_name, last_name, student_id):
        super().__init__(first_name, last_name) #calling the constructor of the super class
        self.student_id = student_id

    def __str__(self):
        return "First Name: {0}, Last Name: {1}, Student ID: {2}".format(self.first_name, self.last_name, self.student_id)

    #overriding a function of the super class for a different behaviour
    def print_last_name(self):
        print("Last Name: {0}, ID: {1}".format(self.last_name, self.student_id))


#example of an informal interface
class InformalInterFaceName:

    def some_function(self):
        pass

    def another_function(self, number1, number2):
        pass


#instancing different student objects
student01 = Student("Alan", "Turing", 126540)
student02 = Student("Ada", "Lovelace", 101215)

#accessing a method/function from an object
student02.print_last_name()

#accessing a attribute/variable directly from an object and assigning it to a variable
id02 = student02.student_id

#optimal way to acces private variable:
student02.print_private_stuff()

#accsessing a protected variable directly is possible, but you will get a warning:
prot = student02._species

#accsesing a private variable directly will fail:
#student02.__dont_touch_this

#but you can access it with a workaround by calling its class name like this:
print(student02._Person__dont_touch_this)










