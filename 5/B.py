def find_max_sub_array(nums, nums_size):
    sums = [0] * nums_size
    max_sum = sums[0] = nums[0]
    for i in range(nums_size):
        sums[i] = max(nums[i], sums[i-1] + nums[i])
        max_sum = max(max_sum, sums[i])
    return max_sum


assert find_max_sub_array([1, 2, 3, 4], 4) == 10
assert find_max_sub_array([5, 4, -10, 4], 4) == 9


if __name__ == '__main__':
    nums_size = int(input())
    nums = list(map(int, input().split()))
    print(find_max_sub_array(nums, nums_size))
