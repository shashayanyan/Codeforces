"""
Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

Note, that during capitalization all the letters except the first one remains unchanged.

Input
A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 103.

Output
Output the given word after capitalization.
"""

if __name__ == "__main__":
    s = input()
    first_letter = s[0]
    print(first_letter.upper(), end="")
    if len(s) > 1:
        print(s[1:])