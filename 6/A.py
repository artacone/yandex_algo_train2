def get_segment_size(nums, left, right):
    begin = 0
    end = len(nums) - 1
    while begin < end:
        middle = (begin + end + 1) // 2
        if nums[middle] <= right:
            begin = middle
        else:
            end = middle - 1
    segment_size = begin
    begin = 0
    end = len(nums) - 1
    while begin < end:
        middle = (begin + end) // 2
        if nums[middle] >= left:
            end = middle
        else:
            begin = middle + 1
    segment_size -= begin
    if segment_size == 0:
        if not left <= nums[begin] <= right:
            return 0
    return segment_size + 1


assert get_segment_size([1], 1, 1) == 1
assert get_segment_size([1], -1, 2) == 1
assert get_segment_size([1], 0, 1) == 1
assert get_segment_size([1], 1, 2) == 1
assert get_segment_size([1], -1, 0) == 0
assert get_segment_size([1], 2, 2) == 0
assert get_segment_size([1, 3, 4, 10, 10], 1, 10) == 5
assert get_segment_size([1, 3, 4, 10, 10], 2, 9) == 2
assert get_segment_size([1, 3, 4, 10, 10], 3, 4) == 2
assert get_segment_size([1, 3, 4, 10, 10], 2, 2) == 0
assert get_segment_size([1, 3, 4, 10, 10], 3, 3) == 1
assert get_segment_size([1, 3, 4, 10, 10], 10, 10) == 2
assert get_segment_size([-10, 0, 10], -10, -10) == 1
assert get_segment_size([-10, 0, 10], 10, 10) == 1
assert get_segment_size([-10, 0, 10], -10, 10) == 3
assert get_segment_size([-10, 0, 10], -9, 9) == 1
assert get_segment_size([-10, 0, 10], -9, 10) == 2
assert get_segment_size([-10, 0, 10], -10, 9) == 2
assert get_segment_size([-10, 0, 10], 0, 9) == 1
assert get_segment_size([-10, 0, 10], -1, 9) == 1
assert get_segment_size([-10, 0, 10], 1, 9) == 0
assert get_segment_size([-10, 0, 10], -9, -1) == 0
assert get_segment_size([-10, 0, 10], -9, 1) == 1


if __name__ == '__main__':
    nums_size = int(input())
    nums = sorted(list(map(int, input().split())))
    n_queries = int(input())
    ans = [0] * n_queries
    for i in range(n_queries):
        left, right = map(int, input().split())
        ans[i] = get_segment_size(nums, left, right)
    print(*ans)
