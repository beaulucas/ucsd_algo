# Uses python3
import sys

def get_fib_mod(n, m):

    if n <= 1:
        return n

    # first thing to do is find the pisano sequence length for m
    # need to get f_n % m (remainder) until we encounter a sequence of 0 1, then stop

    # create empty list with base-case, every sequence starts with 0 1
    lst_mod = [0, 1]

    # if base case or ending in 0, 1 keep going
    while lst_mod == [0, 1] or lst_mod[-2:] != [0,1]:

      # grab f_n mod n until pattern emerges
      fib_mod = (lst_mod[-1] + lst_mod[-2]) % m
      print("remainder of", lst_mod[-1], "and", lst_mod[-2])
      print(fib_mod)
      lst_mod.append(fib_mod)
      print("new list is ", lst_mod)

    sequence = lst_mod[:-2]
    pisano_length = len(sequence)
    rmndr = n % pisano_length

    return sequence[rmndr]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fib_mod(n, m))
