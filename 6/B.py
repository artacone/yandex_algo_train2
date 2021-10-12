def get_entry_segment(nums, n):
    begin = 0
    end = len(nums) - 1
    while begin < end:
        middle = (begin + end) // 2
        if nums[middle] >= n:
            end = middle
        else:
            begin = middle + 1
    left = begin
    begin = 0
    end = len(nums) - 1
    while begin < end:
        middle = (begin + end + 1) // 2
        if nums[middle] <= n:
            begin = middle
        else:
            end = middle - 1
    right = begin
    if nums[left] != n:
        return 0, 0
    return left+1, right+1


assert get_entry_segment([1, 2, 2, 3], 3) == (4, 4)
assert get_entry_segment([1, 2, 2, 3], 2) == (2, 3)
assert get_entry_segment([1, 2, 2, 3], 1) == (1, 1)
assert get_entry_segment([1, 2, 2, 3], 4) == (0, 0)


if __name__ == '__main__':
    nums_size = int(input())
    nums = list(map(int, input().split()))
    n_queries = int(input())
    queries = list(map(int, input().split()))
    for q in queries:
        print(*get_entry_segment(nums, q))
