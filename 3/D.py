def guess_number(max_n):
    ans = set(range(1, max_n + 1))
    while True:
        s = input()
        if s == "HELP":
            break
        guess = set(map(int, s.split()))
        s = input()
        if s == "YES":
            ans.intersection_update(guess)
        else:
            ans.difference_update(guess)
    return ans


def help_beatrice(max_n):
    ans = sorted(list(guess_number(max_n)))
    for n in ans:
        print(n, end=' ')
    print()


if __name__ == '__main__':
    max_n = int(input())
    help_beatrice(max_n)
