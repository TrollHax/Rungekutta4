"""
This program uses the forward euler- and rungekutta 4 method 
to solve differential equations of the first order.
It uses numpy and matplotlib to streamline calculations 
and to visualize the finished graph for easy comparison.

Author: Reymond T
Version: 1.5
Since: 2023-05-05
"""
import os
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


# Rungekutta 4 method
def rung4(f, x0, y0, x_end, n):
    dx = (x_end - x0) / n

    x = np.linspace(x0, x_end, n + 1)
    y = np.zeros(n + 1)

    y[0] = y0

    for i in range(1, n + 1):
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + (dx / 2), y[i - 1] + k1 * (dx / 2))
        k3 = f(x[i - 1] + (dx / 2), y[i - 1] + k2 * (dx / 2))
        k4 = f(x[i - 1] + dx, y[i - 1] + k3 * dx)

        avgK = 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

        y[i] = y[i - 1] + avgK * dx

    return x, y


# **************Main program**********************

# Clear terminal
os.system("cls")

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

# Print solution as list
print("\nApproximate solution with forward euler's method:")
print("------------------------------")
print("x\t\ty")
print("------------------------------")
print(round(x[-1], 2), "\t\t", round(y[-1], 2))

# Plot solution (Euler)
plt.subplot(121)
#Don't plot if dataset larger than 100 points to reduce lag
if (x.size <= 100):
    plt.plot(x, y, "o")
plt.plot(x, y)
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Forward Euler’s Method")

# Rungekutta 4 method call
x, y = rung4(f, x0, y0, x_end, n)

# Print solution as list
print("\nApproximate solution with rungekutta 4:")
print("------------------------------")
print("x\t\ty")
print("------------------------------")
print(round(x[-1], 2), "\t\t", round(y[-1], 2))

plt.subplot(122)
#Don't plot if dataset larger than 100 points to reduce lag
if (x.size <= 100):
    plt.plot(x, y, "o")
plt.plot(x, y)
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Rungekutta 4 Method")
plt.show()
