from greedy_algorithms.car_fueling import compute_min_refills


def test_answer():
  assert compute_min_refills(distance=950, tank=400, stops=[200, 375, 550, 750]) == 2
  assert compute_min_refills(distance=10, tank=3, stops=[1,2,5,9]) == -1
