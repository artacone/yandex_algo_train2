def calculate_fullness(cats, segment):
    left = 0
    right = len(cats) - 1
    while left < right:
        middle = (left + right) // 2
        if cats[middle] >= segment[0]:
            right = middle
        else:
            left = middle + 1
    left_cat = left

    left = 0
    right = len(cats) - 1
    while left < right:
        middle = (left + right + 1) // 2
        if cats[middle] <= segment[1]:
            left = middle
        else:
            right = middle - 1
    right_cat = left
    if right_cat == left_cat:
        if not segment[0] <= cats[right_cat] <= segment[1]:
            return 0
    return right_cat - left_cat + 1


if __name__ == '__main__':
    n_cats, m_segments = map(int, input().split())
    cats = sorted(list(map(int, input().split())))
    segments = []
    for i in range(m_segments):
        l, r = map(int, input().split())
        segments.append((l, r))
    for segment in segments:
        print(calculate_fullness(cats, segment))
