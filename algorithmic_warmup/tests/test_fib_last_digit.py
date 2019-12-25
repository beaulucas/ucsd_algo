from algorithmic_warmup.fib_last_digit import get_fib_last_digit


def test_answer():
  assert get_fib_last_digit(0) == 0
  assert get_fib_last_digit(1) == 1
  assert get_fib_last_digit(2) == 1
  assert get_fib_last_digit(10) == 5
