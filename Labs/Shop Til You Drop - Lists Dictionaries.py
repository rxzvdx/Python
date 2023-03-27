#Using a Blend of Lists and Dictionaries and whatever else you desire, I want you to make a grocery store. You must include the following:
#1.Make several unique grocery aisles 4 minimum
#2.Each aisle should contain at least 5 items.
#3.Each item should have a price attached to it 
#4.Let a user choose to purchase several items
#5. A user should be able to navigate the aisles
#6. A user should only see items while they are in a specific aisle (Ex. I can't see lobster while I'm in the dairy section)
#7.A user should be able to view their cart of current items with its total
#Extra Credit: Add the ability to remove items from their cart

print("Welcome To the Python Grocery Store! \n Your Choices are...")

myList = ['Aisle 1: Grains & Bread', 'Aisle 2: Meat, Poultry, Butcher Items', 
       'Aisle 3: Frozen Items', 'Aisle 4: Fresh Produce']

firstAisle =  ['White Bread $2.00','Oatmeal $4.00','Bagels $2.75','Wheat Bread $2.50','Cereal $3.50']

secondAisle =  ['Ground Beef $4.76','Chicken $1.54', 'Turkey $1.60', 'Pork $2.50','Salmon $19.00']

thirdAisle =  ['Frozen Pizza $3.34','Frozen Veggies $1.64', 'French Fries $1.68', 'Ice Cream $4.50','TV Dinners $3.00']

fourthAisle = ['Fruits $2.00', 'Veggies $2.67', 'Nuts $5.50', 'Flowers $35.00', 'Honey $2.00']

dict_items = {"White Bread" : float(2.00), 
                "Oatmeal" : float(4.00), 
                "Bagels" : float(2.75), 
                "Wheat Bread" : float(2.50), 
                "Cereal" : float(3.50),
                "Ground Beef" : float(4.76),
                "Chicken" : float(1.54), 
                "Turkey" : float(1.60), 
                "Pork" : float(2.50), 
                "Salmon" : float(19.00),
                "Frozen Pizza" : float(3.34), 
                "Frozen Veggies" : float(1.64), 
                "French Fries" : float(1.68), 
                "Ice Cream" : float(4.50), 
                "TV Dinners" : float(3.00),
                "Fruits" : float(2.00),
                "Veggies" : float(2.67),
                "Nuts" : float(5.50),
                "Flowers" : float(35.00),
                "Honey" : float(2.00)}



cartItems = []
cartTotal = []
grandTotal = 0

groceryAisles = 0
while groceryAisles<4:
    print(myList)
    userIn = input("Which Aisle would you like to go to? \n")
    
    if (userIn == "Aisle 1"):
       print("Aisle 1 has... \n")
       for item in firstAisle:
           print(item)
       x = Aisle1 = input("Choose your item for Aisle 1 (Don't worry, you can come back!) \n")
       print("You've Chosen:", x)
       cartItems.append(x)
       cartTotal.append(dict_items.get(x))
       groceryAisles = groceryAisles + 1
       Aisle1_total = dict_items.get(x)
       print("Your Total for Aisle 1: ", Aisle1_total,"\n")
       
    elif (userIn == "Aisle 2"):
       print("Aisle 2 has... \n")
       for item in secondAisle:
           print(item)
       x = Aisle2 = input("Choose your item for Aisle 2 (Don't worry, you can come back!)\n")
       print("You've Chosen:", x)
       cartItems.append(x)
       cartTotal.append(dict_items.get(x))
       groceryAisles = groceryAisles + 1
       Aisle2_total = dict_items.get(x)
       print("Your Total for Aisle 2: ", Aisle2_total,"\n")
       
    elif (userIn == "Aisle 3"):
       print("Aisle 3 has... \n")
       for item in thirdAisle:
           print(item)
       x = Aisle3 = input("Choose your item for Aisle 3 (Don't worry, you can come back!) \n")
       print("You've Chosen:", x)
       cartItems.append(x)
       cartTotal.append(dict_items.get(x))
       groceryAisles = groceryAisles + 1
       Aisle3_total = dict_items.get(x)
       print("Your Total for Aisle 3: ", Aisle3_total,"\n")
 
    elif (userIn == "Aisle 4"):
       print("Aisle 4 has... \n",)
       for item in fourthAisle:
           print(item)
       x = Aisle4 = input("Choose your item for Aisle 4 (Don't worry, you can come back!) \n")
       print("You've Chosen:", x)
       cartItems.append(x)
       cartTotal.append(dict_items.get(x))
       groceryAisles = groceryAisles + 1
       Aisle4_total = dict_items.get(x)
       print("Your Total for Aisle 4: ", Aisle4_total,"\n")
if groceryAisles >=4:
       grandTotal = sum(cartTotal)
       print("\n Your cart: \n", cartItems, "\n Your total: \n", "$",grandTotal)
       y = input("Is there anything you would like to remove? (If yes, type what) \n")
       cartItems.remove(y)
       z = grandTotal - dict_items.get(y)
       print("\n Your cart: \n", cartItems, "\n Your NEW total: \n", "$",z)
