class Person:
    @classmethod
    def class_method(cls): # needs own class
        print("in class method")

Person.class_method() # calling
