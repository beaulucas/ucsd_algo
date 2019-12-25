from algorithmic_warmup.least_common_multiple import lcm


def test_answer():
  assert lcm(8, 6) == 24
  assert lcm(8, 0) == 0
  assert lcm(761457, 614573) == 467970912861
