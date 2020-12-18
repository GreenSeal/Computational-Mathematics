from math import fabs

res = open("TomashevDenis_CompMathLab3Res.txt", "w")

# Newton

polinom = {4, -12, 3, -5}
polinom_diff = {0, 12, -24, 3}
x_0 = 2.5
x_prev = x_0
x = x_prev - (4*x_prev**3 - 12*x_prev**2 + 3*x_prev - 5)/(12*x_prev**2 - 24*x_prev + 3)
x_true = 2.8901454
i = 0
while fabs(x - x_prev) > 0.0000001:
    x_prev = x
    x = x_prev - (4*x_prev**3 - 12*x_prev**2 + 3*x_prev - 5)/(12*x_prev**2 - 24*x_prev + 3)
    i = i+1
    print(x)
res.write("\nIter_num:\n" + str(i))
