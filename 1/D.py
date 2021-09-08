def build_school(n, houses):
    return houses[n // 2]


if __name__ == '__main__':
    n = int(input())
    houses = list(map(int, input().split()))
    print(build_school(n, houses))
