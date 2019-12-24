from fib_mod import get_fib_mod

def test_answer():
  assert get_fib_mod(239, 1000) == 161
  assert get_fib_mod(2816213588, 239) == 151
  assert get_fib_mod(0, 2) == 0
  assert get_fib_mod(1, 3) == 1