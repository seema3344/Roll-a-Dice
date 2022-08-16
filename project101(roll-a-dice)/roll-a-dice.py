import random

response = input("y to roll a dice and n to exit :")

y = response 

no = random.randint(1,6)
   

if(response == y):
    
 if(no == 1):
    print("[ ----- ]")
    print("[       ]")
    print("[   0   ]")
    print("[       ]")
    print("[ ----- ]")
 if(no == 2):
    print("[ ----- ]")
    print("[       ]")
    print("[  0 0  ]")
    print("[       ]")
    print("[ ----- ]")
 if(no == 3):   
    print("[ ----- ]")
    print("[       ]")
    print("[ 0 0 0 ]")
    print("[       ]")
    print("[ ----- ]")
 if(no == 4):
    print("[ ----- ]")
    print("[ 0   0 ]")
    print("[       ]")
    print("[ 0   0 ]")
    print("[ ----- ]")
 if(no == 5):
    print("[ ----- ]")
    print("[ 0   0 ]")
    print("[   0   ]")
    print("[ 0   0 ]")
    print("[ ----- ]")
 if(no == 5):
    print("[ ----- ]")
    print("[ 0   0 ]")
    print("[ 0   0 ]")
    print("[ 0   0 ]")
    print("[ ----- ]")

