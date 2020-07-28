# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:20:34 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z,35)
mc.setBlock(x+1,y,z,35)
mc.setBlock(x+2,y,z,35)
mc.setBlock(x+2,y,z+2,35)
mc.setBlock(x,y,z+1,35)
mc.setBlock(x,y,z+2,35)
mc.setBlock(x+1,y,z+2,35)
mc.setBlock(x+2,y,z+1,35)