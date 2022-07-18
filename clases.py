# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 20:47:44 2021

@author: Caroline
"""

class circle(object):
    
    def _init_ (self, radius, color):
        
        self.radius = radius;
        self.color = color;
        
    def drawCircle(self):
        pass
    
RedCircle = circle(3, 'Red')

RedCircle.drawCircle()

