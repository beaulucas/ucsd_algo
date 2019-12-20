# Uses python3
import sys

def gcd(a, b, local_constraints=True):

  if local_constraints:
    assert 1 <= a
    assert b <= 2 * pow(10, 9)

  if a == 0 | b == 0:
    return 0

  # assign a to b and b to remainder
  # keep going until b reaches 0
  while b > 0:
    remainder = a % b
    a = b
    b = remainder

  if b == 0:
    gcd = a

  return gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))