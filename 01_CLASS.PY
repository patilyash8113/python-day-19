# "OOPs is basically a way to model what we write in a program to the real world." 

# A CLASS: A Class is a blurprint or a template.EG. form for a exam that contain name,age,electives,fathers name etc...

# object: specific instance created from the template (class). eg..form which contain the data for john joe..


class employee:
    company="HP"
    c="yash"

    def get_salary(self): #self  refer to a object of a class which is beign created 
        print(self)
        return 34000
e=employee() #An object of class employee is created here
print(e.get_salary()) #Employee e's get salary method is called.
e2=employee()
print(e2.get_salary())
# print(e2.company)

    
