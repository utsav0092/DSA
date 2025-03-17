'''Leetcode - Merge two 2D array by summing the values'''

def mergeArray(nums1, nums2):

    # res = {}
    # # Add values from nums1
    # for id, val in nums1 + nums2:
    #     res[id] = res.get(id, 0) + val  # Initialize if not present, else sum
    # # # Add values from nums2
    # # for id, val in nums2:
    # #     res[id] = res.get(id, 0) + val  # Sum values if id already exists
    # # Convert to sorted list
    # return sorted([id, val] for id, val in res.items())

    res = {}
    for id, val in sorted(nums1 + nums2):
        if id not in res:
            res[id] = val
            continue
        res[id] += val
    return list(res.items())

def main():
    nums1 = [[1, 2], [3, 4], [4, 6]]
    nums2 = [[1, 2], [3, 4], [5, 6]]
    
    print(mergeArray(nums1, nums2))

if __name__ == "__main__":
    main()