m = [[1,2,3],
     [2,3,3],
     [5,4,3]]
# Solucao 1
m_rotated=[[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
print(m_rotated)
# Solucao 2
print(list(list(x) for x in zip(*m))[::-1])
# Solucao 3
print([[x[i] for x in m] for i in range(len(m))][::-1])
# Solucao 4
r = []
i = 0
for row in m:
  listToAdd = [item[i] for item in m]
  r.append(listToAdd)
  i +=1
print(r[::-1])
# Solucao 5 - usando numpy
import numpy as np
np_m=np.array(m)
print(np.rot90(np_m))