from dynamic_programming.money_change import get_change


def test_answer():
  assert get_change(2) == 2
  assert get_change(34) == 9
  assert get_change(1000) == 250
