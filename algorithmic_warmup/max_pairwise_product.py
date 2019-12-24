# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    '''Find the largest and second largest index in array, then multiply those two'''

    # default is first element is largest
    max_index1 = None
    for i, v in enumerate(numbers):
        if max_index1 is None or numbers[i] > numbers[max_index1]:
            max_index1 = i

    max_index2 = None
    for i, v in enumerate(numbers):
        # make sure indices are not equal first, if this is case, False
        if (i != max_index1) and (max_index2 is None or numbers[i] > numbers[max_index2]):
            max_index2 = i

    max_product = numbers[max_index1] * numbers[max_index2]
    return max_product

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
