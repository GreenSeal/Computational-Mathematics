import numpy as np


class EQUATIONS:
    def __init__(self):
        self.start = 0.0
        self.finish = 1.0
        self.h = 0.1
        self.a1 = self.k(0)
        self.b1 = 0
        self.a2 = self.k(1)
        self.b2 = 1

    def k(self, x):
        return np.exp(x)

    def q(self, x):
        return 1 + x*x*x

    def f(self, x):
        return np.exp(-x)


def fill_A():
    for i in range(11):
        if i == 0:
            A[0, 0] = eq.b1 - eq.a1 / eq.h
            A[0, 1] = eq.a1 / eq.h
            d[0] = 0
        elif i == 10:
            A[i, i - 1] = -eq.a2 / eq.h
            A[i, i] = - eq.b2 - eq.a2 / eq.h
            d[10] = 0
        else:
            A[i, i - 1] = eq.k(i / 10.0 - 0.5 * eq.h)
            A[i, i + 1] = eq.k(i / 10.0 + 0.5 * eq.h)
            A[i, i] = -(A[i, i - 1] + A[i, i + 1] + eq.h * eq.h * eq.q(i / 10.0))
            d[i] = -eq.h * eq.h * eq.f(i / 10.0)


def sweep_method(d):
    # straight stroke
    P = np.zeros(11)
    Q = np.zeros(11)
    u = np.zeros(11)
    for i in range(11):
        if i == 0:
            P[0] = -A[0, 1]/A[0, 0]
            Q[0] = d[0]/A[0, 0]
        else:
            P[i] = A[i-1, i]/(-A[i-1, i-1] - A[i-1, i-2]*P[i-1])
            Q[i] = (A[i-1, i-2]*Q[i-1] - d[i-1])/(-A[i-1, i-1] - A[i-1, i-2]*P[i-1])

    # return stroke
    i = 10
    while i >= 0:
        if i == 10:
            u[10] = (A[i, i-1]*Q[10] - d[10])/(-A[10, 10] - A[10, 9]*P[10])
        elif i == 0:
            u[0] = P[0]*u[1] - Q[0]
        else:
            u[i] = A[i, i+1]/(-A[i, i] - A[i, i-1]*P[i])*u[i+1] + (A[i, i-1]*Q[i] - d[i])/(-A[i, i] - A[i, i-1]*P[i])

        i -= 1

    return u


eq = EQUATIONS()
A = np.zeros((11, 11))
d = np.zeros(11)
fill_A()

u = sweep_method(d)

eps = sweep_method(d - np.dot(A, u))
while any(eps_i > 0.0001 for eps_i in eps):
    u = u + eps
    eps = sweep_method(d - np.dot(A, u))

print("u =", u)



