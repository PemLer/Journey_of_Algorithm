import math

n = int(input())

print((math.factorial(2*n) // (math.factorial(n) ** 2)) // (n+1))