#!/bin/python3
# prime.py
# To print the prime numbers.

def factor(number):
    factor = 0
    for i in range(1, number+1):
        if number % i == 0:
            factor += 1
    
    return factor

def prime(x):
    fact = factor(x)
    if fact == 2:
        print(x)


if __name__ == "__main__":
    print("Enter an integer value till which you want your prime numbers to displayed:")
    N = int(input())

    for i in range(2, N+1):
        prime(i)
    
