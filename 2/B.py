def find_furthest(street):
    markets = [i for i, b in enumerate(street) if b == 2]
    min_dists = []
    for i, b in enumerate(street):
        if b == 1:
            min_dists.append(min([abs(j - i) for j in markets]))
    return max(min_dists)


assert find_furthest([2, 0, 1, 1, 0, 1, 0, 2, 1, 2]) == 3


if __name__ == '__main__':
    street = list(map(int, input().split()))
    print(find_furthest(street))
