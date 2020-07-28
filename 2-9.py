# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:21:26 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
a=input('abc')
mc.setSign(x,y,z,63,1,a)
