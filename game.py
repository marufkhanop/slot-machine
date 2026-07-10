import random as rn
BALANCE = 0

def main():
  global BALANCE
  print("-------------------")
  get_diposit()
  game_loop = 0
  while True:
    if BALANCE < 1:
      break
    if game_loop != 0:
      stop = input("Type 'y' to play and q to quit (y/q): ")
      if stop == "y":
        pass
      elif stop == "q":
        break
      else:
        print(f"{stop} is not an option")
        game_loop += 1
        continue
    start_game()
    game_loop += 1
  print(f"You left with ${BALANCE}")
  print("---------")
  

def start_game():
  line = get_line()
  print("-------------------")
  bet = get_bet()
  print()
  print("---------")
  first, second, third = display_spin()
  score_logic(line, bet, first, second, third)
  print("---------")
  print(f"Your current balance ${BALANCE}")
  
def get_diposit():
  global BALANCE
  while True:
    balance = input("Diposit: $")
    if balance.isdigit():
      balance = int(balance)
      if 0 < balance:
        BALANCE = BALANCE + balance
        break
      else:
        print("Invalid balance")
    else:
      print("Invalid balance")
      
def get_line():
  while True:
    try:
      count = int(input("Lines? (1,2 or 3) "))
      if 1 <= count <= 3:
        return count
      else:
        print("invalid line")
    except ValueError:
      print("invalied line")
      
def get_bet():
  global BALANCE
  while True:
    try:
      count = int(input("Bet ammount? $"))
      if 0 < count <= BALANCE:
        BALANCE = BALANCE - count
        return count
      else:
        print(f"invalid bet,your balance is {BALANCE}")
    except ValueError:
      print("invalied bet")

def display_spin():
  st = ["A","B","C"]
  nd = ["A","B","C"]
  rd = ["A","B","C"]
  rn.shuffle(st)
  rn.shuffle(nd)
  rn.shuffle(rd)
  print(f"{st[0]} | {nd[0]} | {rd[0]}")
  print(f"{st[1]} | {nd[1]} | {rd[1]}")
  print(f"{st[2]} | {nd[2]} | {rd[2]}")
  first = False
  second = False
  third = False
  if st[0]==nd[0]==rd[0]:
    first = True
  if st[1]==nd[1]==rd[1]:
    second = True
  if st[2]==nd[2]==rd[2]:
    third = True
  return first,  second, third

def score_logic(line, bet, first, second, third):
  global BALANCE
  if line == 1:
    if first:
      BALANCE = BALANCE + (bet*4)
  elif line == 2:
    if first or second:
      BALANCE = BALANCE + (bet*3)
  elif line == 3:
    if first or second or third:
      BALANCE = BALANCE + (bet*2)
  else:
    pass
    
    
if __name__ =="__main__":
  main()
