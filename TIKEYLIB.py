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

  for i in range(3):
    if key[i]==keylist[i]:
      p=True
    else:
      p=False
  return p







"""use like this :
g=getkey()
if ispressed("up",g): #if up key is pressed
  #do if pressed




"""
