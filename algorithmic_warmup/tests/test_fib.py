from algorithmic_warmup.fibonacci import fast_fib

def test_answer():
  assert fast_fib(0) == 0
  assert fast_fib(1) == 1
  assert fast_fib(2) == 1
  assert fast_fib(10) == 55
