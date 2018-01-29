#!/bin/python3
# Problem : TO find the mean, median, mode of the given array elements.
# by: Himanshu Shekhar

import sys
import math

# To calculate the Mean of the array.
def Mean(Array):
    sum = 0
    N = len(Array)
    for x in range(N):
        sum += Array[x]

    m = sum / N

    return (m)

# To calculate Median of the given array
def Median(Array):
    N = len(Array)
    Array.sort()
    #print(Array)
    mid = int(N / 2)
    if N % 2 == 0:
        m = (Array[mid] + Array[mid - 1]) / 2
    else:
        m = (Array[mid])

    return (m)


# To calculate the Mode of the given array

def Mode(Array):
    N = len(Array)
    num = Array[0]
    mode = num
    count = 1
    countMode = 1

    for i in range(1, N):
        if Array[i] == num:
            count += 1
        else:
            if count > countMode:
                countMode = count
                mode = num
            
            count = 1
            num = Array[i]

    print("Mode :", mode)
    


if __name__ == "__main__":
    print("Enter the number of array elements:")
    N = int(input())

    arr = [int(x) for x in input().split(' ')]

    mean = Mean(arr)
    print ("Mean :", mean)
    median = Median(arr)
    print("Median :", median)
    Mode(arr)