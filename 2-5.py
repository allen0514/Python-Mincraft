# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:41:26 2020

@author: appedu
"""


mc = Minecraft.create()


while True:
    x,y,z = player.getTilePos()
    mc.setBlocks(x-1,y,z-1,x+1,y,z+1,8)
     time.sleep(10)
     