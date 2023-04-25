cost=0
states=2
currentState=input("Enter Current State(L or R):")
Ldirt = input("Is Left Side Dirty(T/F)")
Rdirt = input("Is Right Side Dirty(T/F)")

while(states>0):
    if(Ldirt=="F" and Rdirt =="F"):
        print("All sides Clean")
        break
    if(currentState=="L"):
        if(Ldirt=="T"):
            print("Performing Suck to Clean Left")
            cost +=1
            Ldirt="F"
        if(Rdirt=="T"):
            print("Moving to Right")
            currentState="R"
            cost +=1
            print("Performing Suck to Clean Right")
            Rdirt="F"
            cost +=1
    
    if(currentState=="R"):
        if(Rdirt=="T"):
            print("Performing Suck to Clean Right")
            cost +=1
            Rdirt="F"
        if(Ldirt=="T"):
            print("Moving to Left")
            currentState="L"
            cost +=1
            print("Performing Suck to Clean Left")
            Ldirt="F"
            cost +=1
    states -=1
print("\nCost: ",cost)
    