#I used the example before, and now you will code it! Let's make a car using a class and methods.
#How:
#Create a car class
#There should be an initial method that has the following properties:
#body type
#engine type 
#brand
#model
#We need some methods as well:
#Determine the cost to paint the car (the larger the more expensive). Assume truck > sedan > coupe. I don't care the actual cost, just have some sort of logic
#Determine the top speed. assume The smaller the car, and the bigger the engine, the faster it is.
#After that:
#Collect user input to populate all the properties. Create options for the user to choose from, this will make error handling and the selection process easier.

#coupe, sedan, truck
topSpeed = 0
cost2paint = 0
class Car:
        def __init__(self, brand, body, model, engine, price):
            self.brand = brand
            self.body = body
            self.model = model
            self.engine = engine
            self.price = price
        
        def car_finalized(self):
            print("Brand: " + self.brand, "\nBody: "+ self.body, "\nModel: " 
                  + self.model, "\nEngine: " + self.engine, "\nPrice: " + self.price)

print("It's time to build a car! Let's choose a brand.")
car_brands = ["Tesla", "Ford"]
car_body = ["Coupe", "Sedan", "Truck"]

tesla_coupe = ["Roadster", "Model 3"]
tesla_sedan = ["Model S"]
tesla_truck = ["Cybertruck", "Semi"]
tesla_engine = "All Tessie's are electrified. that's your only option"

ford_coupe = ["2021 Mustang", "2017 Mustang"]
ford_sedan = ["Fusion", "Maverick"]
ford_truck = ["F-150", "Escape"]

ford_coupeEngines = ["2.3L", "3.0L"]
ford_sedanEngines  = ["2L", "2.5L"]
ford_truckEngines = ["3.5L", "2.5L" ]

for x in car_brands:
    print(x)
brand = userIn = input("Which brand would you like?\n")
if userIn == "Tesla":
    print("You've chosen:",brand)
    for x in car_body:
        print(x)
    body = input("Now choose a body type:\n")
    if body == "Coupe":
        print("You've chosen:",body)
        for x in tesla_coupe:
            print(x)
        model = input("Now choose a model:\n")
        if model == "Roadster":
            print(tesla_engine)
            engine = input("Now Choose an engine: ")
            if engine == "Electrified":
                price = str(50000)
                topSpeed = str(250)
                paint = str(5500)
                price = str(50000 + 5500)
                myCar=Car(brand, body, model, engine, price)
                print("Your car...")
                
        elif model == "Model 3":
            print(tesla_engine)
            engine = input("Now Choose an engine: ")
            if engine == "Electrified":
                price = str(45000)
                topSpeed = str(162)
                paint = str(5000)
                price = str(45000 + 5000)
                myCar=Car(brand, body, model, engine, price)
                print("Your car...")
                
    elif body == "Sedan":
        print("You've chosen:",body)
        for x in tesla_sedan:
            print(x)
        model = input("Now choose a model (there's only one lol):\n")
        if model == "Model S":
            print(tesla_engine)
            engine = input("Now Choose an engine: ")
            if engine == "Electrified":
                price = str(95000)
                topSpeed = str(200)
                paint = str(5500)
                price = str(95000 + 5500)
                myCar=Car(brand, body, model, engine, price)
                print("Your car...")
            
    elif body == "Truck":
        print("You've chosen:",body)
        for x in tesla_truck:
            print(x)
        model = input("Now choose a model:\n")
        if model == "Cybertruck":
            print(tesla_engine)
            engine = input("Now Choose an engine: ")
            if engine == "Electrified":
                price = str(50000)
                topSpeed = str(110)
                paint = str(7000)
                price = str(50000 + 7000)
                print("Your car...")
            
        elif model == "Semi":
            print(tesla_engine)
            engine = input("Now Choose an engine: ")
            if engine == "Electrified":
                price = str(150000)
                topSpeed = str(200)
                paint = str(10000)
                price = str(45000 + 10000)
                myCar=Car(brand, body, model, engine, price)
                print("Your car...")

elif userIn == "Ford":
    print("You've chosen:",brand)
    for x in car_body:
        print(x)
    body = input("Now choose a body type:\n")
    if body == "Coupe":
        print("You've chosen:",body)
        for x in ford_coupe:
            print(x)
        model = input("Now choose a model:\n")
        if model == "2021 Mustang":
            for x in ford_coupeEngines:
                print(x)
            engine = input("Now Choose an engine: ")
            if engine == "2.3L" or "3.0L":
                price = str(27000)
                topSpeed = str(185)
                paint = str(2000)
                price = str(27000 + 2000)
                myCar=Car(brand, body, model, engine, price)
                print("Your car...")
         
        elif model == "2017 Mustang":
            for x in ford_coupeEngines:
                print(x)
            engine = input("Now Choose an engine: ")
            if engine == "3.0L" or "2.3L":
                price = str(25000)
                topSpeed = str(155)
                paint = str(2000)
                price = str(25000 + 2000)
                myCar=Car(brand, body, model, engine, price)
                print("Your car...")
                
    elif body == "Sedan":
        print("You've chosen:",body)
        for x in ford_sedan:
            print(x)
        model = input("Now choose a model:\n")
        if model == "Fusion":
            for x in ford_sedanEngines:
                print(x)
            engine = input("Now Choose an engine: ")
            if engine == "2L" or "2.5L":
                price = str(23000)
                topSpeed = str(150)
                paint = str(2500)
                price = str(23000 + 2500)
                myCar=Car(brand, body, model, engine, price)
                print("Your car...")
                
        elif model == "Maverick":
            for x in ford_sedanEngines:
                print(x)
            engine = input("Now Choose an engine: ")
            if engine == "2L" or "2.5L":
                price = str(20000)
                topSpeed = str(190)
                paint = str(3500)
                price = str(20000 + 3500)
                myCar=Car(brand, body, model, engine, price)
                print("Your car...") 
                
    elif body == "Truck":
        print("You've chosen:",body)
        for x in ford_truck:
            print(x)
        model = input("Now choose a model:\n")
        if model == "F-150":
            for x in ford_truckEngines:
                print(x)
            engine = input("Now Choose an engine: ")
            if engine == "3.5L" or "2.5L":
                price = str(30000)
                topSpeed = str(165)
                paint = str(4000)
                price = str(30000 + 4000)
                print("Your car...")
            
        elif model == "Escape":
            for x in ford_truckEngines:
                print(x)
            engine = input("Now Choose an engine: ")
            if engine == "3.5L" or "2.5L":
                price = str(25000)
                topSpeed = str(293)
                paint = str(4500)
                price = str(25000 + 4500)
                print("Your car...")


myCar = Car(brand, body, model, engine, price)
myCar.car_finalized() 
print("Your Top Speed is:",topSpeed,"mph and paint job was:",paint)         
            
