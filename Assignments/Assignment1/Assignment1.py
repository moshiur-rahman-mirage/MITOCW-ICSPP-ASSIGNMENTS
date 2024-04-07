import numpy as np

x=int(input("Please enter a number: "))
y=int(input("Please enter another number :"))
xpowery=x**y

print(str(x)+" to the power "+str(y)+" is : "+str(xpowery))


def log_base_2(n):
    if n <= 0:
        return float('NaN')  # Logarithm is not defined for non-positive numbers

    count = 0
    while n > 1:
        n /= 2
        count += 1

    return count
print(log_base_2(8))



def log_calc(x):
    guess=0
    epsilon=0.1
    increment=0.01
    while abs(2**guess-x)>=epsilon:
        guess+=increment

    if abs(2**guess-x)>=epsilon:
        return "Failed"
    else:
        return guess

print(log_calc(8))


def logPy(x):
    return np.log2(x)

print(logPy(8))