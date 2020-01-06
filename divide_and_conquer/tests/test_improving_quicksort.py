from divide_and_conquer.improving_quicksort import partition3, randomized_quick_sort
import random


def test_answer():
  a = [2, 3, 9, 2, 2]
  a_sorted = sorted(a)
  b = [2, 2, 2, 2, 2, 8, 4, 9, 3, 1, 2, 10, 11, 22, 4, 2, 1, 3]
  b_sorted = sorted(b)
  c = [1, 2, 3, 4, 1, 2]
  c_sorted = sorted(c)
  randomized_quick_sort(c, 0, len(c) - 1)
  randomized_quick_sort(a=a, l=0, r=len(a) - 1)
  randomized_quick_sort(a=b, l=0, r=len(b) - 1)
  assert a == a_sorted
  assert b == b_sorted
  assert c == c_sorted


def test_stress():
  random.seed(400)
  a = random.sample(range(1, pow(10, 9)), pow(10, 5))
  a_sorted = sorted(a)
  randomized_quick_sort(a=a,l=0,r=len(a) - 1)
  assert a == a_sorted


