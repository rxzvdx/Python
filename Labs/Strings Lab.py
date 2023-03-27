#'''
#Spiderman, Spiderman
#Does whatever a spider can.
#Spins a web, any size.
#Catches thieves- just like flies.
#Look out! Here comes the Spiderman.
#Is he strong? Listen, bud.
#He's got radioactive blood.
#Can he swing, from a thread?
#Take a look overhead.
#Hey, there! There goes the Spiderman!
#In the chill of night, at the scene of a crime
#like a streak of light
#he arrives, just in time!
#Spiderman, Spiderman
#friendly neighborhood Spiderman.
#Wealth and fame? He's ignored.
#Action is his reward.
#Look out! There goes the Spiderman!
#'''

#Hey, so I really like Marvel comics (Especially Spider-Man), I grew up reading them, and watching the shows. 
#I even watched the 40's cartoons where this theme song came from, and now you have to learn it too.

#Using ONLY my variables (below) and any functions and methods you know, recreate the lyrics above EXACTLY.  You cannot modify my variables, and you cannot make your own.    
#Your output in ever sense must look like the block of lyrics above; format, spelling, etc.

#**Also, I want it all done in a single print statement. :)




name = "Spiderman"
verse1 = "Does whatever a can.Spins a web, any size.Catches thieves- just like flies.Look out! Here comes the "
verse2 = "Is he strong? listen, bud.He's got adioactive blood.Can he swing, from a thread?Take a look overhead.Hey, there! There goes the!"
verse3 = "In the chill of night, at the scene of a crimelike a streak of lighthe arrives, just in time!"
verse4 = "friendly neighborhood Wealth and fame? He's ignored.Action is his reward.Look out! There goes the "

print (name+ ",",name,'\n',
       verse1[0:15],
       name[0:6]+verse1[15:20], '\n',
       verse1[20:42], '\n',
       verse1[42:74], '\n',
       verse1[75:]+name+verse1[19], '\n',
       verse2[0:26], '\n', 
       verse2[26:34],""+name[5]+verse2[35:52], '\n',
       verse2[52:80], '\n',
       verse2[80:101], '\n',
       verse2[101:127],""+name+verse2[127], '\n',
       verse3[0:46], '\n',
       verse3[46:68], '\n',
       verse3[68:93], '\n',
       name+ ",",name,'\n',
       verse4[0:21],""+name+verse1[19],'\n',
       verse4[21:52], '\n',
       verse4[52:73],
       verse4[73:97],""+name+verse2[127])



