# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 09:25:35 2020

@author: appedu
"""
for i in range(1,4):
mc = Minecraft.create()
line1=[]
line2=[]
line3=[]
for i in range(1,4):
    line1.append(i*1)

    line2.append(i*2)
for i in range(1,4):
    line3.append(i*3)
x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,2,str(line1),str(line2),str(line3))
