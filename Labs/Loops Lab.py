#Requirements:
#Must use for and while loops.
#Must have a mix of conditional, collection, and counter loops.
#Use your former labs for help! *The plot lab will help you immensely.

#Objective: Plan a state based road trip. Use at least ten states.

#Present the user with the ability to start a trip, continue a trip, 
#or to end a trip.

#If they start a trip, give them an option of which state to start in
#using only one of your ten states.

#They can visit the same state (pretend they went to a different part)
#

#They may essentially teleport to any state, but they can only travel 10 times
# However,
#If they decide to prematurely end a trip, 
#tell them how many states they have visited,and what states. 

myL= ['New Jersey','New York','Pennsylvania','Tennessee','Georgia','Florida',
      'Texas',
      'New Mexico',
      'California',
      'Idaho']

dict_states = {'1' : 'New Jersey',
               '2' : 'New York',
               '3' : 'Pennsylvania',
               '4' : 'Tennessee',
               '5' : 'Georgia',
               '6' : 'Florida',
               '7' : 'Texas',
               '8' : 'New Mexico',
               '9' : 'California',
               '10' : 'Idaho'}
i = input ('Would you like to start a trip? ')
if (i == 'Yes' or i == 'yes'):
    print(myL)
if (i == 'no' or i == 'No'):
    print("You've ended your trip.")
userIn = i
statesPassed = 0
while statesPassed <=10:

    i = input ('Where would you like to go? ')
    
    if (i == 'New Jersey'):
                statesPassed = statesPassed + 1
                print('\n' "Welcome to the Garden State, home of casinos nobody cares about!")
                print("States Passed:", statesPassed)
                print("Where would you like to go next?", myL)
              
    elif (i == 'New York'):
                statesPassed = statesPassed + 1
                print("Welcome to New York, lots of traffic but hey you got to see the Statue of Liberty for 15 minutes.")
                print("States Passed:", statesPassed)
                print("Where would you like to go next?", myL)
                
    elif (i == 'Pennsylvania'):
                statesPassed = statesPassed + 1
                print("Welcome to Pennsylvania home of the Liberty Bell!")
                print("States Passed:", statesPassed)
                print("Where would you like to go next?", myL)
            
    elif (i == 'Tennessee'):
                statesPassed = statesPassed + 1
                print("Welcome to Tennessee! I think they've got chicken idk.")
                print("States Passed:", statesPassed)
                print("Where would you like to go next?", myL)
                 
                 
    elif (i == 'Georgia'):
                statesPassed = statesPassed + 1
                print("Welcome to Georgia! Don't forget to grab some peaches!")
                print("States Passed:", statesPassed)
                print("Where would you like to go next?", myL)
                 
    elif (i == 'Florida'):
                statesPassed = statesPassed + 1
                print("Welcome to Florida, where even during a global pandemic they don't stop partying!")
                print("States Passed:", statesPassed)
                print("Where would you like to go next?", myL)
                 
    elif (i == 'Texas'):
                statesPassed = statesPassed + 1
                print("Yee haw Welcome to Texas! Best BBQ in the country!")
                print("States Passed:", statesPassed)
                print("Where would you like to go next?", myL)
                    
    elif (i == 'New Mexico'):
                statesPassed = statesPassed + 1
                print("Welcome to New Mexico, it's Mexico...but NEW!")
                print("States Passed:", statesPassed)
                print("Where would you like to go next?", myL)
                 
    elif (i == 'California'):
                statesPassed = statesPassed + 1
                print("Welcome to Cali, where there's so damn much to do not even this loop can fit it all!")
                print("States Passed:", statesPassed)
                print("Where would you like to go next?", myL)
                  
    elif  (i == 'Idaho'):
                statesPassed = statesPassed + 1
                print("Welcome to Idaho, they've got potatoes or whatever...")
                print("States Passed:", statesPassed)
                print("Where would you like to go next?", myL)
    
    elif (i == 'end' or i  == 'End'):
       print("Your trip has ended.")
       print("States Passed:")
       print(statesPassed)
       print("You visited: \n")
       for y in myL:
           print(y)
       
    if statesPassed >=10:
        print("\n You've completed your trip! \n You've visited: \n", myL)
        break


  
    
#TEN STATES so I don't have to type them again
#New Jersey
#New York
#Pennsylvania
#Tennessee
#Georgia
#Florida
#Texas
#New Mexico
#California
#Idaho

#state template 2 because im lazy lol
    #elif (i== ''):
   #print("")
     #statesPassed=statesPassed +1
       #print("States Passed:")
       #print(statesPassed)
       #break


   
