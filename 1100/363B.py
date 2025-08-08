"""
There is a fence in front of Polycarpus's home. The fence consists of n planks of the same width which go one after another from left to right. The height of the i-th plank is hi meters, distinct planks can have distinct heights.

Polycarpus has bought a posh piano and is thinking about how to get it into the house. In order to carry out his plan, he needs to take exactly k consecutive planks from the fence. Higher planks are harder to tear off the fence, so Polycarpus wants to find such k consecutive planks that the sum of their heights is minimal possible.

Write the program that finds the indexes of k consecutive planks with minimal total height. Pay attention, the fence is not around Polycarpus's home, it is in front of home (in other words, the fence isn't cyclic).

Input
The first line of the input contains integers n and k (1 ≤ n ≤ 1.5·105, 1 ≤ k ≤ n) — the number of planks in the fence and the width of the hole for the piano. The second line contains the sequence of integers h1, h2, ..., hn (1 ≤ hi ≤ 100), where hi is the height of the i-th plank of the fence.

Output
Print such integer j that the sum of the heights of planks j, j + 1, ..., j + k - 1 is the minimum possible. If there are multiple such j's, print any of them.
"""


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [0]*(n+1)
    dp[0] = sum([x for x in a[:k]])
    print("dp[0]: ", dp[0])
    min_effort = dp[0]
    me_index = 0
    for i in range(1, n-k+1):
        dp[i] = dp[i-1] - a[i-1] + a[i+k-1]
        if dp[i] < min_effort:
            print("new min found at index: ", i)
            min_effort = dp[i]
            me_index = i

    print(me_index+1)