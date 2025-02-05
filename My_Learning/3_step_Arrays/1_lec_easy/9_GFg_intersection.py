'''GFG - Intersection of two sorted arrays'''
'''Time Complexity: O(n*m) and Space Complexity: O(n2)'''

def Intersection(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    # vis = [0]*m
    res = []
    for i in range(n):
        for j in range(m):
            # if (nums1[i] == nums2[j] and vis[j] == 0):
            if (nums1[i] == nums2[j]):
                res.append(nums1[i])
                # vis[j] = 1
                break
    return res

nums1 = [1,2,3,4,5]
nums2 = [1,1,3,3,6]
print(Intersection(nums1, nums2))

'''Optimsed solution'''
'''TC - O(n1+n2) and SC - O(1)'''

def Intersection(arr1, arr2):
    i = 0
    j = 0
    ans = []
    while (i < len(arr1) and j < len(arr2)):
        if (arr1[i] < arr2[j]):
            i += 1
        elif (arr1[i] > arr2[j]):
            j += 1
        else:
            ans.append(arr1[i])
            i += 1
            j += 1
    return ans

nums1 = [1,2,3,4,5]
nums2 = [1,1,3,3,6]
print(Intersection(nums1, nums2))

'''Using set()'''

def Intersection(arr1, arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)
    res = arr1.intersection(arr2)
    res = list(res)
    return res
    # ------------
    res = set()
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            res.add(arr1[i])
        else:
            continue
    return res

arr1 = [1,2,3,4,5]
arr2 = [2,3,4,5,6]
print(Intersection(arr1, arr2))