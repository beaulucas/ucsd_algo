# Uses python3
import sys

def lcm(a, b, local_constraints=True):

  '''
  Given two integers, find their least common multiple.
  lcm(6, 8) = 24
  gcd(8, 6) = 2
  (a * b) / gcd(a, b) = lcm

  :param a:
  :param b:
  :param local_constraints:
  :return:
  '''

  if local_constraints:
    assert 1 <= a
    assert b <= pow(10, 7)

  product = a * b

  # grab gcd
  if a == 0 | b == 0:
    return 0

  while b > 0:
    remainder = a % b
    a = b
    b = remainder

  if b == 0:
    gcd = a

  lcm = int(product / gcd)
  return lcm

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
