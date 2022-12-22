# Rock, Paper, Scissors Game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list1 = [rock, paper, scissors]
list2 = ["rock", "paper", "scissors"]
Y = 0
X = input("What do you want to select? rock, paper or scissors: ")
if X == "rock":
    Y = 0
if X == "paper":
    Y = 1
if X == "scissors":
    Y = 2

print (list1[Y])

Z = random.randint(0, 2)  #Z = Computer's Choice
print(f"The computer chose, {list2[Z]}.")
print(list1[Z])

if Y == 0 and Z == 1:
    print ("You Lose.")
elif Y == 0 and Z == 2:
    print ("You Win.")
elif Y == 1 and Z == 0:
    print ("You Win.")
elif Y == 1 and Z == 2:
    print ("You Lose.")
elif Y == 2 and Z == 0:
    print ("You Lose.")
elif Y == 2 and Z == 1:
    print ("You Win.")
else:
    print ("Draw.")