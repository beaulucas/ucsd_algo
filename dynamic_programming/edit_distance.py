#python3


def edit_distance(a, b, constraints=False):
  """
  Calculate the minimum number of operations (insert, delete, or substitute) to transform
  lowercase string {a} into string {b}.
  :param a: first string
  :param b: second string
  :param constraints: problem constraints set by homework
  :return: minimum number of operations required to transform {a} into {b}
  """

  if constraints:
    assert min(len(a), len(b)) >= 1
    assert max(len(a), len(b)) <= 100

  # add zero padding
  a = a.rjust(len(a) + 1)
  b = b.rjust(len(b) + 1)
  d = [[0] * len(a) for i in range(len(b))]
  # d(i, j) == edit distance between a[0:i+1] and b[0:j+1]

  for index_a, letter_a in enumerate(a):
    for index_b, letter_b in enumerate(b):
      if index_a == 0 and index_b == 0:
        d[index_b][index_a] = 0
      elif index_a == 0 and index_b != 0:
        d[index_b][index_a] = len(b[0:index_b])
      elif index_a != 0 and index_b == 0:
        d[index_b][index_a] = len(a[0:index_a])
      else:
        if letter_a == letter_b:
          dist = d[index_b - 1][index_a - 1]
        else:
          min_neighbor = min(d[index_b - 1][index_a],
                             d[index_b][index_a - 1],
                             d[index_b - 1][index_a - 1])
          dist = min_neighbor + 1

        d[index_b][index_a] = dist

  return d[len(b) - 1][len(a) - 1]


if __name__ == "__main__":
  print(edit_distance(input(), input()))
