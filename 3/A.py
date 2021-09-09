def count_duplicates(list1, list2):
    return len(set(list1).intersection(set(list2)))


assert count_duplicates([1, 3, 2], [4, 3, 2]) == 2
assert count_duplicates([1, 2, 6, 4, 5, 7], [10, 2, 3, 4, 8]) == 2
assert count_duplicates([1, 7, 3, 8, 10, 2, 5], [6, 5, 2, 8, 4, 3, 7]) == 5


if __name__ == '__main__':
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    print(count_duplicates(list1, list2))
