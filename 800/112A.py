"""
Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.

Input
Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

Output
If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.
"""
def Petya_and_Strings(s1, s2, n):
    for i in range(n):
        if s1[i] < s2[i]:
            return -1
        elif s1[i] > s2[i]:
            return 1
        elif s1[i] == s2[i] and i == n-1:
            return 0
    return 0


if __name__ == "__main__":
    str1 = input().lower()
    str2 = input().lower()
    N = len(str1)
    print(Petya_and_Strings(str1, str2, N))