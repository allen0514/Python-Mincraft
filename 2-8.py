# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:58:42 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
try:
    blockType = int(input("方塊ID"))
    mc.setBlock(x,y,z, blockType)
    
except:
    print("olny nomber.")
