import numpy as np
A = np.array([[3,-4],[1,-1]])
n = int(input("Enter the power of Matrix n: ")) 
B=n*A-np.eye(2)*(n-1)  #A^n=nA-(n-1)I
print(B)


