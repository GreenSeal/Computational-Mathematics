import numpy as np
import matplotlib.pyplot as plt


def f(t_n, x_n, y_n):
    return [y_n, x_n*x_n - 1]


def method_runge_kutta(t_n, x_n, y_n):
    k1 = f(t_n, x_n, y_n)
    k2 = f(t_n + C[1]*H_RK,
           x_n + A[1][0]*H_RK*k1[0],
           y_n + A[1][0]*H_RK*k1[1])
    k3 = f(t_n + C[2]*H_RK,
           x_n + H_RK*(A[2][0]*k1[0] + A[2][1]*k2[0]),
           y_n + H_RK*(A[2][0]*k1[1] + A[2][1]*k2[1]))
    k4 = f(t_n + C[3]*H_RK,
           x_n + H_RK*(A[3][0]*k1[0] + A[3][1]*k2[0] + A[3][2]*k3[0]),
           y_n + H_RK*(A[3][0]*k1[1] + A[3][1]*k2[1] + A[3][2]*k3[1]))
    u_next = [x_n + H_RK*(B[0]*k1[0] + B[1]*k2[0] + B[2]*k3[0] + B[3]*k4[0]),
              y_n + H_RK*(B[0]*k1[1] + B[1]*k2[1] + B[2]*k3[1] + B[3]*k4[1])]
    return u_next


def build_graph(start_points, point_x, point_y):
    file = plt.figure(figsize=[12, 8])

    for i in range(len(start_points)):
        x = np.zeros(1)
        y = np.zeros(1)
        x[0] = start_points[i][0]
        y[0] = start_points[i][1]
        j = 0
        while abs(x[j] - point_x) < 2.0 and abs(y[j] - point_y) < 2.0:
            vec = method_runge_kutta(0, x[j], y[j])
            x = np.append(x, vec[0])
            y = np.append(y, vec[1])
            j = j + 1
            if j > 6000:
                break

        plt.plot(x, y)
        plt.tight_layout()

    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Фазовые траектории точки (" + str(point_x) + ", " + str(point_y) + ")")
    file.savefig('Точка_(' + str(point_x) + ", " + str(point_y) + ").png")
    plt.show()
    return


A = np.array([[0, 0, 0, 0],
              [0.5, 0, 0, 0],
              [0, 0.5, 0, 0],
              [0, 0, 1, 0]])

B = np.array([1/6, 1/3, 1/3, 1/6])
C = np.array([0, 0.5, 0.5, 1])

START_POINTS_1 = np.array([[-0.3, 1.3], [1.9, -1.3], [-0.6, 1.3], [1.9, -1.0],
                         [0.0, 1.3], [0.0, 1.7], [1.8, -1.4], [1.8, -1.6]])

START_POINTS_2 = np.array([[-1.05, 0.05], [-1.15, 0.15], [-1.1, 0.1], [-1.2, 0.2]])

H_RK = 0.001

build_graph(START_POINTS_1, 1.0, 0.0)
build_graph(START_POINTS_2, -1.0, 0.0)
