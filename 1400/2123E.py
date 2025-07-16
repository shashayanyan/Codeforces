"""
Define the MEX
 (minimum excluded value) of an array to be the smallest nonnegative integer not present in the array. For example,

MEX([2,2,1])=0
 because 0
 is not in the array.
MEX([3,1,0,1])=2
 because 0
 and 1
 are in the array but 2
 is not.
MEX([0,3,1,2])=4
 because 0
, 1
, 2
, and 3
 are in the array but 4
 is not.
You are given an array a
 of size n
 of nonnegative integers.

For all k
 (0≤k≤n
), count the number of possible values of MEX(a)
 after removing exactly k
 values from a
.

Input
The first line contains an integer t
 (1≤t≤104
)  — the number of test cases.

The first line of each test case contains one integer n
 (1≤n≤2⋅105
) — the size of the array a
.

The second line of each test case contains n
 integers, a1,a2,…,an
 (0≤ai≤n
).

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output a single line containing n+1
 integers — the number of possible values of MEX(a)
 after removing exactly k
 values, for k=0,1,…,n
.
"""
if __name__ == "__main__":
    m =  int(input())
    for testcase in range(m):
        n = int(input())
        a = list(map(int, input().split()))
        