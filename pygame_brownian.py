from brownian.robot import Robot
from brownian.simulate_engine import Simulate
from brownian.visualize import Visualize


def main():
    #defining the display size and robot properties
    height=1000
    width=1000
    arena_height=300
    arena_width=300
    fps=60
    radius=15
    shape="circle"
    #Robot(robot.x,robot.y,robot.radius,robot.color,robot.shape)
    robot=Robot(arena_height/2,arena_width/2,radius,(255,0,0),shape)
    sim=Simulate(robot,arena_height,arena_width)
    vis=Visualize(sim,robot,width,height,fps)
    vis.run()
if __name__=="__main__":
    main()


