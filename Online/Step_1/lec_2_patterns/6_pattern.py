"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

'''
for(i=1;i<=n;i++) 
{
for(j=1;j<=n-i-1;j++)
{
cout << j << " ";
}
cout << endl;
}
'''

def pattern(n):
    for i in range(n):
        for j in range(i, n):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the numeber : "))
    pattern(n)