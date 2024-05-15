import math
import numpy as np


def main(t, h, f, k):
    ans = [f.copy()]
    n = math.ceil(t / h)
    for index in range(n):
        f +=  np.dot(h * k,  f)  
        ans.append(list(f.copy()))
    return ans

n = int(input("Введите количесво уравнений "))

h = float(input("Введите длину шага "))
t = float(input('Введите длительнсь процесса '))

f = np.zeros(n)

for i in range(n):
    f[i] = float(input(f"Введите начальное значение для f_{i} "))

k = np.zeros((n, n))
for i in range(n):
    
    for j in range(n):
        k[i][j] = float(input(f"Введите значение для k_{i}_{j} "))


ans = main(t, h, f, k)
print(ans)