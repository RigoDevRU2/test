from drawnow import drawnow
import matplotlib.pyplot as plt
import numpy as np

# plt.ion() ## Note this correction
#fig=plt.figure()

plt.ion()  # enable interactivity
fig = plt.figure()  # make a figure
plt.axis([0,1000,0,1])
x = list()
y = list()

def make_fig():
    plt.scatter(x, y)  # I think you meant this

def runPlot():
    i=0 
    for i in range(1000):
        temp_y = np.random.random()
        x.append(i)
        y.append(temp_y)  # or any arbitrary update to your figure's data
        i += 1
        drawnow(make_fig)

runPlot()

