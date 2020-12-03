import numpy as np
Q=np.array([[0.894427191,-0.4472135955],[0.4472135955,0.894427191]])
R=np.array([[1.1180339887,0.894427191],[0,0.6708203932]])
result=Q@R
print(result)
