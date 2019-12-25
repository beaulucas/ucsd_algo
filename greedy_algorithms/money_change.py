#python3
import sys

def get_change(m, constraints=True):

  """
  Find the minimum number of coins needed to change the input value (an integer)
  into coins with denominations 1, 5, and 10.
  :param m: the amount of money to change (in cents)
  :return: minimum number of coins with denominations 1,5, 10 that changes m
  """

  if constraints:
    assert 1 <= m <= pow(10, 3)

  dimes = 0
  nickels = 0
  pennies = 0
  change_remaining = m

  # see how many dimes we can get
  # then see how many nickels
  # then see how many pennies

  while change_remaining > 0:

    if change_remaining // 10 > 0:
      dimes = change_remaining // 10
      change_remaining = change_remaining - (dimes * 10)
    if change_remaining // 5 > 0:
      nickels = change_remaining // 5
      change_remaining = change_remaining - (nickels * 5)
    pennies = change_remaining
    change_remaining = change_remaining - pennies

  return dimes + nickels + pennies


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
