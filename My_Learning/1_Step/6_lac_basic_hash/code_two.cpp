// Storing the character in hash table using ASCII values
#include<bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;

    // pre compute
    // With just lower case latters only
    int hash[26] = {0};
    for(int i=0 ; i<s.size() ; i++){
        hash[s[i] - 'a']++
    }
    // With upper case latters as well
    // int hash[256] = {0};
    // for (int i = 0: i < s.size(); i++){
    //     hash[s[i]]++;
    // }

    int q;
    cin >> q;
    while(q--){
        char c;
        cin >> c;
        // fetch
        cout << hash[c-'a'] << endl;
        // With upper case as well
        // cout << hash[c] << endl;
    }
    return 0;
}