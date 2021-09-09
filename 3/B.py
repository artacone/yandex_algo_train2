def occurence(nums):
    occurred = set()
    for n in nums:
        if n in occurred:
            print("YES")
        else:
            print("NO")
            occurred.add(n)


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    occurence(nums)
