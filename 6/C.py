epsilon = 0.00001


def solve_equation(a, b, c, d):
    if a < 0:
        a, b, c, d = -a, -b, -c, -d
    l = -2000
    r = 2000
    while r - l > epsilon:
        m = (r + l) / 2
        if a*m*m*m + b*m*m + c*m + d > 0:
            r = m
        else:
            l = m
    return (l + r) / 2


assert abs(solve_equation(1, -3, 3, -1) - 1.0000036491) < epsilon
assert abs(solve_equation(-1, -6, -12, -7) - -1.0000000111) < epsilon


if __name__ == '__main__':
    a, b, c, d = map(float, input().split())

    print(solve_equation(a, b, c, d))
