"""
This program uses the euler method to solve
differential equations of the first order.
It uses numpy and matplotlib to streamline 
calculations and to visualize the finished graph.

Author: Reymond T
Version: 1.0
Since: 2023-05-05
"""
import numpy as np
from matplotlib import pyplot as plt


# ***************Functions*********************
# Euler's method
def euler(f, x0, y0, x_end, n):
    dx = (x_end - x0) / n

    x = np.linspace(x0, x_end, n + 1)
    y = np.zeros(n + 1)
    
    y[0] = y0

    for i in range(1, n + 1):
        y[i] = y[i - 1] + f(x[i - 1], y[i - 1]) * dx

    return x, y


# **************Main program**********************
# Input differential equation
print("Enter a first order ODE:")
_f = input("dy/dx = ")


# Defines the differential equation based on input
def f(x, y):
    return eval(_f)


print("Enter initial conditions:")
x0 = float(input("x0 = "))
y0 = float(input("y0 = "))

print("Enter calculation point: ")
x_end = float(input("xn = "))

print("Enter number of steps:")
n = int(input("Number of steps = "))

# Euler method call
x, y = euler(f, x0, y0, x_end, n)

plt.subplot(2, 1, 1)
plt.plot(x, y, "o")
plt.plot(x, y)
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Approximate Solution with Forward Euler’s Method")
plt.show()
