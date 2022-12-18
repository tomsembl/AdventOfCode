import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def visualize(size,voxels):

    # # list of voxels

    # # create a figure and axes
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')

    # # create a list of Poly3DCollection objects representing the voxels
    # voxel_collections = []
    # for voxel in voxels:
    #     # create a cube centered at the voxel coordinates with side length 1
    #     x, y, z = voxel
    #     verts = [[x - 0.5, y - 0.5, z - 0.5],
    #             [x - 0.5, y - 0.5, z + 0.5],
    #             [x - 0.5, y + 0.5, z + 0.5],
    #             [x- 0.5, y + 0.5, z - 0.5],
    #             [x + 0.5, y - 0.5, z - 0.5],
    #             [x + 0.5, y - 0.5, z + 0.5],
    #             [x + 0.5, y + 0.5, z + 0.5],
    #             [x + 0.5, y + 0.5, z - 0.5]]
    #     # specify the order in which the vertices should be connected
    #     faces = [[0, 1, 2, 3],  # bottom face
    #             [4, 5, 6, 7],  # top face
    #             [0, 4, 7, 3],  # left face
    #             [1, 5, 6, 2],  # right face
    #             [0, 1, 5, 4],  # front face
    #             [3, 2, 6, 7]]  # back face
    #     voxel_collections.append(Poly3DCollection([verts], facecolors='b', edgecolors='k', linewidths=[1], alpha=1))

    # # add the voxel collections to the plot
    # for collection in voxel_collections:
    #     ax.add_collection(collection)

    # # set the plot limits to fit the voxels
    # ax.set_xlim(min(voxels)[0] - 0.5, max(voxels)[0] + 0.5)
    # ax.set_ylim(min(voxels)[1] - 0.5, max(voxels)[1] + 0.5)
    # ax.set_zlim(min(voxels)[2] - 0.5, max(voxels)[2] + 0.5)

    # plt.show()



    # list of voxels
    #voxels = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]

    # extract x, y, and z coordinates from the voxels list
    xs = [x[0] for x in voxels]
    ys = [x[1] for x in voxels]
    zs = [x[2] for x in voxels]

    # create a 3D scatter plot
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(xs, ys, zs)
    plt.show()


