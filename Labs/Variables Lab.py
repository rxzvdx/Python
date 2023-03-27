#1. Write a variable called myName and set your name equal to it
   #a. What data type is it? How do you know?
#2. Write a variable called bannerId, and set it equal to your bannerId
   #a. What data type is it? How do you know?
#3. Print a sentence, something along the line of Hello, my name is (the variable for your
#name), and my banner id is (variable for banner id).
#4. Write a variable called num1, assign a value of 20.5
   #a. What data type is it? How do you know?
#5. Write a variable called num2, assign a value of 10
   #a. What data type is it? How do you know?
#6. Add num1 and num2, and set a variable num3 equal to it.
   #a. Print num3
   #b. What data type is num3? How do you know?
#7. Create a list of all five variables, called myList
   #a. Print all elements of your list

#8. Ask a user for their a number, then another, and another. I want you to then state what those numbers are, then add them together. Once that is done, find the average. And state the average.

#variables lab
myName = 'Antonio Rosado'
#This data type is a string because it's a collection of certain characters.

bannerID = '916379878'
#This data type is a float, as it's a number with multiple decimal places behind it.

print("Hello my name is " +myName+ " my banner ID is " +bannerID)

num1=20.5
#This data type is a float, because its a numeric value wit a decimal place.

num2=10
#This data type is an integer because it's a whole number. 

num3=num1+num2
print(num3)
#This data type is an operator as it adds two integers together using arithmetic. 

myList = [myName, bannerID, num1, num1, num3]
print(myList)

userInput = input('Give me a number')
userInput2 = input('Give me another number')
userInput3 = input('Give me one final number')

print ((float(userInput) + float(userInput2) + float(userInput3))/int(3))