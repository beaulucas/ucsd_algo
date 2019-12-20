#python3
def fast_fib(n):
    '''calculates the n^th fibonacci number'''

    # constraints
    assert n <= 45

    # create empty list with base-case
    lst = [0, 1]

    for i in range(2, n+1):
        lst.append(lst[i-1] + lst[i-2])
    return lst[n]

n = int(input())
print(fast_fib(n))


