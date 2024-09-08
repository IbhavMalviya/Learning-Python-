from random import choice   
import matplotlib.pyplot as plt
import time


class RandomWalk:
    def __init__(self,num_points=5000):
        self.num_points=num_points
        
        self.xv=[0]
        self.yv=[0]
        
    def fill_walk(self):
        while len(self.xv) <self.num_points:
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction * x_distance
            
            y_direction=choice([1,-1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_direction * y_distance
            
            if x_step == 0 and y_step==0:
                continue
            
            x=self.xv[-1]+x_step
            y=self.yv[-1]+y_step
            
            self.xv.append(x)
            self.yv.append(y)
            
rw=RandomWalk()

rw.fill_walk()
plt.style.use('classic')
fig,ax=plt.subplots()
ax.scatter(rw.xv,rw.yv,s=15)
ax.set_aspect('equal')
plt.show()
plt.savefig('randomwalk.png')
time.sleep(0.2)
    
  
