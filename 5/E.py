# В надежде, что прошлое решение TLилось из-за большой константы хэштаблиц,
# переписал код как в разборе. Стало работать еще медленнее.
# Так что я просто сдал тот же алгоритм, но написанный на Go

def get_enumed_arr():
    array = list(map(int, input().split()))[1:]
    for i in range(len(array)):
        array[i] = array[i], i
    return array


if __name__ == '__main__':
    s = int(input())
    a = get_enumed_arr()
    b = get_enumed_arr()
    c = get_enumed_arr()
    a.sort()
    b.sort()
    c.sort(key=lambda x: (x[0], -x[1]))
    is_first = True
    sum_of_three = 0
    for a_val, a_pos in a:
        c_iter = len(c) - 1
        for b_val, b_pos in b:
            while c_iter > 0 and a_val + b_val + c[c_iter][0] > s:
                c_iter -= 1
            if a_val + b_val + c[c_iter][0] == s and (is_first or (a_pos, b_pos, c_iter) < ans):
                ans = a_pos, b_pos, c[c_iter][1]
                is_first = False
    if not is_first:
        print(*ans)
    else:
        print(-1)
