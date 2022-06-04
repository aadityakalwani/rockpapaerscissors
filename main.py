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


play_or_not = ""
while play_or_not.lower() != "q":
  print(play())
  play_or_not = input("enter 'q' to quit playing, anything else assumes that you want to continue playing\n")