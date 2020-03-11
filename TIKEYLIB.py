from sys import *

def getkey(n=3):
  return list(stdin.readline(n))

def ispressed(key="up",keylist=[]):
  if key=="enter":
    key=" [F"
  if key=="up":
    key=" [A"
  if key=="down":
    key=" [B"
  if key=="right":
    key=" [C"
  if key=="left":
    key=" [D"
  if key=="annul":
    key=" [2"
  press=True
  for i in range(3):
    if key[i]==keylist[i]:
      press=True
    else:
      press=False
  return press


"""use like this :
g=getkey()
if ispressed("up",g): #if up key is pressed
  #do if pressed




"""
