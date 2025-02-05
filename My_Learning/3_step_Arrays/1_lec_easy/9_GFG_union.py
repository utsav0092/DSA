# '''GFG - find the union of two arrays'''

# def Union(nums1, nums2):
#     c = a.union(b)
#     return c

# nums1 = [1, 2, 3, 4, 5]
# nums2 = [4, 5, 6, 7, 8]
# a = set(nums1)
# b = set(nums2)
# print(Union(nums1, nums2))

# '''My solution'''

# def Union(nums1, nums2):
#     temp = []
#     i = 0
#     j = 0
#     n = len(nums1)
#     m = len(nums2)
#     while (i < n and j < m):
#         if (nums1[i] <= nums2[j]):
#             temp.append(nums1[i])
#             i += 1
#         elif (nums1[i] >= nums2[j]):
#             temp.append(nums2[j])
#             j += 1
#     while (i < n):
#         temp.append(nums1[i])
#         i += 1
#     while (j < m):
#         temp.append(nums2[j])
#         j += 1
#     return set(temp)

# nums1 = [1, 2, 3, 4, 5]
# nums2 = [1, 2, 3]
# new = Union(nums1, nums2)
# print(new)

# '''TUF solution'''

# def Union(l1, l2):
#     s = set()
#     union = []
#     for i in l1:
#         s.add(i)
#     for i in l2:
#         s.add(i)
#     for i in s:
#         union.append(i)
#     return union

# l1 = [1,2,3,4,5]
# l2 = [1,2,3,4,5,6,7,8]
# print(Union(l1, l2))

'''AI solution'''

# def value(l1, l2):
#     combined = l1 + l2
#     neg = []
#     pos = []
#     for i in combined:
#         if combined[i] < 0:
#             neg.append(combined[i])
#     for j in combined:
#         if combined[j] >= 0:
#             pos.append(combined[j])
#     neg = list(set(neg))
#     pos = list(set(pos))
#     new = (neg + pos)
#     return new

# l1 = [1, 2, 3, 4, 5, -1, -2]
# l2 = [1, 2, 3, 4, 5, 6, 7, 8, -1, -3]
# print(value(l1, l2))

def union_sorted_arrays(a, b):
    i, j = 0, 0
    result = []
    
    while i < len(a) and j < len(b):
        # If current element of a[] is smaller than current element of b[]
        if a[i] < b[j]:
            if len(result) == 0 or a[i] != result[-1]:
                result.append(a[i])
            i += 1
        # If current element of b[] is smaller than current element of a[]
        elif a[i] > b[j]:
            if len(result) == 0 or b[j] != result[-1]:
                result.append(b[j])
            j += 1
        else:
            # If a[i] == b[j], add any one of them and move both pointers
            if len(result) == 0 or a[i] != result[-1]:
                result.append(a[i])
            i += 1
            j += 1

    # Include remaining elements of a[]
    while i < len(a):
        if len(result) == 0 or a[i] != result[-1]:
            result.append(a[i])
        i += 1

    # Include remaining elements of b[]
    while j < len(b):
        if len(result) == 0 or b[j] != result[-1]:
            result.append(b[j])
        j += 1

    return result

# Example usage:
a = [1, 2, 2, 3]
b = [2, 3, 4, 4, 5]
print(union_sorted_arrays(a, b))  # Output: [1, 2, 3, 4, 5]
