# Rock, Paper, Scissor Game 
import random

mylist=["rock","scissors","paper"]
print("Enter rock,paper or scissor")
player1=input()

#Validating input
if (player1=="rock" or player1=="paper" or player1=="scissor"):
  print("Valid input. Let's play")
else:
  print("Invalid input. Enter rock, paper or scissor only")

#Computer generating choice
player2=random.choice(mylist)
print("Computer chose", player2)

#game logic
if (player1=="rock" and player2=="rock"):
  print("No one wins")
elif (player1 == "rock" and player2=="paper"):
  print("Paper covers the rock. Therefore, computer wins")
elif (player1== "rock" and player2== "scissor"):
  print("Rock smashes the scissor. Therefore, computer wins")

if (player1=="paper" and player2=="paper"):
  print("No one wins")
elif (player1 == "paper" and player2=="rock"):
  print("Paper covers the rock. Therefore, you win")
elif (player1== "paper" and player2== "scissor"):
  print("Scissor cuts the paper. Therefore, computer wins")

if (player1=="scissor" and player2=="scissor"):
  print("No one wins")
elif (player1 == "scissor" and player2=="paper"):
  print("Scissor cuts the paper. Therefore, you win")
elif (player1== "scissor" and player2== "rock"):
  print("Rock smashes the scissor. Therefore, computer wins")






