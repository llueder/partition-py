from .types import Instance, Partition

def naive_greedy(numbers: Instance, return_indices=False) -> Partition:
    numbers = sorted(numbers, reverse=True)

    list_a = []
    list_b = []
    sum_a = 0
    sum_b = 0

    for idx, number in enumerate(numbers):
        if sum_a <= sum_b:
            list_a.append(idx if return_indices else number)
            sum_a += number
        else:
            list_b.append(idx if return_indices else number)
            sum_b += number

    return (list_a, list_b)
