#!/usr/bin/env python3
x = float(input("Enter a value of X : "))
n = term = num = 1
result = 1.0
while n <= 100:
    term *= x / n
    result += term
    n += 1
    if term < 0.0001:
        break
print("No of Times= {} and sum= {}".format(n,result))
