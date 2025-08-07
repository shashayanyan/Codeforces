"""
Polycarpus has a ribbon, its length is n. He wants to cut the ribbon in a way that fulfils the following two conditions:

After the cutting each ribbon piece should have length a, b or c.
After the cutting the number of ribbon pieces should be maximum.
Help Polycarpus and find the number of ribbon pieces after the required cutting.

Input
The first line contains four space-separated integers n, a, b and c (1 ≤ n, a, b, c ≤ 4000) — the length of the original ribbon and the acceptable lengths of the ribbon pieces after the cutting, correspondingly. The numbers a, b and c can coincide.

Output
Print a single number — the maximum possible number of ribbon pieces. It is guaranteed that at least one correct ribbon cutting exists.
"""

if __name__ == "__main__":
    n, a, b, c = map(int, input().split())
    allowed_lens = [a,b,c]
    min_allowed_len = min(allowed_lens)
    dp = [0]*(n+1)
    for i in range(min_allowed_len):
        dp[i]=0

    dp[min_allowed_len] = 1

    # base made
    for i in range(min_allowed_len+1, n+1):
        if i >= a:
            dp_a = dp[i-a]
        else:
            dp_a = 0
        
        if i >= b:
            dp_b = dp[i-b]
        else:
            dp_b = 0
        
        if i >= c:
            dp_c = dp[i-c]
        else:
            dp_c = 0
        
        dp_i = 0
        if i in allowed_lens:
            dp_i = 1
        if dp_a != 0:
            dp_i = max(dp_i, dp_a + 1)
        if dp_b != 0:
            dp_i = max(dp_i, dp_b + 1)
        if dp_c != 0:
            dp_i = max(dp_i, dp_c + 1)
        
        dp[i] = dp_i
    
    print(dp[-1])