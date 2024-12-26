""" 
# funkcija collatz
@param num: int === paran broj
  ? true   stampa i deli num sa 2
  : false  stampa i mnozi num sa 3 i dodaje 1
@return rez: int 
"""

def collatz(num):
  if num % 2 == 0:      # ? Da li je paran broj 
    rez = int(num/2)
    print(rez)
    return rez
  else:
    rez = int(3 * num + 1)
    print(rez)
    return rez

print("Enter number: ")
broj = input()

try:
  while broj!=1:                # ? da li je broj == 1
    broj = collatz(int(broj))   # * poziva funkciju collatz
except Exception:               # ! Niste uneli ceo broj
  print('Unesite ceo broj !!!') # * prekida izvrsavanje programa