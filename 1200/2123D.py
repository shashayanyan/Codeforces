"""
Alice and Bob are given a binary string s
 of length n
, and an integer k
 (1≤k<n
).

Alice wins if she is able to transform all characters of s
 into zeroes. If Alice is unable to win in a finite number of moves, then Bob wins.

Alice and Bob take turns, with Alice going first.

On Alice's turn, she may choose any subsequence∗
 of length k
 in s
, then set all characters in that subsequence to zero.
On Bob's turn, he may choose any substring†
 of length k
 in s
, then set all characters in that substring to one.
Note that Alice wins if the string consists of all zeros at any point during the game, including in between Alice's and Bob's turns.

Determine who wins with optimal play.

∗
A subsequence of a string s
 is a set of characters in s
. Note that these characters do not have to be adjacent.

†
A substring of a string s
 is a contiguous group of characters in s
. Note that these characters must be adjacent.

Input
The first line contains an integer t
 (1≤t≤104
)  — the number of test cases.

The first line of each test case contains two integers n
 and k
 (2≤n≤2⋅105
, 1≤k<n
).

The second line of each test case contains a binary string s
 of length n
.

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output on a single line "Alice" if Alice wins with optimal play, and "Bob" if Bob wins with optimal play.

You can output the answer in any case (upper or lower). For example, the strings "aLiCe", "alice", "ALICE", and "alICE" will be recognized as "Alice".
"""

def count_ones(s, n):
    cnt = 0
    for i in range(n):
        if s[i] == '1':
            cnt+=1
    return cnt

if __name__ == "__main__":
    winners = []
    m = int(input())
    for i in range(m):
        n, k = map(int, input().split())
        s = input()
        ones = count_ones(s, n)
        if ones > k and n >= 2 * k:
            print("BOB")
        else:
            print("ALICE")
    


