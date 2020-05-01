class A:

    def welcome(self):
        print("This is a class function")

    def hello(self):
        print("Hello World")

    def sum(self, a, b):
        c = a + b
        print("Sum is " + str(c))




# To call any member of the class, create an object of that class
obj = A()

# Call functions of a class by using the object
obj.welcome()
