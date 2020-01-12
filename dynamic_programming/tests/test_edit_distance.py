from dynamic_programming.edit_distance import edit_distance
import string
import random


def test_answer():
  assert edit_distance(a='ab', b='ab') == 0
  assert edit_distance(a='short', b='ports') == 3
  assert edit_distance(a='editing', b='distance') == 5
  assert edit_distance(a='aaaaak', b='ak') == 4


def test_stress():
  length = 100
  a = ''.join(random.choice(string.ascii_lowercase) for x in range(length))
  b = ''.join(random.choice(string.ascii_lowercase) for x in range(length))
  assert edit_distance(a=a, b=b) <= 100
