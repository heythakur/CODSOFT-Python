import random

score = 0
decision = ""
CPU_choice = ""
USER_choice = ""

def won():
    global decision, score
    decision = "* YOU WON *"
    score += 1  
    
def lose():
    global decision, score
    decision = "* YOU LOSE *"
    score -= 1 
    
def draw():
    global decision
    decision = "*DRAW*\t"


def rpc_Game(choice1):
    global CPU_choice, USER_choice
    
    rpc_options = ["Rock", "Paper", "Scissors"]
    CPU_choice = random.choice(rpc_options)
    
    if choice1 == 1: 
        USER_choice = "Rock"
        if CPU_choice == "Paper":
            lose()
        elif CPU_choice == "Scissors":
            won() 
        else:
            draw()
            
    elif choice1 == 2:
        USER_choice = "Paper"
        if CPU_choice == "Scissors":
            lose()  
        elif CPU_choice == "Rock":
            won()
        else:
            draw()   
                     
    elif choice1 == 3:  
        USER_choice = "Scissors"
        if CPU_choice == "Rock":
            lose
        elif CPU_choice == "Paper":
            won() 
        else:
            draw()             
    
    

#Main_Body()
print("\t** Welcome to Rock-Paper-Scissors Game **")

round = 1

while True:
    print("\n\t\t 1. Rock \n\t\t 2. Paper \n\t\t 3. Scissors")
    choice1 = int(input("\n\t\tChoice (1, 2, 3): "))
    
    if choice1==1 or choice1==2 or choice1==3:
        rpc_Game(choice1) 
        print("-" * 50)
        print("ROUND", round, "\n")
        print("\tUser:", USER_choice, "\tCPU:", CPU_choice)
        print("\n\t",decision, "\tScore:", score)
        print("-" * 50)
        
        while True:
            more_rounds = input("\nAnother Round? (Y/N): ")
            if more_rounds=='N' or more_rounds=='n':
                print("\nFinal Score:",score,"\nExiting Program. \n")
                exit()
            elif more_rounds=='Y' or more_rounds=='y':
                break
            else:
                print("\nInvalid Input \nPlease Try Again")
                
        round+=1  
        
    else:
        print("\nInvalid Input \nPlease Try Again\n\n")