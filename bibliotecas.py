import math as m

print("3^2 = ",m.pow(m.ceil(2.2),m.floor(2.2)),"\n")

import numpy as np
a = np.array([1,2,3])
b = a
c = np.array([5,6,7])

print(np.dot(np.dot(a,b),c)) #(1*1+2*2+3*3)*(5+6+7)

matriz_a = np.array([[1,2,3],
                     [5,2,5]])
matriz_b = np.array([[2,2],
                     [1,1],
                     [2,3]])


print(f"\n\nAs matrizes A({matriz_a}) e B({matriz_b}) multiplicadas resultam em \n\n{matriz_a @ matriz_b}")
matriz_c = np.full((3,2),5)
print(f"\n{matriz_c}")