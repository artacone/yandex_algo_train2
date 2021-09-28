def get_prefix_sums(nums, nums_size):
    prefix_sums = [0] * (nums_size + 1)
    for i in range(1, nums_size + 1):
        prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
    return prefix_sums


def answer_queries(nums, nums_size, n_queries):
    prefix_sums = get_prefix_sums(nums, nums_size)

    for i in range(n_queries):
        left, right = map(int, input().split())
        print(prefix_sums[right] - prefix_sums[left-1])


if __name__ == '__main__':
    nums_size, n_queries = map(int, input().split())
    nums = list(map(int, input().split()))
    answer_queries(nums, nums_size, n_queries)
