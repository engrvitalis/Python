"""
Write a Python program that, given an initial positive integer, 
implements the Collatz conjecture by iteratively applying the rules to 
generate a sequence of numbers until reaching 1, and outputs this 
sequence along with the total number of steps taken. 
"""

# take any non-negative and non-zero integer number and name it c0;
c_0 = int(input("Enter a positive integer: "))
count = 0

while c_0 != 1:
    if c_0 % 2 == 0:
        # evaluate a new c0 as c0 ÷ 2;
        c_0 /= 2
    else:
    # evaluate a new c0 as 3 × c0 + 1;
        c_0 = 3 * c_0 + 1

    count += 1

    print(int(c_0))

print("steps: ", count)