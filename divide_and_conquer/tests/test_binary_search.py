from divide_and_conquer.binary_search import binary_search
import random
import time

def test_answer():
  a = [1, 5, 8, 12, 13]
  assert binary_search(a=a, x=23) == -1
  assert binary_search(a=a, x=8) == 2


def test_stress():
  random.seed(400)
  numbers = sorted(random.sample(range(1, pow(10, 9)), 3 * pow(10, 4)))
  values = sorted(random.sample(range(1, pow(10, 9)), pow(10, 5)))
  for x in values:
    binary_search(a=numbers, x=x)
