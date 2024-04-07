from math import sqrt

# x=int(input("Please enter a number: "))
# y=int(input("Please enter another number :"))
# xpowery=x**y
#
# print(str(x)+" to the power "+str(y)+" is : "+str(xpowery))
#

def log_base_2(n):
    if n <= 0:
        return float('NaN')  # Logarithm is not defined for non-positive numbers

    count = 0
    while n > 1:
        n /= 2
        count += 1

    return count
print(log_base_2(8))


# cube = 27
# #cube = 8120601
# #cube = 10000
# epsilon = 0.1
# guess = 0.0
# increment = 0.01
# num_guesses = 0
# # look for close enough answer and make sure
# # didn't accidentally skip the close enough bound
# while abs(guess**3 - cube) >= epsilon and guess <= cube:
#    guess += increment
#    num_guesses += 1
# print('num_guesses =', num_guesses)
# if abs(guess**3 - cube) >= epsilon:
#    print('Failed on cube root of', cube, "with these parameters.")
# else:
#    print(guess, 'is close to the cube root of', cube)



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