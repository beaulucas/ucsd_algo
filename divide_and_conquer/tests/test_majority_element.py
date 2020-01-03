from divide_and_conquer.majority_element import get_majority_element
import random


def test_answer():
  assert get_majority_element(a=[2, 3, 9, 2, 2]) == 1
  assert get_majority_element(a=[1, 2, 3, 4]) == 0


def test_stress():
  random.seed(400)
  a = sorted(random.sample(range(1, pow(10, 9)), pow(10, 5)))
  assert get_majority_element(a) == 0

