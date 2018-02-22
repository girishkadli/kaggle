import sys
T = int(input())
for t in range(T):
    input_str = input()
    n, m, x, k = [int(v) for v in input_str.split(' ')]
    odd_even = input()
    odd_count = odd_even.count("O")
    even_count = odd_even.count("E")
    for i in range(1, m + 1):
        if (i%2 == 1):
            if (odd_count >= x):
                n -= x
                odd_count -= x
            else:
                n -= odd_count
                odd_count = 0
        else:
            if (even_count >= x):
                n -= x
                even_count -= x
            else:
                n -= even_count
                even_count = 0
    if (n <= 0):
        print("yes")
    else:
        print("no")
