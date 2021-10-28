def get_intersection_length(segments):
    points = []
    for s in segments:
        points.append((s[0], -1))
        points.append((s[1], 1))
    points.sort()
    length = 0
    n_intersect = 0
    curr_left = 0
    for p in points:
        if p[1] == -1:
            if n_intersect == 0:
                curr_left = p[0]
            n_intersect += 1
        else:
            n_intersect -= 1
            if n_intersect == 0:
                length += p[0] - curr_left
    return length


assert get_intersection_length([(10, 20)]) == 10
assert get_intersection_length([(10, 10)]) == 0
assert get_intersection_length([(10, 20), (20, 40)]) == 30


if __name__ == '__main__':
    n_segments = int(input())
    segments = []
    for i in range(n_segments):
        l, r = map(int, input().split())
        segments.append((l, r))
    print(get_intersection_length(segments))
