'''

import matplotlib.pyplot as plt
import numpy as np
plt.ion() ## Note this correction
fig=plt.figure()
plt.axis([0,1000,0,1])

i=0

while i <1000:
    temp_y=np.random.random();
    #x.append(i);
    #y.append(temp_y);
    plt.scatter(i,temp_y);
    i+=1;
    plt.show()
    plt.pause(0.0001) #Note this correction
'''
import numpy as np
import matplotlib.pyplot as plt
from drawnow import drawnow

plt.ion()  # enable interactivity
fig = plt.figure()  # make a figure
x = list()
y = list()

def make_fig():
    plt.scatter(x, y)  # I think you meant this

def runPlot():
    for i in range(1000):
        temp_y = np.random.random()
        x.append(i)
        y.append(temp_y)  # or any arbitrary update to your figure's data
        i += 1
        drawnow(make_fig)

runPlot()

