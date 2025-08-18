"""
Iahub got bored, so he invented a game to be played on paper.

He writes n integers a1, a2, ..., an. Each of those integers can be either 0 or 1. He's allowed to do exactly one move: he chooses two indices i and j (1 ≤ i ≤ j ≤ n) and flips all values ak for which their positions are in range [i, j] (that is i ≤ k ≤ j). Flip the value of x means to apply operation x = 1 - x.

The goal of the game is that after exactly one move to obtain the maximum number of ones. Write a program to solve the little game of Iahub.

Input
The first line of the input contains an integer n (1 ≤ n ≤ 100). In the second line of the input there are n integers: a1, a2, ..., an. It is guaranteed that each of those n values is either 0 or 1.

Output
Print an integer — the maximal number of 1s that can be obtained after exactly one move.
"""


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    best = -1
    current_start = -1
    #current_end = 0
    current_value = 0

    count_ones = 0

    for i in range(n):
        if a[i] == 1:
            count_ones += 1
        if current_start == -1:
            if a[i] == 0:
                current_start = i
                #current_end = i
                current_value = 1
                if current_value > best:
                    best = current_value
        else:
            if a[i] == 0:
                #current_end += 1
                current_value += 1
                if current_value > best :
                    best = current_value
            else : # a[i]==1
                current_value -= 1
                if current_value == 0:
                    current_start = -1

    
    print(count_ones + best)