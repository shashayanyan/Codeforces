"""
You are given two arrays of integers a1,a2,…,an
 and b1,b2,…,bn
. It is guaranteed that each integer from 1
 to 2⋅n
 appears in exactly one of the arrays.

You need to perform a certain number of operations (possibly zero) so that both of the following conditions are satisfied:

For each 1≤i<n
, it holds that ai<ai+1
 and bi<bi+1
.
For each 1≤i≤n
, it holds that ai<bi
.
During each operation, you can perform exactly one of the following three actions:

Choose an index 1≤i<n
 and swap the values ai
 and ai+1
.
Choose an index 1≤i<n
 and swap the values bi
 and bi+1
.
Choose an index 1≤i≤n
 and swap the values ai
 and bi
.
You do not need to minimize the number of operations, but the total number must not exceed 1709
. Find any sequence of operations that satisfies both conditions.

Input
Each test consists of multiple test cases. The first line contains a single integer t
 (1≤t≤100
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n
 (1≤n≤40
) — the length of the arrays a
 and b
.

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤2⋅n
).

The third line of each test case contains n
 integers b1,b2,…,bn
 (1≤bi≤2⋅n
).

It is guaranteed that each integer from 1
 to 2⋅n
 appears either in array a
 or in array b
.

Output
For each test case, output the sequence of operations.

In the first line for each test case, output the number of operations k
. Note that 0≤k≤1709
.

In the following k
 lines for each test case, output the operations themselves:

If you want to swap the values ai
 and ai+1
, output two integers 1
 and i
. Note that 1≤i<n
.
If you want to swap the values bi
 and bi+1
, output two integers 2
 and i
. Note that 1≤i<n
.
If you want to swap the values ai
 and bi
, output two integers 3
 and i
. Note that 1≤i≤n
.
It can be shown that under the given constraints, a solution always exists.
"""

if __name__ == "__main__":
    m = int(input())
    for i in range(m):
        # inputs
        n= int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        operations = []
        # sorting like bubble sort
        for j in range(n):
            for k in range(1, n):
                if a[k-1] > a[k] :
                    # swap 
                    tmp = a[k]
                    a[k] = a[k-1]
                    a[k-1] = tmp
                    # add op
                    operations.append([1, k])


        for j in range(n):
            for k in range(1, n):
                if b[k-1] > b[k]:
                    # swap
                    tmp = b[k]
                    b[k] = b[k-1]
                    b[k-1] = tmp
                    # add op
                    operations.append([2, k])

        for j in range(n):
            if a[j] > b[j]:
                operations.append([3, j+1])

        print(len(operations))
        for x in operations:
            print(x[0], x[1])