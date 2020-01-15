from dynamic_programming.knapsack import optimal_weight
import random


def test_answer():
  assert optimal_weight(total_capacity=10, weights=[1, 4, 8]) == 9
  assert optimal_weight(total_capacity=13, weights=[1, 4, 8]) == 13


def test_stress():
  random.seed(400)
  stress_weights = random.sample(range(0, pow(10, 5)), 300)
  stress_capacity = pow(10, 4)
  assert optimal_weight(total_capacity=stress_capacity, weights=stress_weights) <= stress_capacity

