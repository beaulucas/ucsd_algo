#python3
import sys
import random


def partition3(a, l, r):
  """
  Partitions array a into three parts based on value of x. Used recursively by quicksort.
  First part range(0, m1) is < x
  Second part range(m1, m2 + 1) == x
  Third part range(m2 + 1, r) > x
  :param a: input array
  :param l: left-most index
  :param r: right-most index
  :return: m1 and m2, which split array as above
  """

  k = random.randint(l, r)
  m1 = l
  m2 = l
  x = a[k]

  a[l], a[k] = a[k], a[l]

  for i in range(l + 1, r + 1):
    if a[i] < x:
      a[i], a[m1] = a[m1], a[i]
      a[i], a[m2 + 1] = a[m2 + 1], a[i]
      m1 += 1
      # because we pushed range right we need to extend upper
      m2 += 1
    elif a[i] == x:
      a[i], a[m2 + 1] = a[m2 + 1], a[i]
      m2 += 1

  return [m1, m2]


def randomized_quick_sort(a, l, r):
  """
  Randomized three-way quicksort. Selects random pivot and partitions array, then partitions
  sub arrays until array is sorted.
  :param a: input array
  :param l: left-most index to sort
  :param r: right-most index to sort
  :return: None, modifies array in place
  """
  if l >= r:
    return

  m = partition3(a, l, r)
  left = len(a[m[1]+1:r+1])
  right = len(a[l:m[0]])

  if left == 1:
    randomized_quick_sort(a, l, m[0])
  elif right == 1:
    randomized_quick_sort(a, m[1] + 1, r)
  else:
    randomized_quick_sort(a, l, m[0])
    randomized_quick_sort(a, m[1] + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    assert 1 <= len(a) <= pow(10, 5)
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
