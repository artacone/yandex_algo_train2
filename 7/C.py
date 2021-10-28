def find_min_cover(m, segments):
    segments.sort()
    cover = []
    curr_right = 0
    next_right = 0
    curr_best = 0, 0
    for (left, right) in segments:
        if left > curr_right:
            cover.append(curr_best)
            curr_right = next_right
            if curr_right >= m:
                break
        if left <= curr_right and right > next_right:
            next_right = right
            curr_best = (left, right)

    if curr_right < m:
        curr_right = next_right
        cover.append(curr_best)
    if curr_right < m:
        return None
    return cover


if __name__ == '__main__':
    m = int(input())
    segments = []
    while True:
        l, r = map(int, input().split())
        if l == 0 and r == 0:
            break
        if r > 0 and l < m:
            segments.append((l, r))
    cover = find_min_cover(m, segments)
    if not cover:
        print("No solution")
    else:
        print(len(cover))
        for segment in cover:
            print(*segment)
