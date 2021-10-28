def get_number_of_machines(n, t_in, t_out):
    events = []
    for i in range(n):
        events.append((t_in[i], 1))
        events.append((t_out[i], -1))
    events.sort()
    max_ships = 0
    curr_ships = 0
    for event in events:
        if event[1] == -1:
            curr_ships -= 1
        else:
            curr_ships += 1
        max_ships = max(max_ships, curr_ships)
    return max_ships


if __name__ == '__main__':
    n_ships = int(input())
    times_in = [0] * n_ships
    times_out = [0] * n_ships
    for i in range(n_ships):
        time_in, length = map(int, input().split())
        times_in[i], times_out[i] = time_in, time_in + length
    print(get_number_of_machines(n_ships, times_in, times_out))
