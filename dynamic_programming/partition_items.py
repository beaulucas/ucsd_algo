# python3
import sys


def partition3(values):
  """
  Evenly split value of items among three partitions using dynamic programming.
  :param values: values of the items to split
  :return: 1 if possible to partition, else 0
  """

  values = sorted(values)
  target_bucket_value = int(sum(values) / 3)
  sums = range(0, target_bucket_value + 1)

  if sum(values) % 3 != 0:
    return 0
  if values[-1] > target_bucket_value:
    return 0

  # d[i][s1][s2] = boolean if it is possible to make sums s1 and s2 with subset i
  d = [
    [[None for s in list(sums)] for s in list(sums)] for subset in range(len(values))
  ]

  for ind, val in enumerate(values):
    subset = values[0 : ind + 1]
    for s1 in sums:
      for s2 in sums:
        if s1 == 0 and s2 == 0:
          d[ind][s1][s2] = True
        # another base case when subset is one item
        elif len(subset) == 1:
          can_fill = (sum(subset) == s2 or sum(subset) == s1) and (s1 == 0 or s2 == 0)
          d[ind][s1][s2] = can_fill
        else:
          # we have multiple choices
          # if item is too large for s1, skip s1, then check if we can use or skip for s2
          # if item is right size for s1, use it
          fits_s1 = subset[-1] <= s1
          fits_s2 = subset[-1] <= s2

          if not fits_s1:
            if not fits_s2:
              # can't use either, so we must skip for both
              d[ind][s1][s2] = d[ind - 1][s1][s2]
            elif fits_s2:
              use_s2 = d[ind][s1][s2 - subset[-1]]
              skip_s2 = d[ind - 1][s1][s2]
              d[ind][s1][s2] = max(use_s2, skip_s2)
          elif fits_s1:
            d[ind][s1][s2] = d[ind][s1 - subset[-1]][s2]

  return int(d[-1][-1][-1])


if __name__ == "__main__":
  input = sys.stdin.read()
  n, *values = list(map(int, input.split()))
  print(partition3(values))
