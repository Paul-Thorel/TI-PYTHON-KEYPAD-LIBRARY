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

  if key[0]==keylist[0]:
    if key[1]==keylist[1]:
      if key[2]==keylist[2]:
        return True 
  return False 







"""use like this :
g=getkey()
if ispressed("up",g): #if up key is pressed
  #do if pressed




"""
