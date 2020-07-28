# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from mcpi.minecraft import minecraft 
mc.minecraft.create()
x,y,z = mc.player. getTilePos()
mc.setBlocks(x-25,y-1,z-25,x+25,y-1,z+25,57)
