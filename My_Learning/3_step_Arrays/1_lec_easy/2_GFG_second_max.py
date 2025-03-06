'''Find the second max element in array with sort'''
'''TC = O(nlogn) and SC = O(n)'''

def Smax(arr):
    arr.sort()
    return arr[-2]

arr = list(map(int, input().split()))
print(f"Element is: {Smax(arr)}")

'''without sort'''
'''TC = O(2n) and SC = O(n)'''

def Smax(arr):
    large = arr[0]
    slarge = -1
    for i in range(len(arr)):
        if (arr[i] > large):
            large = arr[i]
    for i in range(len(arr)):
        if (arr[i] > slarge and arr[i] != large):
            slarge = arr[i]
    return slarge

arr = list(map(int, input("Enter your values: ").split()))
print(f"Number: {Smax(arr)}")

'''Optimised TC = O(n) and SC = O(n)'''

def Smax(arr):
    large = arr[0]
    slarge = -1
    for i in range(len(arr)):
        if (arr[i] > large):
            slarge = large
            large = arr[i]
        elif (arr[i] < large and arr[i] > slarge):
            slarge = arr[i]
    return slarge

arr = list(map(int, input("Enter your values: ").split()))
print(f"Smax: {Smax(arr)}")

'''Find the second min element in array with sort'''
'''TC = O(n) and SC = O(n)'''

def Smin(arr):
    Small = arr[0]
    SSmall = 1000
    for i in range(len(arr)):
        if (arr[i] < Small):
            Small = arr[i]
        elif (arr[i] > Small and arr[i] < SSmall):
            SSmall = arr[i]
    return SSmall  
  
arr = list(map(int, input("Enter your values: ").split()))
print(f"Smin: {Smin(arr)}")