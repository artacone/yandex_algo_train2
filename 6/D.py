def count_trees_timbered(timber1_prod, timber1_dayoff, timber2_prod, timber2_dayoff, days):

    return timber1_prod * (days - days // timber1_dayoff) + timber2_prod * (days - days // timber2_dayoff)


def count_days_to_work(timber1_prod, timber1_dayoff, timber2_prod, timber2_dayoff, num_trees):
    left = 0
    right = 2 * num_trees
    while left < right:
        middle = (left + right) // 2
        if count_trees_timbered(timber1_prod, timber1_dayoff, timber2_prod, timber2_dayoff, middle) >= num_trees:
            right = middle
        else:
            left = middle + 1
    return left


assert count_days_to_work(1, 2, 1, 3, 10) == 8
assert count_days_to_work(1, 2, 1, 3, 11) == 9
assert count_days_to_work(19, 3, 14, 6, 113) == 4


if __name__ == '__main__':
    a, k, b, m, x = map(int, input().split())
    print(count_days_to_work(a, k, b, m, x))
