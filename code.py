import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(1,100,50)
plt.xlim(-5,5)
plt.ylim(-5,5)
x_values = [4, 3] 
y_values = [4, 5] 
plt. plot(x_values, y_values)
x_values = [3, -1] 
y_values = [5, -1] 
plt. plot(x_values, y_values)
x_values = [-1, 4] 
y_values = [-1, 4] 
plt. plot(x_values, y_values)
plt.title('Right Angle Triangle')
plt.grid() 
plt.show()
