"""
You are given string s. Your task is to determine if the given string s contains two non-overlapping substrings "AB" and "BA" (the substrings can go in any order).

Input
The only line of input contains a string s of length between 1 and 105 consisting of uppercase Latin letters.

Output
Print "YES" (without the quotes), if string s contains two non-overlapping substrings "AB" and "BA", and "NO" otherwise.
"""

def find_AB(s):
    n = len(s)
    ab_start_indices = []
    i = 0
    while(i < n-1):
        if s[i]=="A":
            if s[i+1]=="B":
                ab_start_indices.append(i)
                i += 2
            else:
                i += 1
        else:
            i += 1
    return ab_start_indices


def find_BA(s):
    n = len(s)
    ba_start_indices = []
    i = 0
    while(i < n-1):
        if s[i]=="B":
            if s[i+1]=="A":
                ba_start_indices.append(i)
                i += 2
            else:
                i += 1
        else:
            i += 1
    return ba_start_indices


if __name__ == "__main__":
    s = input()

    ba_list = find_BA(s)
    ab_list = find_AB(s)

    if ba_list == [] or ab_list == []:
        print("NO")
    else:
        res = "NO"
        for i in ab_list:
            for j in ba_list:
                if abs(i - j) > 1:
                    res = "YES"
                    break
            if res=="YES":
                break
        
        print(res)


