def get_final(r, i, c):
    if i == 0:
        if r != 0:
            f = 3
        else:
            f = c
    elif i == 1:
        f = c
    elif i == 4:
        if r != 0:
            f = 3
        else:
            f = 4
    elif i == 6:
        f = 0
    elif i == 7:
        f = 1
    else:
        f = i
    return f


assert get_final(0, 0, 0) == 0
assert get_final(-1, 0, 1) == 3
assert get_final(42, 1, 6) == 6
assert get_final(44, 7, 4) == 1
assert get_final(1, 4, 0) == 3
assert get_final(-3, 2, 4) == 2


if __name__ == '__main__':
    r = int(input())
    i = int(input())
    c = int(input())
    print(get_final(r, i, c))
