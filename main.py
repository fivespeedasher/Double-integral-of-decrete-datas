#_*_ coding:gb2312_*_
from typing import ChainMap
from scipy.interpolate import Rbf
import matplotlib.pyplot as plt
from scipy.interpolate import RectBivariateSpline
import numpy as np
# TODO 改成xlsx或者SQL中读取
# Decrete Datas
x = [   1,1,1,1,1,
        2,2,2,2,2,
        3,3,3,3,3,
        4,4,4,4,4]
y = [   1,2,3,4,5,
        1,2,3,4,5,
        1,2,3,4,5,
        1,2,3,4,5]
H = [   13.73,25.8,8.47,25.27,22.32,
        15.47,21.33,14.49,24.83,26.19,
        23.28,26.48,29.14,12.04,14.58,
        19.95,23.73,15.35,18.01,16.29]


# Interpolation the H(x,y)
def spline_interpolation(x, y, z):
    """
    Parameter:
        x,y -> np.array,1-D : should be coordinate in strictly ascending order.
        z -> np.array,2-D,shape==(x.size,y.size)
    """
    spline = RectBivariateSpline(x, y, z,bbox=[x[0], x[-1], y[0], y[-1]])
    
    # plot
    plt.subplot(1, 1, 1)
    x_edges = np.linspace(1, 4, 90)
    y_edges = np.linspace(1, 5, 120)
    X_edges, Y_edges = np.meshgrid(x_edges, y_edges)
    X,Y = np.meshgrid(x,y)
    ZI = spline(x_edges, y_edges)
    lims = dict(cmap='Blues', vmin=5, vmax=35)
    plt.pcolormesh(X_edges, Y_edges, ZI.T, shading='flat', **lims)
    plt.scatter(X,Y, 100, z.T, edgecolor='w', lw=0.2, **lims)
    plt.title('RBF interpolation - multiquadrics')
    plt.xlim(0, 5)
    plt.ylim(0, 6)
    plt.colorbar()
    plt.show()
    return spline


if __name__ == "__main__":
    x_axis = np.arange(1,5).flatten()
    y_axis = np.arange(1,6).flatten()
    h_2d = np.array(H).reshape(4,5)
    assert(h_2d.shape == (x_axis.size,y_axis.size))
    spline = spline_interpolation(x_axis,y_axis,h_2d)
    