"""
You have a positive integer m and a non-negative integer s. Your task is to find the smallest and the largest of the numbers that have length m and sum of digits s. The required numbers should be non-negative integers written in the decimal base without leading zeroes.

Input
The single line of the input contains a pair of integers m, s (1 ≤ m ≤ 100, 0 ≤ s ≤ 900) — the length and the sum of the digits of the required numbers.

Output
In the output print the pair of the required non-negative integer numbers — first the minimum possible number, then — the maximum possible number. If no numbers satisfying conditions required exist, print the pair of numbers "-1 -1" (without the quotes).
"""

if __name__ == "__main__":
    m, s = map(int, input().split())

    biggest = 0
    current_sum = 0
    digit_count = 0

    if s==0 and m==1:
        print("0 0")

    elif s == 0 or s > 9*m:
        print("-1 -1")
    
    else:

        while digit_count < m:
            r = s - current_sum
            if r >= 9:
                biggest = biggest*10 + 9
                current_sum = current_sum + 9
                digit_count += 1
            else:
                biggest = biggest*10 + r
                current_sum = current_sum + r
                digit_count += 1
        


        if s-1 <= (m-1)*9:
            smallest = 1
        else:
            smallest = s - (m-1)*9

        current_sum = smallest
        digit_count = 1

        while digit_count < m:
            r = s - current_sum
            tmp = m - digit_count - 1
            #print("r= ", r, " tmp= ", tmp)
            
            
            
            
            
            
            if r != 0:
                if (r) <= (tmp * 9):
                    #print("in if, digit_count= ", digit_count)
                    # can put 0, but if not, we need to find the one that allows that
                    smallest = (smallest * 10) 
                    #current_sum += 1
                    digit_count += 1
                else:
                    #print("in else, digit_count= ", digit_count)
                    next_digit = r - tmp*9
                    smallest = (smallest * 10) + next_digit
                    current_sum += next_digit
                    digit_count += 1
            else:
                smallest = smallest*10
                digit_count += 1
        
        print(smallest, biggest)

        