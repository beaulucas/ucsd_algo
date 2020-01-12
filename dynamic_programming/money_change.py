#python3
import sys


def get_change(m):
  """
  Produce minimal number of coins needed to change money,
  given coin denominations of (1, 3, 4). Function utilizies
  :param m: Money to be changed
  :return: Minimum number of coins that changes {m}
  """

  denoms = [1, 3, 4]
  # set arbitary value as amount + 1 used to find minimum later
  min_coins = (m + 1) * [m + 1]
  min_coins[0] = 0
  # we want to compute for every amount of money, how many coins to change it
  for money, min_coin in enumerate(min_coins):

    k = (max(denoms) + 1) * [m + 1]
    # for each money, find optimal number of steps to change
    for denom in denoms:
      if money == 0:
        k[denom] = 0
        break
      if denom > money:
        pass
      elif denom <= money:
        # go back a step to see how many steps it took minus this last coin, then add 1
        money_remaining = money - denom
        k[denom] = min_coins[money_remaining] + 1

      min_coins[money] = min(k)

  return min_coins[m]


if __name__ == '__main__':
  m = int(sys.stdin.read())
  print(get_change(m))
