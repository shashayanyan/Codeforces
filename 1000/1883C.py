"""
You are given an array of integers a1,a2,…,an
 and a number k
 (2≤k≤5
). In one operation, you can do the following:

Choose an index 1≤i≤n
,
Set ai=ai+1
.
Find the minimum number of operations needed to make the product of all the numbers in the array a1⋅a2⋅…⋅an
 divisible by k
.

Input
Each test consists of multiple test cases. The first line contains a single integer t
 (1≤t≤104
) — the number of test cases. Then follows the description of the test cases.

The first line of each test case contains two integers n
 and k
 (2≤n≤105
, 2≤k≤5
) — the size of the array a
 and the number k
.

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤10
).

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output the minimum number of operations needed to make the product of all the numbers in the array divisible by k
.
"""
def getFactors(num):
    factors = []
    for i in range(2, num//2 + 1):
        if num % i == 0:
            tmp = num
            k = 0
            while tmp % i == 0:
                k = k+1
                tmp = tmp//i
            factors.append([i,k])
    return factors

def aux(num, prime_fac):
    r = num % prime_fac
    if r == 0:
        return 0
    else:
        return prime_fac - r
    


if __name__ == "__main__":
    testcases = int(input())
    #print(getFactors(testcases))
    for i in range(testcases):
        n, k = map(int, input().split())
        minr = 1000
        scnd_minr = 1000
        a = list(map(int, input().split()))
        for j in range(n):
            r = a[j] % k
            if r == 0:
                minr = r
                break
            elif minr > k - r:
                minr = k - r
        
        if k == 4:
            factors = [[2,2]]
            dp = [[0]]*n
            minrs = []
            for j in range(n):
                if a[j]%4 == 0:
                    scnd_minr = 0
                    break
                for l in range(len(factors)):
                    dp[j][l] = aux(a[j], factors[l][0])
                    minrs.append(dp[j][l])
            
            if minr != 0:
                minrs.sort()
                scnd_minr = minrs[0]+minrs[1]
            
        print(min(scnd_minr, minr))
                
            