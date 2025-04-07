import numpy as np
import pygame
from .robot import Robot


class Simulate:
    def __init__(self,robot,arena_height,arena_width):
        self.arena_height = arena_height
        self.arena_width = arena_width

        self.robot = robot
        self.rotate=False
        self.rotating_time=0
        self.rotating_time_max = 1
    def move(self,dt):
        if not self.rotate:
            
            self.robot.update_position(dt)
            self.rotate = self.check_collision()
        else:
            
            if self.rotating_time<=0:
                self.rotate=False
            else:
                self.rotating_time-=dt
                self.robot.rotate(dt)
            
        

    def check_collision(self):
        #if the robot collides at left wall
        if self.robot.x < self.robot.radius:
            self.robot.x=self.robot.radius
            self.robot.angle=(np.pi)/2 #after that rotate clockwise
            self.rotating_time=np.random.uniform(0.1,self.rotating_time_max)
           
            return True
        #if the robot collides at right wall
        if self.robot.x + self.robot.radius>self.arena_width:
            self.robot.x = self.arena_width - self.robot.radius
            self.robot.angle=(3/2)*(np.pi) #after that rotate clockwise
            self.rotating_time=np.random.uniform(0.1,self.rotating_time_max)
            
            return True
        #if robot collides at lower wall
        if self.robot.y < self.robot.radius:
            self.robot.y = self.robot.radius
            self.robot.angle=np.pi
            self.rotating_time=np.random.uniform(0.1,self.rotating_time_max)
            #self.robot.rotate()
            return True

        #if the robot collides at lower wall
        if self.robot.y +self.robot.radius>self.arena_height:
            self.robot.y=self.arena_height-self.robot.radius
            self.robot.angle=0
            self.rotating_time=np.random.uniform(0.1,self.rotating_time_max)

           
            return True

    




        

        
        


    

    


