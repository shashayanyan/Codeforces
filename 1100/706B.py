"""
Vasiliy likes to rest after a hard work, so you may often meet him in some bar nearby. As all programmers do, he loves the famous drink "Beecola", which can be bought in n different shops in the city. It's known that the price of one bottle in the shop i is equal to xi coins.

Vasiliy plans to buy his favorite drink for q consecutive days. He knows, that on the i-th day he will be able to spent mi coins. Now, for each of the days he want to know in how many different shops he can buy a bottle of "Beecola".

Input
The first line of the input contains a single integer n (1 ≤ n ≤ 100 000) — the number of shops in the city that sell Vasiliy's favourite drink.

The second line contains n integers xi (1 ≤ xi ≤ 100 000) — prices of the bottles of the drink in the i-th shop.

The third line contains a single integer q (1 ≤ q ≤ 100 000) — the number of days Vasiliy plans to buy the drink.

Then follow q lines each containing one integer mi (1 ≤ mi ≤ 109) — the number of coins Vasiliy can spent on the i-th day.

Output
Print q integers. The i-th of them should be equal to the number of shops where Vasiliy will be able to buy a bottle of the drink on the i-th day.
"""

def bin_search(p_count, prices, p):
    res = -1
    l = 0
    r = p_count-1
    while l <= r:
        mid = (l+r)//2
        if prices[mid] <= p:
            res = mid
            l = mid+1
        else:
            r = mid-1
    return res+1



if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    shops = len(x)
    q = int(input())
    dp = {}
    x.sort()
    for i in range(q):
        day = int(input()) 
        bars = dp.get(day)
        if bars is None:
            bars = bin_search(shops, x, day)
            dp.update({day: bars})
        
        print(bars)

"""    
    for i in range(q):
        if dp[days[i]] == -1:
            dp[days[i]] = bin_search(x, days[i])
        print(dp[days[i]])"""
        
