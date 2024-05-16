import math
import numpy as np

class Solver:
    n = None 
    t = None 
    f = None 
    h = None 
    k = None  


    def __init__(self):
        self.read()
        ans = self.solve()
        self.print(ans)

    def read(self):
        self.n = int(input("Введите количесво уравнений "))
        self.h = float(input("Введите длину шага "))
        self.t = float(input('Введите длительнсь процесса '))
        self.f = np.zeros(self.n)
        for i in range(self.n):
            self.f[i] = float(input(f"Введите начальное значение для f_{i} "))
        self.k = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                self.k[i][j] = float(input(f"Введите значение для k_{i}_{j} "))
        

    def solve(self):
        n = math.ceil(self.t / self.h)
        ans = np.zeros((n + 1, self.n))
        ans[0] = self.f.copy()
        for index in range(n):
            ans[index + 1] = ans[index] + np.dot(self.h * self.k,  ans[index])
        return ans.tolist()
    
    def print(self, ans):
        print(ans)


Solver()