num1 = int(input("num1:")) #to put the first number
func = input("function:") #to choose which function we want to use, we can choose * , + , / -
num2 = int(input("num2:")) #to put the second number

class calculator:  #to define the class of the object
    def __init__(self,num1,num2): #to define the attribute of the object
        self.num1 = num1
        self.num2 = num2

    def plus(self): #to define the plus method of the object
        if func == "+":  #if we choose the "+" function, then it will do this calculation only
          print (self.num1 + self.num2) #to print it and count number 1 plus number 2

    def minus(self): #to define minus method of the object
        if func == "-": #if we choose the "-" function, then it will do this calculation only
            print (self.num1 - self.num2) #to print it and count number 1 minus number 2
    def divide(self): #to define the divide method of the object
        if func == "/": #if we choose the "/" function, then it will do this calculation only
            print(self.num1 / self.num2) #to print it and count number 1 divided by number 2
    def multiply(self): #to define the multiply method of the object
        if func == "*": #if we choose the "*" function, then it will do this calculation only
            print(self.num1 * self.num2) #to print it and count number1 multiplied by number 2

c = calculator(num1,num2) #to input the attribute
c.plus() #to input the plus method
c.minus() #to input the minus method
c.divide() #to input the divide method
c.multiply() #to input the multiply method


