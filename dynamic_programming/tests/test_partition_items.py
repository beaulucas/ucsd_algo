from dynamic_programming.partition_items import partition3


def test_answer():
  assert partition3(values=[1]) == 0
  assert partition3(values=[3, 3, 3, 3]) == 0
  assert partition3(values=[40]) == 0
  assert partition3(values=[17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]) == 1
  assert partition3(values=[1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]) == 1
  assert partition3(values=[5, 5, 5, 15, 15]) == 1
