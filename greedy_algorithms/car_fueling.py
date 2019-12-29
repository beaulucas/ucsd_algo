#python3
import sys


def compute_min_refills(distance, tank, stops, constraints=True):
  """
  Calculates the smallest number of refills to complete a journey of {distance} across
  {stops} with a fuel capacity of {tank}.

  Safe move: Find the furthest gas station away to refill at.

  :param distance: how far the journey is
  :param tank: fuel capacity of gas tank
  :param stops: list of distances of gas station stops
  :param constraints: problem constraints
  :return: minimum number of refills to complete journey, or -1 if impossible
  """
  constraints = True

  if constraints:
    assert 1 <= distance <= pow(10, 5)
    assert 1 <= tank <= 400
    assert 1 <= len(stops) <= 300
    assert max(stops) < distance
    assert min(stops) > 0
    assert sorted(stops) == stops

  # problem constants
  starting_position = 0
  a = [starting_position] + stops + [distance]

  # variables to iterate on:
  current_refill_index = 0
  num_refills = 0
  current_position = starting_position

  while current_position < distance:
    for index, stop in enumerate(a):
      if distance - current_position <= tank:
        current_position = distance
        break
      elif stop - current_position <= tank:
        pass
      # find first stop at least 2 stops away that is further than tank
      # once we find this, we know we need to refill at the prior stop
      elif (stop - current_position) > tank and (index != current_refill_index + 1):
        current_refill_index = index - 1
        current_position = a[current_refill_index]
        num_refills += 1
        a = a[current_refill_index:]
        current_refill_index = 0
        break
      # if stop is next stop and further than tank, we can't complete journey
      elif (stop - current_position) > tank and index == current_refill_index + 1:
        return -1
  return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
