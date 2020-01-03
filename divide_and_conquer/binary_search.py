#python3
import sys


def binary_search(a, x):
  """
  Search a sorted list for an element by dividing list in half until value is found.
  :param a: The sorted list
  :param x: The element to search for
  :return: index of {a} where value {x} is found, otherwise -1
  """

  low_index = 0
  high_index = len(a) - 1
  assert high_index >= low_index

  while low_index <= high_index:
    mid_index = (low_index + high_index) // 2
    if a[mid_index] > x:
      high_index = mid_index - 1
    elif a[mid_index] < x:
      low_index = mid_index + 1
    else:
      return mid_index

  return -1


if __name__ == '__main__':
  input = sys.stdin.read()
  data = list(map(int, input.split()))
  n = data[0]
  m = data[n + 1]
  a = data[1:n + 1]
  assert 1 <= len(a) <= 3 * pow(10, 4)
  assert 1 <= len(data[n + 2:]) <= pow(10, 5)
  assert 1 <= a[-1] <= pow(10, 9)
  assert 1 <= data[n + 2:][-1] <= pow(10, 9)

  for x in data[n + 2:]:
    # replace with the call to binary_search when implemented
    print(binary_search(a, x), end=' ')
