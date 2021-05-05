import numpy as np
import matplotlib.pyplot as plt


def y(x):
    return (1-eps*np.log(np.exp(1/eps)-1)) - eps*np.log(1/(np.exp(1/eps) - 1) + x)


NET_SIZE = 500000
h = 1/NET_SIZE
eps = 0.15
yN = 0

print("h = ", h)
y_prev = np.zeros(NET_SIZE)
y_next = np.zeros(NET_SIZE)
y_prev[0] = 1.0
y_next[0] = 1.0

while eps != 0.07:
    file = plt.figure(figsize=[6, 4])
    a0 = 0
    y_prev[1] = (h)*a0 + 1.0
    y_next[1] = (h)*(a0+h) + 1.0
    for i in range(2, NET_SIZE):
        # if i == 1001 or i == NET_SIZE - 10:
        #       y_prev[i] = 101*100*((y_prev[i-1] - y_prev[i-2])**2)/eps + 101*y_prev[i-1] - 100*y_prev[i-2]
        #       y_next[i] = 101*100*((y_next[i-1] - y_next[i-2])**2)/eps + 101*y_next[i-1] - 100*y_next[i-2]
        # else:
        y_prev[i] = ((y_prev[i-1] - y_prev[i-2])**2)/eps + 2*y_prev[i-1] - y_prev[i-2]
        y_next[i] = ((y_next[i-1] - y_next[i-2])**2)/eps + 2*y_next[i-1] - y_next[i-2]
    print("yN_prev =", y_prev[NET_SIZE-1])
    print("yN_next =", y_next[NET_SIZE-1])


    a = a0 - y_prev[NET_SIZE-1]*h/(y_next[NET_SIZE-1] - y_prev[NET_SIZE-1])
    while abs(y_prev[NET_SIZE - 1] - yN) > 0.001:
        y_prev[1] = (h)*a + 1.0
        y_next[1] = (h)*(a + h) + 1.0
        for i in range(2, NET_SIZE):
            # if i == 251 or i == NET_SIZE - 1:
            #     y_prev[i] = 101*100*((y_prev[i-1] - y_prev[i-2])**2)/eps + 101*y_prev[i-1] - 100*y_prev[i-2]
            #     y_next[i] = 101*100*((y_next[i-1] - y_next[i-2])**2)/eps + 101*y_next[i-1] - 100*y_next[i-2]
            # else:
            y_prev[i] = ((y_prev[i-1] - y_prev[i-2])**2)/eps + 2*y_prev[i-1] - y_prev[i-2]
            y_next[i] = ((y_next[i-1] - y_next[i-2])**2)/eps + 2*y_next[i-1] - y_next[i-2]
            #print("yn=", y_prev[i])
        print("a = ", a)
        print("yN_prev =", y_prev[NET_SIZE - 1])
        print("yN_next =", y_next[NET_SIZE - 1])
        a = a - y_prev[NET_SIZE-1]*h/(y_next[NET_SIZE-1] - y_prev[NET_SIZE-1])

    print("yN = ", y_prev[NET_SIZE-1])

    x_band = np.linspace(0, 1, NET_SIZE)
    y_arr = np.array([y(x) for x in x_band])
    plt.plot(x_band, y_prev-y_arr)
    plt.tight_layout()


    #plt.plot(x_band, [y(x) for x in x_band])
    #plt.tight_layout()
    plt.title("Ошибка при eps = " + str(eps))
    plt.grid()
    file.savefig("Ошибка при eps = " + str(eps) + ".png")
    plt.show()
    eps -= 0.01




