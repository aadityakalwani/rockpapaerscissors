import random

def play():
  user = (input("Enter the move you want to make\ntype 'r' for rock, 'p' for paper and 's' for scissors:\n"))
  computer = random.choice(["r", "p", "s"])
  print(f"the computer chose {computer}")

  if user == computer:
    return "draw"

  if is_win(user,computer):
    return "you won!"

  return "you lost huge L"

def is_win(player, opponent):
  if player == "r" and opponent == "s" or player == "p" and opponent == "r" or player == "s" and opponent == "p":
    return True
    
# while loop that says 'while game is not won'

print(play())
