# Uses python3
import sys

def get_majority_element(a, constraints=True):
  """
  Check whether an input sequence contains a majority element. Depending on parity of list length,
  will scan at different midpoint.
  :param a: List of elements.
  :param constraints: Local problem constraints
  :return: 1 if the sequence contains an element that appears more than len(a) / 2 times, else 0
  """

  a = sorted(a)

  if constraints:
    assert 1 <= len(a) <= pow(10, 5)
    assert 0 <= a[-1] <= pow(10, 9)

  count = 0
  decision_index = len(a) // 2

  element = a[decision_index]
  for i, v in enumerate(a):
    if a[i] == element:
      count += 1
  if count > len(a) // 2:
    return 1
  else:
    return 0


if __name__ == '__main__':
  input = sys.stdin.read()
  n, *a = list(map(int, input.split()))
  print(get_majority_element(a))
