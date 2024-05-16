import math
import numpy as np

class Solver:
    """!  Класс реализующий паттерн шаблонный функции 
    @param n количесво уравлнений
    @param t время
    @param f начальные условие
    @param h шаг
    @param k матрица значний уравнений
    """
    n = None 
    t = None 
    f = None 
    h = None 
    k = None  


    def __init__(self):
        """!  Функции инициализации """
        self.read()
        ans = self.solve()
        self.print(ans)

    def read(self):
        """!  Функции чтения """
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
        """!  Функции решение системы
        @return 2 мерный масив ответов
        """
        n = math.ceil(self.t / self.h)
        ans = np.zeros((n + 1, self.n))
        ans[0] = self.f.copy()
        for index in range(n):
            ans[index + 1] = ans[index] + np.dot(self.h * self.k,  ans[index])
        return ans.tolist()
    
    def print(self, ans):
        """!  Функции выводва данных
        @param ans расчитанные данные
        """
        print(ans)


Solver()