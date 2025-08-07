"""
Kefa decided to make some money doing business on the Internet for exactly n days. He knows that on the i-th day (1 ≤ i ≤ n) he makes ai money. Kefa loves progress, that's why he wants to know the length of the maximum non-decreasing subsegment in sequence ai. Let us remind you that the subsegment of the sequence is its continuous fragment. A subsegment of numbers is called non-decreasing if all numbers in it follow in the non-decreasing order.

Help Kefa cope with this task!

Input
The first line contains integer n (1 ≤ n ≤ 105).

The second line contains n integers a1,  a2,  ...,  an (1 ≤ ai ≤ 109).

Output
Print a single integer — the length of the maximum non-decreasing subsegment of sequence a.
"""


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    lens = [1]
    for i in range(1,n):
        if a[i] >= a[i-1]:
            lens.append(lens[i-1]+1)
        else:
            lens.append(1)
    
    print(max(lens))