# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:00:48 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
def Tree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,57)
    mc.setBlocks(x,y,z,x,y+4,z+1,17)
Tree(x,y,z)
for i in range(10):
   for j in range(10):
       for k in range(5):
           Tree(x+i*5,y+j*i,z+k*i)
           time.sleep(0.5)