import numpy as numpy
import matplotlib.pylab as plot
import math as math
import sys
global gravity
velocity1 = int(input('Enter the 1st initial velocity (m/s) >> '))     #type your 1st velocity
gravity = 9.8       #gravity is 9.8 in physic
angle1 =  math.radians(int(input('Enter the 1st angle of projection (degrees) >> ')))
t1 = ((2*velocity1)*numpy.sin(angle1))/gravity   # Formula to find time
ts1 = t1*numpy.linspace(0,1)  # Time vector
x1 = (velocity1*ts1)*numpy.cos(angle1)  # Formula to find the x position
y1 = (velocity1*ts1)*numpy.sin(angle1) - (gravity/2)*(ts1**2)  # Formula to find y position

velocity2 = int(input('Enter the 2nd initial velocity (m/s) >> '))     #type your 2nd velocity
angle2 = math.radians(int(input('Enter the 2nd angle of projection (degrees) >> ')))

t2 = ((2*velocity2)*numpy.sin(angle2))/gravity   # Formula to find time
ts2 = t2*numpy.linspace(0,1)  # Time vector

x2 = (velocity2*ts2)*numpy.cos(angle2)  # Formula to find the x position
y2 = (velocity2*ts2)*numpy.sin(angle2) - (gravity/2)*(ts2**2)  # Formula to find y position

velocity3 = int(input('Enter the 3rd initial velocity (m/s) >> '))     #type your 3re velocity

angle3 = math.radians(int(input('Enter the 3rd angle of projection (degrees) >> ')))

t3 = ((2*velocity3)*numpy.sin(angle3))/gravity   # Formula to find time
ts3 = t3*numpy.linspace(0,1)  # Time vector

x3 = (velocity3*ts3)*numpy.cos(angle3)  # Formula to find the x position
y3 = (velocity3*ts3)*numpy.sin(angle3) - (gravity/2)*(ts3**2)  # Formula to find y position

#type the title and explanation of what x and y label are
plot.title("PROJECTILE", fontsize=24)
plot.xlabel("HORIZONTAL DISTANCE", fontsize=14)
plot.ylabel("VERTICAL DISTANCE", fontsize=14)

# Create graph using line with label
plot.plot(x1,y1,label='1st Vector')
plot.plot(x2,y2,label='2nd Vector')
plot.plot(x3,y3,label='3rd Vector')

plot.legend()

plot.show() # Show on one graph
sys.exit()

referensi : ajaran dari dzaky dan eris
