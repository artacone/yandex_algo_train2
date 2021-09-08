def calculate_route_length(n, i, j):
    if j < i:
        i, j = j, i
    route1 = j - i - 1
    route2 = (n-j) + (i-1)
    return min(route1, route2)


assert calculate_route_length(100, 5, 6) == 0
assert calculate_route_length(10, 1, 9) == 1
assert calculate_route_length(2, 2, 1) == 0


if __name__ == '__main__':
    n, i, j = map(int, input().split())
    print(calculate_route_length(n, i, j))
