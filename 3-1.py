# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:54:40 2020

@author: appedu
"""

while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y ,hit.p

        blockID = mc.getBlock(x,y,z)
        print('恭喜獵到ID為'+str(blockID)+'的方塊')
        mc.postToChat('恭喜獵到ID為'+str(blockID)+'的方塊')