'''
1 for stone
-1 for paper
0 for scissor
'''
import random
computer = random.choice([-1,0,1])
print("s-stone ,p-Paper,S-secissor")
youstr=input("Enter your choise:")
youdict={"s":1,"p":-1,"S":0}
revdict={1:"stone",-1:"Paper",0:"Scissor"}
you=youdict[youstr]

print(f"You chose {revdict[you]} and computer chose {revdict[computer]}")

if(computer == you): 
    print("Draw")

if(computer == -1 and you == 1): 
    print("Computer win")

elif(computer==-1 and you==0):
    print("You win")

elif(computer==0 and you==1):
    print("You win")

elif(computer==0 and you==-1):
    print("Computer win")

elif(computer==1 and you==-1):
    print("You win")

elif(computer==1 and you==0):
    print("Computer win")
else:
    print("Select valid item")

