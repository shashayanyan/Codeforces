"""
Ilya the Lion wants to help all his friends with passing exams. They need to solve the following problem to pass the IT exam.

You've got string s = s1s2... sn (n is the length of the string), consisting only of characters "." and "#" and m queries. Each query is described by a pair of integers li, ri (1 ≤ li < ri ≤ n). The answer to the query li, ri is the number of such integers i (li ≤ i < ri), that si = si + 1.

Ilya the Lion wants to help his friends but is there anyone to help him? Help Ilya, solve the problem.

Input
The first line contains string s of length n (2 ≤ n ≤ 105). It is guaranteed that the given string only consists of characters "." and "#".

The next line contains integer m (1 ≤ m ≤ 105) — the number of queries. Each of the next m lines contains the description of the corresponding query. The i-th line contains integers li, ri (1 ≤ li < ri ≤ n).

Output
Print m integers — the answers to the queries in the order in which they are given in the input.
"""

if __name__ == "__main__":
    s = input()
    n = len(s)
    m = int(input())

    dp = [0]*(n+1)
    for i in range(1,n):
        if s[i-1] == s[i]:
            dp[i] = dp[i-1]+1
        else:
            dp[i] = dp[i-1]

    dp[n] = dp[n-1]

    for i in range(m):
        l, r = map(int, input().split())
        print(dp[r-1] - dp[l-1])