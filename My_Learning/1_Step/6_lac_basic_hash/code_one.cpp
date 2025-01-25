//Store the duplicate numbers in hash table
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);  // Use vector for dynamic array
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Determine the maximum value in the array for hash table size
    int maxValue = *max_element(arr.begin(), arr.end());

    // Precompute
    vector<int> hash(maxValue + 1, 0);  // Hash table sized dynamically
    for (int i = 0; i < n; i++) {
        hash[arr[i]] += 1;
    }

    int q;
    cin >> q;
    while (q--) {
        int number;
        cin >> number;

        // Fetch result from hash table
        if (number >= 0 && number <= maxValue) {
            cout << hash[number] << endl;
        } else {
            cout << 0 << endl;  // If number is out of hash table bounds
        }
    }
    return 0;
}