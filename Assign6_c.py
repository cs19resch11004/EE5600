import math 
import numpy as np

# Function to find distance 
def shortest_distance(x1, y1, z1, a, b, c, d):  
      
    d = abs((a * x1 + b * y1 + c * z1 + d))  
    e = (math.sqrt(a * a + b * b + c * c)) 
    return (d/e)
    
# Point
x1 = -2
y1 = 2
z1 = 4

#plane parameters
a = -3
b = 1
c = 2
d = -11
  
# Function call 
d=shortest_distance(x1, y1, z1, a, b, c, d)   
print("The distance between the point and plane using conventional formula is ", d)

#SVD of M matrix
M=np.array([[1,0],[0,1],[3/2,-1/2]])
u, s, vT = np.linalg.svd(M, full_matrices=True)

#pseudo inverse of s i.e s+
smat=np.zeros((3,2))
smat[:2, :3] = np.diag(s)
sinv=np.linalg.pinv(smat)

#Matrix b
b=np.array([[1],[-2],[5]])

#finding least square solution x=vS+U^Tb
uTb=np.matmul(np.transpose(u),b)
sinvuTb=np.matmul(sinv,uTb)
x=np.matmul(np.transpose(vT),sinvuTb)
print("\nx= ",x)

#finding the foot of perpendicular
Q=np.array([[-3],[4],[-1]])+x[0,0]*M[:,[0]]+x[1,0]*M[:,[1]]
print("\nFoot of perpendicular Q is \n", Q)

#finding the distance from point D (-1,2,-4)
d=np.array([[-2],[2],[4]])
distance=np.linalg.norm(Q-d)
print("\nThe distance using the foot of perpendicular is \n",distance)
