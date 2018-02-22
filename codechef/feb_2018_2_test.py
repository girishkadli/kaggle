import sys
T = int(input())
for z in range(T):
    input_str = input()
    N, m, x, k = [int(i) for i in input_str.split(" ")]
    s = input()
    even_count = s.count("E")
    odd_count = s.count("O")
    for c in range(1, m + 1):
        if (not c % 2 == 0):
            if (odd_count >= x):
                N -= x
                odd_count -= x
            else:
                N -= odd_count
                odd_count = 0
        else:
            if (even_count >= x):
                N -= x
                even_count -= x
            else:
                N -= even_count
                even_count = 0
    if (N <= 0):
        print("yes")
    else:
        print("no")
