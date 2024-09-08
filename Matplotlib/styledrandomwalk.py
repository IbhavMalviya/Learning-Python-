from random import choice   
import matplotlib.pyplot as plt
import time


class RandomWalk:
    def __init__(self,num_points=50000):
        self.num_points=num_points
        
        self.xv=[0]
        self.yv=[0]
        
    def fill_walk(self):
        while len(self.xv) <self.num_points:
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4,5,6,7,8])
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
fig,ax=plt.subplots(figsize=(10,6),dpi=128)
point_numbers=range(rw.num_points)
ax.scatter(rw.xv,rw.yv,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
ax.set_aspect('equal')
ax.scatter(0,0,c='green',edgecolors='none',s=50)
ax.scatter(rw.xv[-1],rw.yv[-1],c='red',edgecolors='none',s=50)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()
plt.savefig('randomwalk.png')

  
