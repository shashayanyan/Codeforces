"""
All cities of Lineland are located on the Ox coordinate axis. Thus, each city is associated with its position xi — a coordinate on the Ox axis. No two cities are located at a single point.

Lineland residents love to send letters to each other. A person may send a letter only if the recipient lives in another city (because if they live in the same city, then it is easier to drop in).

Strange but true, the cost of sending the letter is exactly equal to the distance between the sender's city and the recipient's city.

For each city calculate two values ​​mini and maxi, where mini is the minimum cost of sending a letter from the i-th city to some other city, and maxi is the the maximum cost of sending a letter from the i-th city to some other city

Input
The first line of the input contains integer n (2 ≤ n ≤ 105) — the number of cities in Lineland. The second line contains the sequence of n distinct integers x1, x2, ..., xn ( - 109 ≤ xi ≤ 109), where xi is the x-coordinate of the i-th city. All the xi's are distinct and follow in ascending order.

Output
Print n lines, the i-th line must contain two integers mini, maxi, separated by a space, where mini is the minimum cost of sending a letter from the i-th city, and maxi is the maximum cost of sending a letter from the i-th city.
"""

if __name__ == "__main__":
    n = int(input())
    cities = list(map(int, input().split()))
    print( cities[1] - cities[0], " ", cities[n-1] - cities[0] )
    for i in range(1, n-1):
        print( min(cities[i+1] - cities[i], cities[i] - cities[i-1]), " ", max(cities[n-1] - cities[i], cities[i] - cities[0]) )
    print( cities[n-1] - cities[n-2], " ", cities[n-1] - cities[0])