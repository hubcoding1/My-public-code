#boter kaas en eieren
import random
from os import system
from time import sleep
W = 0
G = 0
V = 0
S = 0
def board():
   board = [[a,b,c],
            [d,e,f],
            [g,h,i]]
   for k in board:
       for j in k:
         print(j, end = "  ")
       print()    
system('cls')
while True:
  system('cls')
  print('W [',W,'], G [',G,'], V [',V,']')
  print('')
  def WinCheck():
    if a == b == c or a == d == g:
      print('Winnaar =',a)
      if a == 'X':
        S = 1
        return(S)
      if a == 'O':
        S = 2
        return(S)
    elif g == h == i or i == f == c:
      print('Winnaar =', i)
      if i == 'X':
        S = 1
        return(S)
      if i == 'O':
        S = 2
        return(S)
    elif a == e == i or b == e == h or c == e == g or d == e == f:
      print('Winnaar =', e)
      if e == 'X':
        S = 1
        return(S)
      if e == 'O':
        S = 2
        return(S)
  BList = [1,2,3,4,5,6,7,8,9]
  a = '1'
  b = '2'
  c = '3'
  d = '4'
  e = '5'
  f = '6'
  g = '7'
  h = '8'
  i = '9'
  board()
  #1e zet van player
  while True:
    try:
      PM1 = int(input('Kies een plek: '))
      break
    except ValueError:
      print('Ongeldig')
  if PM1 == 1:
    a = 'X'
  elif PM1 == 2:
    b = 'X'
  elif PM1 == 3:
    c = 'X'
  elif PM1 == 4:
    d = 'X'
  elif PM1 == 5:
    e = 'X'
  elif PM1 == 6:
    f = 'X'
  elif PM1 == 7:
    g = 'X'
  elif PM1 == 8:
    h = 'X'
  elif PM1 == 9:
    i = 'X'
  else:
     print('Ongeldige invoer')
     continue
  S = WinCheck()
  if a == 'X':
    S = 1
  if a == 'O':
    S = 2
  #1e zet van bot
  while True:
    BM1 = random.choice(BList)
    if BM1 == PM1:
      continue
    else:
      break
  if BM1 == 1:
    a = 'O'
  elif BM1 == 2:
    b = 'O'
  elif BM1 == 3:
    c = 'O'
  elif BM1 == 4:
    d = 'O'
  elif BM1 == 5:
    e = 'O'
  elif BM1 == 6:
    f = 'O'
  elif BM1 == 7:
    g = 'O'
  elif BM1 == 8:
    h = 'O'
  elif BM1 == 9:
    i = 'O'
  S = WinCheck()
  if S == 1:
    W += 1
    continue
  elif S == 2:
    V += 1
    continue
  print('W [',W,'], G [',G,'], V [',V,']')
  print('')
  system('cls')
  board()
  #2e zet van speler
  while True:
    try:
      while True:
        PM2 = int(input('Kies een plek: '))
        if PM2 == PM1 or PM2 == BM1:
          print('Dat kan niet')
          continue
        else:
          break
      break
    except ValueError:
      print('Ongeldig')
  if PM2 == 1:
    a = 'X'
  elif PM2 == 2:
    b = 'X'
  elif PM2 == 3:
    c = 'X'
  elif PM2 == 4:
    d = 'X'
  elif PM2 == 5:
    e = 'X'
  elif PM2 == 6:
    f = 'X'
  elif PM2 == 7:
    g = 'X'
  elif PM2 == 8:
    h = 'X'
  elif PM2 == 9:
    i = 'X'
  else:
     print('Ongeldige invoer')
     continue
  S = WinCheck()
  if S == 1:
    W += 1
    continue
  elif S == 2:
    V += 1
    continue
  #2e zet van bot
  while True:
    BM2 = random.choice(BList)
    if BM2 == PM1 or BM2 == BM1 or BM2 == PM2:
      continue
    else:
      break
  if BM2 == 1:
    a = 'O'
  elif BM2 == 2:
    b = 'O'
  elif BM2 == 3:
    c = 'O'
  elif BM2 == 4:
    d = 'O'
  elif BM2 == 5:
    e = 'O'
  elif BM2 == 6:
    f = 'O'
  elif BM2 == 7:
    g = 'O'
  elif BM2 == 8:
    h = 'O'
  elif BM2 == 9:
    i = 'O'
  S = WinCheck()
  if S == 1:
    W += 1
    continue
  elif S == 2:
    V += 1
    continue
  print('W [',W,'], G [',G,'], V [',V,']')
  print('')
  system('cls')
  board()
  #3e zet van speler
  while True:
    try:
      while True:
        PM3 = int(input('Kies een plek: '))
        if PM3 == PM1 or PM3 == BM1 or PM3 == PM2 or PM3 == BM2:
          print('Dat kan niet')
          continue
        else:
          break
      break
    except ValueError:
      print('Ongeldig')
  if PM3 == 1:
    a = 'X'
  elif PM3 == 2:
    b = 'X'
  elif PM3 == 3:
    c = 'X'
  elif PM3 == 4:
    d = 'X'
  elif PM3 == 5:
    e = 'X'
  elif PM3 == 6:
    f = 'X'
  elif PM3 == 7:
    g = 'X'
  elif PM3 == 8:
    h = 'X'
  elif PM3 == 9:
    i = 'X'
  else:
     print('Ongeldige invoer')
     continue
  S = WinCheck()
  if S == 1:
    W += 1
    continue
  elif S == 2:
    V += 1
    continue
  #3e zet van bot
  while True:
    BM3 = random.choice(BList)
    if BM3 == PM1 or BM3 == BM1 or BM3 == PM2 or BM3 == BM2 or BM3 == PM3:
      continue
    else:
      break
  if BM3 == 1:
    a = 'O'
  elif BM3 == 2:
    b = 'O'
  elif BM3 == 3:
    c = 'O'
  elif BM3 == 4:
    d = 'O'
  elif BM3 == 5:
    e = 'O'
  elif BM3 == 6:
    f = 'O'
  elif BM3 == 7:
    g = 'O'
  elif BM3 == 8:
    h = 'O'
  elif BM3 == 9:
    i = 'O'
  S = WinCheck()
  if S == 1:
    W += 1
    continue
  elif S == 2:
    V += 1
    continue
  print('W [',W,'], G [',G,'], V [',V,']')
  print('')
  system('cls')
  board()
  #4e zet speler
  while True:
    try:
      while True:
        PM4 = int(input('Kies een plek: '))
        if PM4 == PM1 or PM4 == BM1 or PM4 == PM2 or PM4 == BM2 or PM4 == PM3 or PM4 == BM3:
          print('Dat kan niet')
          continue
        else:
          break
      break
    except ValueError:
      print('Ongeldig')
  if PM4 == 1:
    a = 'X'
  elif PM4 == 2:
    b = 'X'
  elif PM4 == 3:
    c = 'X'
  elif PM4 == 4:
    d = 'X'
  elif PM4 == 5:
    e = 'X'
  elif PM4 == 6:
    f = 'X'
  elif PM4 == 7:
    g = 'X'
  elif PM4 == 8:
    h = 'X'
  elif PM4 == 9:
    i = 'X'
  else:
     print('Ongeldige invoer')
     continue
  S = WinCheck()
  if S == 1:
    W += 1
    continue
  elif S == 2:
    V += 1
    continue
  #4e bot move
  while True:
    BM4 = random.choice(BList)
    if BM4 == PM1 or BM4 == BM1 or BM4 == PM2 or BM4 == BM2 or BM4 == PM3 or BM4 == BM3 or BM4 == PM4:
      continue
    else:
      break
  if BM4 == 1:
    a = 'O'
  elif BM4 == 2:
    b = 'O'
  elif BM4 == 3:
    c = 'O'
  elif BM4 == 4:
    d = 'O'
  elif BM4 == 5:
    e = 'O'
  elif BM4 == 6:
    f = 'O'
  elif BM4 == 7:
    g = 'O'
  elif BM4 == 8:
    h = 'O'
  elif BM4 == 9:
    i = 'O'
  S = WinCheck()
  if S == 1:
    W += 1
    continue
  elif S == 2:
    V += 1
    continue
  print('W [',W,'], G [',G,'], V [',V,']')
  print('')
  system('cls')
  board()
  #5e player move
  while True:
    try:
      while True:
        PM5 = int(input('Kies een plek: '))
        if PM5 == PM1 or PM5 == BM1 or PM5 == PM2 or PM5 == BM2 or PM5 == PM3 or PM5 == BM3 or PM5 == PM4 or PM5 == BM4:
          print('Dat kan niet')
          continue
        else:
          break
      break
    except ValueError:
      print('Ongeldig')
  if PM5 == 1:
    a = 'X'
  elif PM5 == 2:
    b = 'X'
  elif PM5 == 3:
    c = 'X'
  elif PM5 == 4:
    d = 'X'
  elif PM5 == 5:
    e = 'X'
  elif PM5 == 6:
    f = 'X'
  elif PM5 == 7:
    g = 'X'
  elif PM5 == 8:
    h = 'X'
  elif PM5 == 9:
    i = 'X'
  else:
     print('Ongeldige invoer')
     continue
  S = WinCheck()
  if S == 1:
    W += 1
    continue
  elif S == 2:
    V += 1
    continue
  print('Gelijkspel!')
  G += 1