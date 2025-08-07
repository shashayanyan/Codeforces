"""
Allen has a LOT of money. He has n
 dollars in the bank. For security reasons, he wants to withdraw it in cash (we will not disclose the reasons here). The denominations for dollar bills are 1
, 5
, 10
, 20
, 100
. What is the minimum number of bills Allen could receive after withdrawing his entire balance?

Input
The first and only line of input contains a single integer n
 (1≤n≤109
).

Output
Output the minimum number of bills that Allen could receive.
"""

if __name__ == "__main__":
    n = int(input())
    bills = [100,20,10,5,1]
    b_count = 5
    min_bills = 0
    for i in bills:
        if n >= i:
            min_bills += n // i
            n = n % i
    
    print(min_bills)