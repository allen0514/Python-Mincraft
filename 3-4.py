# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:55:29 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random, time
pos = mc.player.getTilePos()
while True:
    x=pos.x+random.uniform(-10,0)
    y=pos.y+0
    z=pos.z+random.uniform(-20,20)
    mc.spawnEntity(x,y,z,12)
    time. sleep(0.1)
    