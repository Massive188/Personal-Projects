#simple program
#WORK IN PROGRESS
#WORK IN PROGRESS 
#RESEARCHING...

# print introduction for the game
print("Simple first game build")

print("you will have a ten lives")

print("if your lives reaches 0 you lose, simple right")


# player will input name here
name = input("What is your name:")

age = int(input("What is your age: "))

# rules
health = 10

damage = 10 

direction = input("What alley will you choose Right or Left:")

healed = 5

total = health - damage


#if the player age is greater or equal to 18
if age >= 18:
    print("Your old enough to play")

    # if not 18 and older, player will be forced to enter his/her age again.
else: 
    while age < 18:
            print("Your not old enough to play")
            age = int(input("What is your age:"))

# if player decides to turn right
if direction ==  "Right":                            
    
    print("you went through a lake and a snake bit you, you lose",damage)
    
    print("you have", health, "health left")
    
    print(health)
    

#if player picks left
elif direction == "left":

     night=print("you went back to your camp and slept there for the night")
        
 
if health == 10:
      
        limit = healed != health
 
else:
    
    limit_health_range = healed + health

    heal2=print("you have gain a total",total,"health your health bar has reached its limit of 10 health")
    
# decision whether the player wants to get go in the cave
lake = input("A cave can be seen in the distance will you go through the cave yes or no:")

#if player picks "yes" to go in the cave
if lake:
    
    print("With its narrow passages, flowing eams, and chambers studded with stalagmites and stalactites you spot a golden sword")
    
    decision = input("Do you want to pull the sword out of the ground yes or no:")

#if decide to go in the cave.
    if decision == "yes":
            
            print("the ground start rumbling and rocks starts falling, one of the rocks fell on your head you lose", total,"health")
            
  #if player decide to not get in the cave.
    elif decision == "no":
            
            night=print("you went back to your camp and slept there for the night")
            
            heal = health + 5
            
            heal2=print("you have gain a total",heal,"health your health bar has reached its limit of 10 health")

            Nextday = input("Next day, you went back where the cave was and started to decided again to whether go in the cave yes or no:")
            
            #if player decide "no"
            
            if Nextday == "no":
                
                print(night)
                
                if health == 10:
                    limit = healed != health
                else:
                    limit_health_range = healed + health

                print(heal2)
        
           #if player decides "yes"
            elif Nextday == "yes":
                print("you went inside the cave and spotted a sleeping bear,behind the bear there an entrance to the caverns where the dimonds are stored in.what will you do ")
                print("decide",'A == Kick the bear and run away\n',
                                'B == Slowly walk pass the bear\n',    
                                'C == Go back to camp\n',                             
                                'D == Shoot the bear\n',                     
                                'E == Bear trap\n'   )
                dec = input("decide an action to take:")
#Different type of decision for the player to decide to which action to take. 
def decision2(A,B,C,D,E):
     A == 'Kick the bear and run away'
     B == 'Slowly walk pass the bear'    
     C == 'Go back to camp'                             
     D == 'Shoot the bear'                     
     E == 'Bear trap'                 

     # if player pick A 
     
        if decision2 == A: 
         print("You kicked the bear and it woke up, it slashes you, you lose",total,"health")
     
    # if player pick B
     
        elif decision2 == B:
            print('you start walking quietly around the bear, you step on a stick it snaps!!, the bear wakes up and slashes your head off, you lose',total,'health')
           
     # if player pick C     
     
        elif decision2 == C:
          print("you went back to your camp and slept there for the night")
          heal = health + healed
          print("you have gain a total",heal,"health your health bar has reached its limit of 10 health")
          nextmorning = input("Next day, you went back where the cave was and started to decided again to whether go in the cave yes or no:")  
       
     # if player decides to go back to camp, on the nextmorning, the same questions will be asked again.   
        if nextmorning == "yes":
            
            def decision2(A,B,C,D,E):
                A == 'Kick the bear and run away'
                B == 'Slowly walk pass the bear'    
                C == 'Go back to camp'                             
                D == 'Shoot the bear'                     
                E == 'Bear trap'
     
    
    elif decision2 == D:
         print("you shot the bear, and the bear still hasnt fallen, you lose",total,"health")

     
    
    elif decision2 == E:
         print("you placed a trap on the entrance of the cave")
         print("you hit the bear and run away")
         print("you forgot about the trap, and get caught on the trap, you lose",total,"health","then the bear get to you and eats you, you lose",total,"health")
         print(health)

if health == 0: 
    print("you lose try again")

elif lake == "no":
        print("Mission Fail")
    
elif direction == "left":
        print("you lose try again")
        name = input("What is your name:")

