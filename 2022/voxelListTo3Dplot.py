import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def visualize(voxels): #list of lists eg. [[1,2,3],[4,5,6],[7,8,9]]

    xs = [x[0] for x in voxels]
    ys = [x[1] for x in voxels]
    zs = [x[2] for x in voxels]

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(xs, ys, zs)
    plt.show()


