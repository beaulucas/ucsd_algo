from greedy_algorithms.max_loot_value import get_optimal_value


def test_answer():
  assert int(get_optimal_value(capacity=50,
                           weights=[20, 50, 30],
                           values=[60, 100, 120])) == 180
  assert int(get_optimal_value(capacity=10,
                               weights=[30], values=[500])) == 166
  assert int(get_optimal_value(capacity=1000,
                               weights=[30], values=[500])) == 500
