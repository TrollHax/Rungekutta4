import numpy as np
from matplotlib import pyplot as plt

#***************FUNCTION DEFINITIONS*****************
# Euler method
def euler(f,x0,y0,x_end,n):
    
  dx = (x_end-x0)/n

  x = np.linspace(x0, x_end, n + 1)
  y = np.zeros(n + 1)
  
  y[0] = y0
  
  for i in range(1, n + 1):
    y[i] = y[i-1] + f(x[i-1], y[i-1]) * dx

  return x, y


  
#****************MAIN PROGRAM*********************
  
# Inputs
print('Enter a first order ODE:')
_f = input('dy/dx = ')
def f(x,y):
  return eval(_f)

print('Enter initial conditions:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter calculation point: ')
x_end = float(input('xn = '))

print('Enter number of steps:')
n = int(input('Number of steps = '))


# Euler method call
x, y = euler(f,x0,y0,x_end,n)


# Print solution as list and graph
print('\n-----------SOLUTION-----------')
print('------------------------------')    
print('x\t\ty\t\tslope')
print('------------------------------')

for i in range(n+1):
  print(round(x[i],2),' \t', round(y[i],2),' \t', round(f(x[i],y[i]),2))
  print('------------------------------')

#DEBUG
print()
print(x)
print(y)
#/DEBUG

plt.plot(x ,y , 'o')
plt.xlabel('Value of x')
plt.ylabel('Value of y')
plt.title('Approximate Solution with Forward Euler’s Method')
plt.show()