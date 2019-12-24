#python3
import sys

def get_fib_last_digit(n, local_constraints=True):

  '''calculates the n^th fibonacci number's last digit'''

  # set up base cases
  lst = [0, 1]

  if local_constraints:
    assert n <= pow(10, 7)

  for i in range(2, n + 1):
    # if last digits of previous numbers are x = 5 and y = 7,
    # last digit of new number must (x + y) % 10
    last_digit = (lst[i - 1] + lst[i - 2]) % 10
    lst.append(last_digit)

  return lst[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fib_last_digit(n))