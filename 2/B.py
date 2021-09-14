def find_furthest(street):
    dist_left_shops = [0] * len(street)
    shop_pos = -20
    for i in range(len(street)):
        if street[i] == 2:
            shop_pos = i
        elif street[i] == 1:
            dist_left_shops[i] = i - shop_pos
    furthest = 0
    shop_pos = 30
    for i in range(len(street) - 1, -1, -1):
        if street[i] == 2:
            shop_pos = i
        elif street[i] == 1:
            min_dist = min(shop_pos - i, dist_left_shops[i])
            furthest = max(min_dist, furthest)
    return furthest


assert find_furthest([2, 0, 1, 1, 0, 1, 0, 2, 1, 2]) == 3


if __name__ == '__main__':
    street = list(map(int, input().split()))
    print(find_furthest(street))
