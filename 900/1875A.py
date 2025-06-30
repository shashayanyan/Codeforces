"""
Flowey has planted a bomb in Snowdin!

The bomb has a timer that is initially set to b
. Every second, the timer will decrease by 1
. When the timer reaches 0
, the bomb will explode! To give the residents of Snowdin enough time to evacuate, you will need to delay the bomb from exploding for as long as possible.

You have n
 tools. Each tool can only be used at most once. If you use the i
-th tool, the timer will increase by xi
. However, if the timer is changed to an integer larger than a
, the timer will be set to a
 due to a bug.

More specifically, the following events will happen every second in the following order:

You will choose some (possibly none) of your tools that have not been used before. If you choose the i
-th tool, and the bomb's timer is currently set to c
, the timer will be changed to min(c+xi,a)
.
The timer decreases by 1
.
If the timer reaches 0
, the bomb explodes.
Jellyfish now wants to know the maximum time in seconds until the bomb explodes if the tools are used optimally.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤2000
). The description of the test cases follows.

The first line of each test case contains three integers a
, b
 and n
 (1≤b≤a≤109
, 1≤n≤100
) — the maximum value of the bomb's timer, the initial value of the timer of the bomb and the number of tools.

The second line of each test contains n
 integers x1,x2,…,xn
 (1≤xi≤109
) — the number the timer can increase by using the i
-th tool.

Note that the sum of n
 over all test cases is not bounded.

Output
For each test case, output a single integer — the maximum time in seconds until the bomb explodes.
"""

if __name__ == "__main__":
    k = int(input())
    ttimes = []
    for i in range(k):
        ttime = 0
        a, b, n = map(int, input().split())
        tools = list(map(int, input().split()))
        used = [0] * n
        c = b
        for j in tools:
            if j >= a:
                c += a-1
            else:
                c += j
        ttimes.append(c)
    
    for i in ttimes:
            print(i)
"""        while c > 0:
            ttime += 1
            for j in range(n):
                if used[j] == 0:
                    if tools[j] + c < a:
                        c = min(tools[j]+c, a)
                        used[j] = 1
                    elif c == 1: # and tools[j] + c >= a
                        c = min(tools[j]+c, a)
                        used[j] = 1
            
            c -= 1
        ttimes.append(ttime)"""

    