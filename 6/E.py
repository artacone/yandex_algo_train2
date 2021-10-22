def is_covered(points, length_segments, num_segments):
    count_segments = 0
    covered_till = points[0] - 1
    for x in points:
        if x > covered_till:
            count_segments += 1
            covered_till = x + length_segments
    return count_segments <= num_segments


def find_min_segment(num_segments, points):
    begin = 0
    end = points[-1] - points[0]
    while begin < end:
        middle = (begin + end) // 2
        if is_covered(points, middle, num_segments):
            end = middle
        else:
            begin = middle + 1
    return begin


assert find_min_segment(2, [1, 2, 3, 7, 8, 9]) == 2


if __name__ == '__main__':
    num_points, num_segments = map(int, input().split())
    points = sorted(list(map(int, input().split())))
    print(find_min_segment(num_segments, points))
