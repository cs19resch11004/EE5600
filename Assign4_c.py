import numpy as np
from numpy import matrix as m
import matplotlib.pyplot as plt
from numpy import linalg as LA

#Generating points on an ellipse
def ellipse_gen(a,b):
    len = 100
    theta = np.linspace(0,2*np.pi,len)
    x_ellipse = np.zeros((2,len))
    x_ellipse[0,:] = a*np.cos(theta)
    x_ellipse[1,:] = b*np.sin(theta)
    return x_ellipse

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 50
y = np.linspace(-10,10,len)
V = np.array(([1,0.5],[0.5,1]))
V_1 = np.array(([1,0.5],[0.5,1]))
u = np.array(([0.5,0.5]))
u_1 = np.array(([0,0]))
f = -1
cs = -LA.inv(V)@u
print(cs)
cs_1=-LA.inv(V_1)@u_1


#print(cs_1)
cst = cs[np.newaxis, :].T
cst_1 = cs_1[np.newaxis, :].T
#Eigenvalues and eigenvectors
D_vec,P= LA.eig(V)
D = np.diag(D_vec)
D_vec_1,P_1= LA.eig(V_1)

#Ellipse parameters
a = np.sqrt(8/3)
b = np.sqrt(8/9)
xStandardEllipse = ellipse_gen(b,a)

#Major and Minor Axes
MajorStandard = np.array(([b,0]))
MinorStandard = np.array(([0,a]))

xActualEllipse = P@xStandardEllipse+cst
MajorActual = P@MajorStandard+cst[0]

MinorActual = P@MinorStandard+cst[1]
MajorActual1= P_1@MajorStandard+cst_1[0]
MinorActual1 = P_1@MinorStandard+cst_1[1]

plt.plot(xActualEllipse[0,:],xActualEllipse[1,:],label='Ellipse')

plt.plot(-1/3, -1/3, 'o', color='green');
plt.text(-0.3, -1/3,'  C(-1/3, -1/3)')
plt.plot(MajorActual[0], MajorActual[1], 'o', color='red');
plt.text(MajorActual[0]+0.1, MajorActual[1],'  A(1/3, 1/3)')
plt.plot(MinorActual[0], MinorActual[1], 'o', color='black');
plt.text(MinorActual[0] +0.05, MinorActual[1]-0.1,'  B(-1.48803387, 0.82136721)')
print(MajorActual)
print(MinorActual)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.show()
