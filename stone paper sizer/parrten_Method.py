'''
    computer - you # Parttens
    -2 and 1 computer win
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

if(computer - you ==  1)and (computer-you == -2):
    print("You lose")
else:
    print("You win")