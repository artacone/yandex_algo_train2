def find_distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def get_position(d, x, y):
    if (x >= 0) and (y >= 0) and (x + y <= d):
        return 0
    distances = [
        (find_distance((x, y), (0, 0)), 1),
        (find_distance((x, y), (d, 0)), 2),
        (find_distance((x, y), (0, d)), 3)
    ]
    return min(distances)[1]


assert get_position(5, 1, 1) == 0
assert get_position(3, -1, -1) == 1
assert get_position(4, 4, 4) == 2
assert get_position(4, 2, 2) == 0


if __name__ == '__main__':
    d = int(input())
    x, y = map(int, input().split())
    print(get_position(d, x, y))
