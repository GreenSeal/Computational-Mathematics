import numpy as np
import matplotlib.pyplot as plt


class EQUATION:
    def __init__(self):
        self.a = 2.0
        self.b = 0.0015
        self.g = 5.0
        self.tetta0 = 3.0
        self.phi0 = 0.0525
        self.C = 5.0
        self.k1 = 0.05
        self.k2 = 0.35


class BUTCHER_TABLE:
    def __init__(self):
        self.a = np.array([[0.25, 0.0],
                           [0.25, 0.25]])

        self.b = np.array([0.5, 0.5])
        self.c = np.array([0.5, 0.5])
        self.H_RK = 0.001


def f(u_n):
    return np.array([EQ.a*u_n[0]*u_n[0]/(u_n[0]+EQ.tetta0) - EQ.k1*u_n[0] - EQ.g*u_n[0]*u_n[1],
            EQ.b*u_n[0]*(1 - u_n[1]/EQ.C)*(1 + (u_n[1]/EQ.phi0)**2) - EQ.k2*u_n[1]])


def jakob_matrix_f(u_n):
    jakob_matrix = np.zeros((2, 2))
    jakob_matrix[0, 0] = EQ.a*(u_n[0]**2 + 2*u_n[0]*EQ.tetta0)/(u_n[0] + EQ.tetta0)**2 - EQ.k1 - EQ.g*u_n[1]
    jakob_matrix[0, 1] = -EQ.g*u_n[0]
    jakob_matrix[1, 0] = EQ.b*(1-u_n[1]/EQ.C)*(1+(u_n[0]/EQ.phi0)**2)
    jakob_matrix[1, 1] = -1/EQ.C - 3*u_n[1]**2/(EQ.C*EQ.phi0**2) + 2*u_n[1]/(EQ.phi0**2)*EQ.b*u_n[0] - EQ.k2
    return jakob_matrix


# Работает только если сжимающее!
def MSI_k1(k1_0):
    print("k1_0 = ", k1_0)
    k1_n = f(k1_0 + BT.H_RK*BT.a[0, 0]*k1_0)
    for i in range(50):
        k1_n = f(k1_n + BT.H_RK*BT.a[0, 0]*k1_n)
        print("k1_n = ", k1_n)

    return k1_n


def MSI_k2(k2_0, k1):
    k2_n = f(k2_0 + BT.H_RK*BT.a[1, 0]*k1 + BT.a[1, 1]*BT.H_RK*k2_0)
    for i in range(50):
        k2_n = f(k2_n + BT.H_RK*BT.a[1, 0]*k1 + BT.H_RK*BT.a[1, 1]*k2_n)

    return k2_n


def newton_method_k1(k1_0, u_n):
    a = np.linalg.inv(np.identity(2) - BT.H_RK * BT.a[0, 0] * jakob_matrix_f(k1_0))
    k1_n = a.dot(f(k1_0))
    for i in range(50):
        k1_n = k1_n - a.dot(k1_n - f(u_n + BT.H_RK * BT.a[0, 0] * k1_n))

    # print("k1=", k1_n)
    return k1_n


def newton_method_k2(k2_0, u_n):
    a = np.linalg.inv(np.identity(2) - BT.H_RK * BT.a[1, 1] * jakob_matrix_f(k2_0))
    k2_n = a.dot(f(k2_0))
    for i in range(50):
        k2_n = k2_n - a.dot(k2_n - f(u_n + BT.H_RK * BT.a[1, 1] * k2_n))

    # print("k2=", k2_n)
    return k2_n


def method_runge_kutta(u_n):

    k1 = newton_method_k1(u_n, u_n)
    k2 = newton_method_k2(u_n + BT.H_RK*BT.a[1, 0]*k1, u_n)
    u_next = [u_n[0] + BT.H_RK*(BT.b[0]*k1[0] + BT.b[1]*k2[0]),
              u_n[1] + BT.H_RK*(BT.b[0]*k1[1] + BT.b[1]*k2[1])]
    return u_next


def build_graph(start_points, point_x, point_y):
    file = plt.figure(figsize=[12, 8])

    for i in range(len(start_points)):
        x, y = np.zeros(1), np.zeros(1)
        x[0], y[0] = start_points[i][0], start_points[i][1]
        j = 0
        while 1:
            vec = method_runge_kutta(np.array([x[j], y[j]]))
            x, y = np.append(x, vec[0]), np.append(y, vec[1])
            j = j + 1
            if j > 10000:
                break

        plt.plot(x, y)
        plt.tight_layout()

    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Фазовые траектории")
    file.savefig("График_" + str(graph_num) + ".png")
    plt.show()
    return


EQ = EQUATION()
BT = BUTCHER_TABLE()
graph_num = 0

START_POINTS_1 = np.array([#[-0.3, 1.3],
                           [0.5, -1.5],
#                           [-0.6, 1.3],
                           [0.5, -0.1],
                           [0.5, -0.5],
#                           [-0.1, 1.7],
#                           [1.2, -1.4],
                           [0.5, -2.5]])

START_POINTS_2 = np.array([[-2.5, 1],
                           [-2.5, 2],
                           [-2.5, 1.5],
                           [-2.5, 0.5]
                           ])


build_graph(START_POINTS_1, 1.0, 0.0)
graph_num += 1
build_graph(START_POINTS_2, -1.0, 0.0)
