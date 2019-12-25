from greedy_algorithms.money_change import get_change


def test_answer():
  assert get_change(500) == 50
  assert get_change(28) == 6
  assert get_change(2) == 2
  assert get_change(55) == 6
