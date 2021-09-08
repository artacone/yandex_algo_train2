def is_date_unambiguous(x, y, z):
    if x > 12 or y > 12 or x == y:
        return 1
    else:
        return 0


assert is_date_unambiguous(1, 2, 2003) == 0
assert is_date_unambiguous(2, 29, 2008) == 1
assert is_date_unambiguous(1, 1, 2021) == 1


if __name__ == '__main__':
    x, y, z = map(int, input().split())
    print(is_date_unambiguous(x, y, z))
