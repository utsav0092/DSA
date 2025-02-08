# Explanation and Examples of Hash Data Structure in Python

# --- What is a Hash Data Structure? ---
# A hash data structure stores data in key-value pairs.
# It uses a hash function to map keys to specific "buckets" in memory, allowing fast access.

# --- Examples of Hash in Python ---

# 1. Using `dict` (Dictionary)
# A dictionary is a hash table where you can associate a key with a value.
hash_table = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing elements
print(hash_table["name"])  # Output: Alice

# Adding an element
hash_table["job"] = "Engineer"

# Removing an element
del hash_table["age"]

print(hash_table)  # Output: {'name': 'Alice', 'city': 'New York', 'job': 'Engineer'}

# 2. Using `set`
# A set is like a dictionary but only stores keys (no values). It ensures all elements are unique.
hash_set = {1, 2, 3, 4}

# Adding elements
hash_set.add(5)

# Removing elements
hash_set.remove(3)

print(hash_set)  # Output: {1, 2, 4, 5}

# --- Key Features of Hash in Python ---
# 1. Fast Access: Constant-time operations for lookups and insertions.
# 2. Unique Keys: Dictionary keys must be unique.
# 3. Hash Function: Used to map keys to buckets.
# 4. Mutable: Can add, update, or remove key-value pairs.

# --- Applications of Hash in Python ---

# 1. Frequency Counting
# Count the occurrences of elements using a dictionary.
arr = [1, 2, 2, 3, 3, 3]
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print(freq)  # Output: {1: 1, 2: 2, 3: 3}

# 2. Checking Duplicates
# Use a set to check for duplicates.
arr = [1, 2, 3, 4, 2]
unique = set(arr)
print(len(unique) < len(arr))  # Output: True (because 2 is duplicate)

# 3. Mapping Data
# Store and retrieve data using keys.
phone_book = {"Alice": "1234", "Bob": "5678"}
print(phone_book["Alice"])  # Output: 1234

# --- Advantages of Hash DS ---
# 1. Fast Operations: Average case time complexity for lookups, insertions, and deletions is O(1).
# 2. Dynamic Sizing: Python dictionaries resize automatically as needed.
# 3. Flexible Keys: Keys can be of any immutable type (e.g., strings, numbers, tuples).

# --- Limitations of Hash DS ---
# 1. Collision: Two keys may hash to the same bucket, requiring resolution (handled internally in Python).
# 2. Unordered: Dictionaries were unordered before Python 3.7; now, they maintain insertion order.
# 3. Memory Overhead: May use extra memory to maintain speed.

# --- Example Code: Frequency Counting using Class-Based Approach ---
class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        # Find the size of the array (N)
        n = len(arr)

        # Create a frequency array initialized to 0 for indices 1 to N
        freq = [0] * (n + 1)  # Use n+1 to include index n

        # Count frequencies of elements in the given range (1 to N)
        for num in arr:
            if 1 <= num <= n:  # Only count if the number is within range 1 to N
                freq[num] += 1

        # Replace the elements in the original array with their frequencies
        for i in range(n):
            arr[i] = freq[i + 1]  # Use indices 1 to N from the frequency array

# Example Usage
arr = [2, 3, 2, 3, 5]
solution = Solution()
solution.frequencyCount(arr)
print("Updated array with frequencies:", arr)  # Output: [2, 2, 0, 0, 1]

'''--------------------------------------------------------------------------------------------------'''

# What are the hashable and what are not ?
'''
Hashables (Immutables)

1.Strings
2.Integers
3.Tuples {1,2,3,4,5}
-----------------------
Not hashables (Mutables)

1.Array (Dynamic arrays)
2.Dictionaries (they themselves are hashmaps)
'''

"""Hash Sets"""

s = set()
print(s)
#add the items in the set
s.add(1)
s.add(2)
s.add(3)
print(s)
#Lookup if the item in the set - O(1)
if 1 in s:
    print(True)
else:
    print(False)
if 1 not in s:
    print(True)
else:
    print(False)
#remove the items
s.remove(3)
print(s)

string = 'aaaaaaaabbbbbbbbbccccccccccccdddddddddddddd'
sett = set(string) #set contruction - O(s) - s is the length of the string
print(sett)
if 'a' in sett:
    print(True)
# looping over items in set - O(n)
for i in sett:
    print(i, end="")
sett.remove('b')
print()
print(sett)

'''Hashmaps'''

d = {"greg" : 1, "stieve" : 2, "rob" : 3}
print(d)
# add a key-value - O(1)
d["ash"] = 4
print(d)
#checking the items/keys - O(1)
if 'ash' in d:
    print(True)
#Check the value correspoinding to a key in the dictionary - O(1)
print(d["ash"])
if d["greg"] == 1:
    print(True)
# Looping over the key:value pairs of the dictionary - O(n)
for key, value in d.items():
    print(f"Key: '{key}', Value: {value}")

# Defaultdict
from collections import defaultdict
from collections import Counter

# default = defaultdict(int)
default = defaultdict(list)
print(default[2]) # it will return 0
print(default) # defaultdict(int, {2:0}) ``
string = 'aaaaaaaaaabbbbbbbbbbbbbbcccccccddddd'
counter = Counter(string)
print(counter)