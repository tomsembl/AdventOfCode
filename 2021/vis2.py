import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from random import randint
import numpy as np
# Create figure and 3D axis
fig = plt.figure()

# prepare some coordinates
x, y, z = np.indices((8, 8, 8))

# Update function for animation
def update(n):    
    ax = fig.add_subplot(111, projection='3d')
    for _ in range(4):
        a=[]
        for _ in range(3):
            rands = [randint(0,8) for _ in range(2)]
            a+=sorted(rands)
        ax.voxels((x >= a[0]) & (x <= a[1]+1) & (y >= a[2]) & (y <= a[3]+1) & (z >= a[4]) & (z <= a[5]+1), facecolors=[randint(0,10)*0.1 for _ in range(3)]+[0.4], edgecolors=[1,1,1, 0.1])
def init():
    ax = fig.add_subplot(111, projection='3d')
    
# Create animation
#ani = FuncAnimation(fig, update, frames=8, interval=1000, repeat=False)
#ani.save('c:/temp/basic_animation.mp4', fps=2, extra_args=['-vcodec', 'libx264'])
ani = FuncAnimation(fig, update, frames=8, interval=2000, repeat=False, init_func=init)
plt.show()