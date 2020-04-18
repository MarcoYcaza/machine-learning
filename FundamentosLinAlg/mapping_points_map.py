import matplotlib.pyplot as plt
import numpy as np
from numpy import save

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

points_storage=[]

def onclick(event):
    
    
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))
    plt.plot(event.xdata, event.ydata, 'o',markersize=5)

    fig.canvas.draw()
    points_storage.append([event.xdata, event.ydata])

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

acumulado =np.asarray(points_storage)

np.save('puntos.npy', acumulado)

print(acumulado)


# load numpy array from npy file
#from numpy import load
# load array
#data = load('data.npy')
# print the array
#print(data)
# load numpy array from npy file
#from numpy import load
# load array
#data = load('data.npy')
# print the array
#print(data)
