import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True

    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False

    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("Computer's Turn: Snake(s), Water(w) or Gun(g) ?")
randNo= random.randint(1,3)

if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

you=input("Your Turn:Snake(s), Water(w) or Gun(g) ? \n")
a=gamewin(comp,you)
print(f"Computer chose {comp}")
print(f"You chose {you}")
if a==None:
    print("This game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")