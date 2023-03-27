#How should I recycle this?
#Many people today recognize the benefits of recycling, but they do not know exactly how it should correctly be done. Your lab is to read the following 2 web pages, and based on the information, write a script that will ask the user:
#What do you want to recycle? Their choices should be the section headings of this article: https://www.epa.gov/recycle/how-do-i-recycle-common-recyclables#pla
#Then tell the user how it should be recycled
#Exception! Plastics are tricky when it comes to recycling. So if they enter plastic or Plastic, they should be asked a follow up question: What kind of plastic is it? (Foam, plastic bag, #1-7 plastic, or a #7 PLA plastic). Based on their answer, give them the right directions based on this article: https://www.ecocycle.org/plastics-recycling 

userIn = input("What do you want to recycle? ")

#paper
if (userIn == "Paper" or userIn == "paper"):
    print ('Most community or office recycling programs accept paper and paper products.')
#gift wrap & gift bags
elif (userIn == "Gift Wrap" or userIn == "gift wrap" or userIn == "Gift Bags" or userIn == "gift bags"):
    print ('If you use gift wrap, look to find a type that can be recycled or that is made from recycled content. Consumers can also reduce waste by using decorative boxes that do not require wrapping and that can be recycled. A lot of gift wrap isn’t recyclable because of the coating on the paper, which is often shiny and laminated. The Agency encourages consumers to reuse gift bags and tissue paper, and not discard them after a single use.')
#batteries
elif (userIn == "Batteries" or userIn == "batteries"):
    print(' For Dry cell Batteries: Look for in-store recycling bins or community collection events for disposal. \n Lithium-ion Batteries: Cannot be disposed in trash or recycling bins. Return to manufacturer/automobile dealer or installation company. \n Lithium Metal Batteries: Return lead-acid batteries to a battery retailer or local household hazardous waste collection program. \n Lead-Acid Batteries: Return to a battery retailer or hazardous waste collection program. \n Other rechargable batteries: Dedicated in-store recycling bins or household hazardous waste collection events.')
#plastic section
elif (userIn == 'Plastics' or userIn == 'plastics' or userIn == 'Plastic' or userIn == 'plastic'):
    plasticResponse = input('What kind of plastic? \n' 'Is it foam, a bag, #1-7, or #7 PLA? ')
    if (plasticResponse == 'Foam' or plasticResponse == 'foam'):
        print ('Not recyclable')
    elif(plasticResponse == 'Bag' or plasticResponse == 'bag'):
        print ('Bags with #2 or #4 can be recycled at the CHaRM (Center for Hard-to-Recycle Materials), or at participating grocery stores')
    elif(plasticResponse == '#1-7'):
        print('All plastic bottles, tubs, and jars numbered 1-7 are accepted')
    elif(plasticResponse == '#7 PLA'):
       print('Any #7 including the initials PLA is NOT accepted.')
#glass
elif (userIn == 'Glass' or userIn == 'glass'):
    print('Glass, especially glass food and beverage containers, can be recycled over and over again. Most curbside community recycling programs accept different glass types mixed together.')
#oil
elif (userIn == 'Used Oil' or userIn == 'used oil' or userIn == 'Used oil' ):
    print('Many garages and auto-supply stores that sell motor oil also accept it for recycling.')
#Household hazardous waste
elif (userIn == 'Household Hazardous Waste' or userIn == 'Household hazardous waste' or userIn == 'household hazardous waste'):
    print('Special collection events and permanent collection centers accept household hazardous waste. Sometimes the vendors of the products also accept them for recycling.')
#tires
elif (userIn == 'Tires' or userIn == 'tires'):
    print('Most garages are required to accept and recycle your used tires when you have new ones installed.')
else:
    userIn = input("Invalid Answer")

"""
Created on Sun Oct 17 23:11:28 2021

@author: rosado44
"""

