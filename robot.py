import numpy as np
import pygame
import sys

class Robot:
    def __init__(self,x,y,radius,color,shape):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.shape = shape
        self.angle = np.random.uniform(0,2 * np.pi) #for generating the random angle
        
        self.speed= 100
        self.angular_speed=5

    def update_position(self,dt):

        self.x += np.cos(self.angle) * self.speed * dt
        self.y += np.sin(self.angle) * self.speed * dt


    def get_position(self):
        return (self.x,self.y)

    def rotate(self,dt):
        self.angle -= self.angular_speed * dt
    




    

    

