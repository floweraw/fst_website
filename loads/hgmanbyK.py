import random

#####define
cntry=["india"]
r=random.choice(cntry)
wl=[]
rl=[]
######interface
print("-"*len(r))

for x in r:
    rl.append(x)
for x in ("-"*len(r)):
    wl.append(x)

#######how many points
points=10
#####main code goes heree
w=""
while r!=w:

    ltr=input("guess the letters :")
    ltr=ltr[0]
    
    if ltr not in rl:
        print(ltr," -letter in not in the word")
        points=points-1
    while ltr in rl:
        idx=rl.index(ltr)
        wl[idx]=ltr
        rl[idx]="-"
        #######list->string
    w=""
    for x in wl:   
        w=w+x
    print(w)
    if points==0:
        print("game over")
        break
######################
print("you won the game \nyour score is-",points)

