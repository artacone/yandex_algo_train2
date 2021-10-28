from math import pi


if __name__ == '__main__':
    n_rects = int(input())
    r1, r2, phi1, phi2 = map(float, input().split())
    r_min = r1
    r_max = r2
    events = [(phi1, -1), (phi2, 1)]
    for i in range(2, n_rects + 1):
        r1, r2, phi1, phi2 = map(float, input().split())
        r_min = max(r_min, r1)
        r_max = min(r_max, r2)
        events.append((phi1, -i))
        events.append((phi2, i))
    events.sort()
    alpha = (r_max*r_max - r_min*r_min)/2
    rects_met = set()
    rects_count = 0
    for event in events:
        if event[1] < 0:
            rects_count += 1
            rects_met.add(-event[1])
        elif event[1] in rects_met:
            rects_count -= 1

    area = 0
    for i in range(len(events)):
        event = events[i]
        if event[1] < 0:
            rects_count += 1
        else:
            rects_count -= 1
        if rects_count == n_rects:
            if i < len(events) - 1:
                area += (events[i+1][0] - events[i][0]) * alpha
            else:
                area += (events[0][0] - events[len(events) - 1][0] + 2 * pi) * alpha
    print(area)
