#Let's make a calculator using functions:

#1) It will need to accept user input (At several different points)

#2) Each mathematic operation needs to be it's own function/method:

#Addition - Takes up to 5 arguments
#Subtraction - - Takes 3 arguments
#Multiplication - Takes 4 arguments
#Division - Takes 2 arguments
#Log - Takes 1 argument
#Raise a number to a power ex. X squared
#Solve Pythagorean theorem
#Factorial
#3)  Create the ability for a user to use up to 3 of the aforementioned operations together. Example, I can add 5 numbers making result X. I may then take X, and divide it by 4, generating result Y. That's an example of 2, but you get the idea.  

import math

#addition functions
def add(num1,num2):
    return(num1+num2)

def add3(num1,num2,num3):
    return(num1+num2+num3)

def add4(num1,num2,num3,num4):
    return(num1+num2+num3+num4)

def add5(num1,num2,num3,num4,num5):
    return(num1+num2+num3+num4+num5)

#subtraction functions
def subtract(num1,num2):
    return(num1-num2)

def subtract3(num1,num2,num3):
    return(num1-num2-num3)

#multiplication functions
def multiply(num1,num2):
    return(num1*num2)

def multiply3(num1,num2,num3):
    return(num1*num2*num3)

def multiply4(num1,num2,num3,num4):
    return(num1*num2*num3*num4)

#division function
def divide(num1,num2):
    return(num1/num2)

#natural log function
def nLog(num1):
    return(math.log(num1))

#log with specified base function
def log(num1,num2):
    return(math.log(num1,num2))

#power function
def power(num1,num2):
    return(num1**num2)

#pythagorean theorem function
def pythagorean(num1,num2):
    return(num1**2+num2**2)

#factorial function
def factorial(num1):
    return(math.factorial(num1))

print("Select a mathematic operation to perform: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Natural Logarithm")
print("6. Log(x)")
print("7. Power")
print("8. Pythagorean Theorem")
print("9. Factorial")
print("10. Freestyle")
operation = input()


if operation == "1":
    #addition
    userIn = input("You can add up to 5 numbers. How many numbers will you be adding? \n")
    if userIn == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("The answer is: ", add(num1,num2))
    elif userIn == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        print("The answer is: ", add3(num1,num2,num3))
    elif userIn == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))
        print("The answer is: ", add4(num1,num2,num3,num4))
    elif userIn == "5":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))
        num5 = float(input("Enter fifth number: "))
        print("The answer is: ", add5(num1,num2,num3,num4,num5))
    else:
        print("ERROR")
        
elif operation == "2":
    #subtraction
    userIn2 = input("You can subtract up to 3 numbers. How many numbers will you be subtracting? \n")
    if userIn2 == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("The answer is: ", subtract(num1,num2))
    elif userIn2 == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        print("The answer is: ", subtract3(num1,num2,num3))
    else:
        print("ERROR")
        
elif operation == "3":
    #multiplication
    userIn3 = input("You can multiply up to 4 numbers. How many numbers will you be multiplying? \n")
    if userIn3 == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("The answer is: ",multiply(num1,num2))
    elif userIn3 == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        print("The answer is: ",multiply3(num1,num2,num3))
    elif userIn3 == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))
        print("The answer is: ",multiply4(num1,num2,num3,num4))
    else:
        print("ERROR")
        
elif operation == "4":
    #division
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The answer is: ",divide(num1,num2))
    
elif operation == "5":
    #Natural Logs
    num1 = float(input("Enter a number: "))
    print("The answer is: " ,nLog(num1))

elif operation == "6":
    #Log with specified base 
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The answer is: " ,log(num1,num2))
    
elif operation == "7":
    #Powers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The answer is: " ,power(num1,num2))
    
elif operation == "8":
    #Pythagorean Theorem
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("The answer is: " ,pythagorean(num1,num2))
    
elif operation == "9":
    #Factorial
    num1 = float(input("Enter a number: "))
    print("The answer is: " ,factorial(num1))

elif operation == "10":
    #Freestyle
    print("1. Add/Divide/Subtract")
    print("2. Power/Multiply/Power")
    print("3. Pythagorean Theorem/Divide/Natural Log")
    i2 = input("Select from one of the above to mess around with \n")
    if i2 == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        x = add(num1,num2)
        print("The answer is: ", add(num1,num2))
        print("What would you like to divide",x,"by?")
        num3 = float(input("Enter a divisor: "))
        y = divide(x,num3)
        print("The answer is:", y)
        print("What would you like to subtract from",y,"?")
        num4 = float(input("Enter a number to subtract by: "))
        z = subtract(y,num4)
        print("The answer is:",z)
    
    elif i2 == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        x2 = power(num1,num2)
        print("The answer is: " ,power(num1,num2))
        print("What would you like to multiply",x2,"by?")
        num3 = float(input("Enter a number: "))
        y2 = multiply(x2,num3)
        print("The answer is:",y2)
        print("You will be increasing", y2,"by the power of a number")
        num4 = float(input("Enter your previous answer: "))
        num5 = float(input("Now enter the power you want to increase it by: "))
        z2 = power(num4,num5)
        print("The answer is: " ,z2)
        
    elif i2 == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("The answer is: " ,pythagorean(num1,num2))
        x3 = pythagorean(num1,num2)
        print("What will you divide",x3,"by?")
        num3 = float(input("Enter a divisor: "))
        y3 = divide(x3,num3)
        print("The answer is:", y3)
        print("You will be taking the natural log of your previous answer,")
        num4 = float(input("Enter that previous answer: "))
        z3 = power(y3,num4)
        print("The answer is: " ,z3)
        
        
        
else:
    print("This calculator is not cool enough for that. Just enter a number, a college student made this lol.")
