"""
Sereja has an array a, consisting of n integers a1, a2, ..., an. The boy cannot sit and do nothing, he decided to study an array. Sereja took a piece of paper and wrote out m integers l1, l2, ..., lm (1 ≤ li ≤ n). For each number li he wants to know how many distinct numbers are staying on the positions li, li + 1, ..., n. Formally, he want to find the number of distinct numbers among ali, ali + 1, ..., an.?

Sereja wrote out the necessary array elements but the array was so large and the boy was so pressed for time. Help him, find the answer for the described question for each li.

Input
The first line contains two integers n and m (1 ≤ n, m ≤ 105). The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 105) — the array elements.

Next m lines contain integers l1, l2, ..., lm. The i-th line contains integer li (1 ≤ li ≤ n).

Output
Print m lines — on the i-th line print the answer to the number li.
"""

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    dp = set()
    for i in range(n):
        dp.add( a[n-i-1] )
        a[n-i-1] = len(dp)


    for i in range(m):
        li = int(input())
        print(a[li-1])