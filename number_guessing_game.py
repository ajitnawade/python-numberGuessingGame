import random
guess=0
def guess_result(attempts):
  print(f"You Have {attempts} attempts to Guess.")
  guess=int(input("Enter Your guess : "))
  if number<guess:
    print("Too High")
    return attempts-1
  elif number>guess:
    print("Too Low")
    return attempts-1
  elif number==guess:
    print(f"You Guessed it!!!, The number was {number}")
    return exit
print("WelCome to the Guessing Game.")
print("I am Guessing the NUMBER between 1 & 100")
number=random.randint(1,100)
level = input("Choose a Difficulty level. 'easy' or 'hard' : ")
if level=='easy':
  attempts=10
  while attempts!=exit:
    attempts=guess_result(attempts) 
    if attempts==0:
      print("Out of attempts!!!")
      break
elif level == 'hard':
  attempts=5
  while attempts!=exit:
    attempts=guess_result(attempts)
    if attempts==0:
      print("Out of attempts!!!")
      break