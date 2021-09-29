def get_enumed_arr():
    array = list(map(int, input().split()))
    for i in range(len(array)):
        array[i] = (array[i], i + 1)
    array.sort()
    return array


def distribure_students():
    n_groups, n_rooms = map(int, input().split())
    groups = get_enumed_arr()
    rooms = get_enumed_arr()
    rooms_iterator = 0
    groups_count = 0
    ans = [0] * (n_groups + 1)
    for n_students, group in groups:
        while rooms_iterator < n_rooms and rooms[rooms_iterator][0] < n_students + 1:
            rooms_iterator += 1
        if rooms_iterator == n_rooms:
            break
        ans[group] = rooms[rooms_iterator][1]
        rooms_iterator += 1
        groups_count += 1
    print(groups_count)
    print(*ans[1:])


if __name__ == '__main__':
    distribure_students()
