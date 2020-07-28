# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:45:04 2020

@author: appedu
"""
import random,time
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

while True:
    color = random.randrange(0,16)
    
    time.sleep(1)