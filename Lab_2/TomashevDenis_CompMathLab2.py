import numpy as np

res = open("TomashevDenis_CompMathLab2Res.txt", "w")
# fill A
a = np.zeros((100, 100), dtype=np.double)
for i in range(0, 100):
    for j in range(0, 100):
        if i == j:
            a[i][j] = 100
        elif (j - i) < 2:
            a[i][j] = (i+1)/(j+1)

# fill f
f = np.zeros((100, 1))
for i in range(100):
    f[i][0] = i+1

a_inv = np.linalg.inv(a)
res.write("Condition number = " + str(np.linalg.det(a_inv)*np.linalg.det(a)))
res.write("\nЛmax = " + str(max(np.linalg.eigvals(a))) + "  Лmin = " + str(min(np.linalg.eigvals(a))))
a_st = a
f_st = f

# Gauss method

# straight stroke
for k in range(0, 100):
    n = np.zeros((100, 100), dtype=np.double)
    for i in range(k, 100):
        n[i][k] = -a[i][k] / a[k][k]
    for i in range(0, 100):
        n[i][i] = 1
    a = np.dot(n, a)
    f = np.dot(n, f)

# return stroke
u = np.zeros((100, 1))
for i in range(0, 100):
    u[99-i] = f[99-i]
    for j in range(100-i, 100):
        u[99-i] = u[99-i] - a[99-i][j]*u[j]
    u[99-i] = u[99-i]/a[99-i][99-i]
res.write("\nUgauss:\n" + str(u))
# res.write(f_st)
# res.write(a_st)
res.write("\nThe discrepancy on Gauss:\n" + str(f_st - np.dot(a_st, u)))

# Seidel method

l, d, r = np.zeros((100, 100)), np.zeros((100, 100)), np.zeros((100, 100))
for i in range(100):
    for j in range(100):
        if i > j:
            l[i][j] = a_st[i][j]
        elif i == j:
            d[i][j] = a_st[i][j]
        elif i < j:
            r[i][j] = a_st[i][j]

u_prev = np.zeros((100, 1))
b = -np.dot(np.linalg.inv(l+d), r)
f = np.dot(np.linalg.inv(l+d), f_st)
u = np.dot(b, u_prev) + f
e = 10**(-7)

while np.linalg.norm(u - u_prev) > e:
    u_prev = u
    u = np.dot(b, u_prev) + f
res.write("\nUsei:\n" + str(u))
res.write("\nThe discrepancy on Seidel:\n" + str(f_st - np.dot(a_st, u_prev)))
res.close()
