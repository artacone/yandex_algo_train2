def get_diff_to_palindrom(s):
    diff = 0
    for i in range(len(s) // 2):
        if s[i] != s[-1 - i]:
            diff += 1
    return diff


assert get_diff_to_palindrom("a") == 0
assert get_diff_to_palindrom("ab") == 1
assert get_diff_to_palindrom("cognitive") == 4


if __name__ == '__main__':
    s = input()
    print(get_diff_to_palindrom(s))
