# imports 
import os, sys, time, random

# O Bunch Of Variables
HEALTH = 100
DISEASE = False
HUNGER = ["🍕", "🍕", "🍕", "🍕", "🍕", "🍕"]
THIRST = ["💧", "💧", "💧", "💧", "💧", "💧", "💧", "💧", "💧", "💧", "💧",]
GAME = True
CARROT = "🥕"
TALK = ["Hey you! Listen up. You gotta keep me alive by feeding me, protecting me from bad people and diseases. This is your first day so I don't blame you. But if I die, it's all on your shoulders. Check my stats and do whatever you need to.",
""]
DAY = 1
# Colors :)
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'

RESET = '\033[0m'

# Clear
def clear():
  os.system('cls')

# Stats
class Status:
  def Health():
    print(f"{RED}Health: {HEALTH}")
  
  def Disease():
    print(f"{YELLOW}Disease: {DISEASE}")
  
  def Hunger():
    sys.stdout.write(f"{GREEN}Hunger: ")
    print(*HUNGER)

  def Thirst():
    sys.stdout.write(f"{BLUE}Thirst: ")
    print(f"*THIRST {RESET}")

# Game
while GAME:
  clear()
  print(f"{CARROT} - {TALK[DAY-1]}\n")
  Status.Health()
  Status.Disease()
  Status.Hunger()
  Status.Thirst()

  print("""
    <1> Feed meh food
    <2> Feed meh water
    <3> Protec meh from disease
  """)

  choice = input("* ")
  if choice == "1" and HUNGER != ["🍕", "🍕p", "🍕", "🍕", "🍕", "🍕"]:
    print()
  else:
    print("Bruh, plez pay 'ttention to ma stats :|")
  
  if choice == "2" and THIRST != ["💧", "💧", "💧", "💧", "💧", "💧", "💧", "💧", "💧", "💧", "💧",]:
    print()
  else:
    print("Bruh, plez pay 'ttention to ma stats :|")

  if choice == "3" and DISEASE != False:
    print()
  else:
    print("Bruh, plez pay 'ttention to ma stats :|")
  
  # some other stuff ig

  DAY += 1
  # stats change somehow
  break
