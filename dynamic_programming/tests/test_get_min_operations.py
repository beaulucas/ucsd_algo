from dynamic_programming.minimum_operations import get_min_operations


def test_answer():

  assert get_min_operations(1)[0] == 0
  assert get_min_operations(5)[0] == 3
  assert get_min_operations(96234)[0] == 14

def test_stress():
  n = pow(10, 6)
  assert get_min_operations(n)[0] == 19
