#This is Mr. Poppins, and he's a princess. That's my problem generally, but today, it's yours too. He randomly decides on a whim if he wants wet or dry food. The thing is, the type of wet or dry isn't enough, the brand he desires always changes. This results in me offering him between 1 - let's say 8 kinds of food every meal. The amount he eats each time is random too, so he must be fed multiple times a day (like 8). Anyway do the following:

#Create a 2 collections of food, wet and dry. Each collection should have several brands of food (4 each)

#Program some cat logic (Random selection) where Poppins will secretly choose what he wants to eat between the 2 collections.

#A user should then try to guess what food he wanted. If correct, Poppins was fed 1 meal. If incorrect, but the type is correct (you both chose a dry food, but not the same dry food), Poppins is fed 1/2 a meal. If the type, and brand are wrong, he skips the meal. Either way, remove that choice from its collection.

#Poppins should RANDOMLY decide if he wants 4 - 6 feedings. However, in order for the user to do an acceptable job, they must succeed in their selections at least 50% of the time.

#Every time a player must guess, Mr. Poppins should have made another new random selection (remember, he's annoying).

#You must include error handling as well. Hint: Two methods you might thank me for isdigit(), and isalpha()

#Also, remember, he's a good boy!

dry_list = ["Blue Buffalo","Purina","Cat Chow","Iams"]
wet_list = ["Nine Lives", "Purina ONE", "Rachel Ray", "Sheba"]

mealsEaten = 0
wrong_attempts = 0

import random

poppins_amountChoice = random.randint(4, 6)

print("Mr. Poppins is hungry... \nHe has to choose from:")
print("Dry Foods \nWet Foods")


while mealsEaten < poppins_amountChoice  and wrong_attempts < 6:
    cat_choice = random.choice(['Dry Foods', 'Wet Foods'])
    cat_choice2 = random.choice(dry_list)
    cat_choice3 = random.choice(wet_list)
    x = input("Which food type will you give Mr. Poppins? \n")
    print("Mr. Poppins chose:", cat_choice)
    if (x == cat_choice):
        print("Mr. Poppins is in the mood for that type! Now what kind of food from that type will you choose?")

#If user and poppins both choose dry foods

    if (x == "Dry Foods" and cat_choice == "Dry Foods"):
        mealsEaten += 0.5
        print("\nDry Foods...")
        for x in dry_list:
            print(x)
        y = input("Which dry food will you give Mr. Poppins? \n")

        if (y == "Blue Buffalo" and cat_choice2 == y ):
            print("Fantastic! Mr. Poppins loves it!")
            mealsEaten += 1.0
            print("Meals Eaten:",mealsEaten)
            dry_list.remove("Blue Buffalo")
    
        elif (y == "Purina" and cat_choice2 == y ):
            print("Fantastic! Mr. Poppins loves it!")
            mealsEaten += 1.0
            print("Meals Eaten:",mealsEaten)
            dry_list.remove("Purina")
                
        elif (y == "Cat Chow" and cat_choice2 == y ):
            print("Fantastic! Mr. Poppins loves it!")
            mealsEaten += 1.0
            print("Meals Eaten:",mealsEaten)
            dry_list.remove("Cat Chow")
                    
        elif (y == "Iams" and cat_choice2 == y ):
            print("Fantastic! Mr. Poppins loves it!")
            mealsEaten += 1.0
            print("Meals Eaten:",mealsEaten)
            dry_list.remove("Iams")
                
        elif (y != cat_choice2):
                wrong_attempts = wrong_attempts +1
                dry_list.remove(y)
                print("Mr. Poppins chose:",cat_choice2)
                print("He did want dry food, but not THAT dry food :( try again!")
                mealsEaten += 0.5
                print("Meals Eaten:",mealsEaten)
                
#If user and poppins both choose wet foods
    elif (x == "Wet Foods" and cat_choice == "Wet Foods"):
        print("\nWet Foods...")
        for x in wet_list:
            print(x)
        z = input("Which wet food will you give Mr. Poppins? \n")
        if (z == "Nine Lives" and cat_choice3 == z ):
            print("Fantastic! Mr. Poppins loves it!")
            mealsEaten+= 1.0
            print("Meals Eaten:",mealsEaten)
            wet_list.remove("Nine Lives")

        elif (z == "Purina ONE" and cat_choice3 == z ):
            print("Fantastic! Mr. Poppins loves it!")
            mealsEaten+= 1.0
            print("Meals Eaten:",mealsEaten)
            wet_list.remove("Purina ONE")
        
        elif (z == "Rachel Ray" and cat_choice3 == z ):
            print("Fantastic! Mr. Poppins loves it!")
            mealsEaten+= 1.0
            print("Meals Eaten:",mealsEaten)
            wet_list.remove("Rachel Ray")
                
        elif (z == "Sheba" and cat_choice3 == z):
            print("Fantastic! Mr. Poppins loves it!")
            mealsEaten+= 1.0 
            print("Meals Eaten:",mealsEaten)
            wet_list.remove("Sheba")
        elif (z != cat_choice3):
                wrong_attempts = wrong_attempts +1
                wet_list.remove(z)
                print("Mr. Poppins chose:",cat_choice3)
                print("He did want wet food, but not THAT wet food :( try again!")
                mealsEaten += 0.5
                print("Meals Eaten:",mealsEaten)
    
    elif (mealsEaten >= poppins_amountChoice):
        print("Mr. Poppins has eaten enough today! (Thank god)")
        
    elif (x != cat_choice):
        False
        print("Mr. Poppins doesn't like that one :( try again!")
    
else:
    wrong_attempts = wrong_attempts + 1





