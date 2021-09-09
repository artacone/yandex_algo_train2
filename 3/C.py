def get_unique(nums):
    occurences = {}
    unique = []
    for n in nums:
        if n in occurences:
            occurences[n] += 1
        else:
            occurences[n] = 1
    for n, count in occurences.items():
        if count == 1:
            unique.append(n)
    return unique

def print_unique(nums):
    unique = get_unique(nums)
    for n in unique:
        print(n, end=' ')
    print()


assert get_unique([1, 2, 2, 3, 3, 3]) == [1]
assert get_unique([4, 3, 5, 2, 5, 1, 3, 5]) == [4, 2, 1]


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print_unique(nums)
