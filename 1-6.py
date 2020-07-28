# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:02:41 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z,103)