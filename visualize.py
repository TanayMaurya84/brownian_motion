import numpy as np
import pygame
import sys


class Visualize:
    def __init__(self,simulation,robot,width,height,fps):
        pygame.init()

        self.width=800
        self.height=600
        self.fps=fps
        self.simulation = simulation
        self.robot=robot
        self.boundary_color=(0,0,0)
        self.background_color=(255,255,255)
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Brownian motion")
        self.clock = pygame.time.Clock()

    def sim_to_screen_coordinates(self,sim_x,sim_y):
        scale_x = (self.width-40)/self.simulation.arena_width
        scale_y = (self.height-40)/self.simulation.arena_height

        screen_x = int(20+ sim_x * scale_x)
        screen_y = int(20+ sim_y * scale_y)

        return screen_x,screen_y
    def draw_robot(self):
        sim_x = self.simulation.robot.x
        sim_y = self.simulation.robot.y

        screen_x,screen_y = self.sim_to_screen_coordinates(sim_x,sim_y)
          #pygame.draw.circle(screen,(255,0,0),((int(self.x)),int(self.y)),self.radius) 
        pygame.draw.circle(self.screen,self.robot.color,(screen_x,screen_y),self.robot.radius)
    def draw_arena(self):
        top_left = self.sim_to_screen_coordinates(0,0)
        bottom_right = self.sim_to_screen_coordinates(
            self.simulation.arena_width,self.simulation.arena_height
        )

        arena_rect=pygame.Rect(
            top_left[0],top_left[1],
            bottom_right[0]-top_left[0],
            bottom_right[1]-top_left[1]
        )
        pygame.draw.rect(self.screen,self.boundary_color,arena_rect,2)
    def render(self):
        self.screen.fill(self.background_color)

        self.draw_arena()
        self.draw_robot()

        pygame.display.flip()
    

    def handle_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    return False
        return True
    
    def run(self):
        running=True
        while running:
            running = self.handle_events()
            dt = self.clock.tick(self.fps)/1000.0

            
            self.simulation.move(dt)
            self.render()
        pygame.quit()
        sys.exit()
