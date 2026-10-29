import random
guess=int(input("Guess a number between 1 to 100: "))
n=random.randint(1,100)
attemts=0
while True:
    attemts+=1
    if guess>n:
      print("Too high")
      guess=int(input("Guess Again: "))
    elif guess<n:
      print("Too low")
      guess=int(input("Guess Again: "))
    elif guess==n:
     print("Congratualtions! You guessed it!")
     print("Attemts:",attemts)
     break
    else:
      print("Invalid")
