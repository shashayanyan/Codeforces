"""
You are given array consisting of n integers. Your task is to find the maximum length of an increasing subarray of the given array.

A subarray is the sequence of consecutive elements of the array. Subarray is called increasing if each element of this subarray strictly greater than previous.

Input
The first line contains single positive integer n (1 ≤ n ≤ 105) — the number of integers.

The second line contains n positive integers a1, a2, ..., an (1 ≤ ai ≤ 109).

Output
Print the maximum length of an increasing subarray of the given array.
"""

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    dp = [1]*n
    max_len = 1

    for i in range(1, n):
        if a[i] > a[i-1]:
            dp[i] = dp[i-1]+1
            if dp[i] > max_len:
                max_len = dp[i]
        
    print(max_len)
