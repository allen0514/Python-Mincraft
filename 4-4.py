# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:45:26 2020

@author: appedu
"""
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    mc.executeCommand("time add 30")
    time.sleep(0.05)