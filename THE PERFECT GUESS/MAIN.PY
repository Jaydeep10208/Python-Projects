import random
n = random.randint(0,100)
a = -1
guess = 1
while(a!=n):
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower Number please")
    elif(a<n):
        print("higher number please")
    guess +=1 

print(f"You guess correct number {n} in {guess} attempt")