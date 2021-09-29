def sum_of_three(a, b, c):
    c_num_to_index = {}
    for i in range(len(c)):
        if c[i] not in c_num_to_index:
            c_num_to_index[c[i]] = i
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            ck = s - (a[i] + b[j])
            if ck in c_num_to_index:
                return i-1, j-1, c_num_to_index[ck]
    return -1


if __name__ == '__main__':
    s = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = sum_of_three(a, b, c[1:])
    if ans == -1:
        print(ans)
    else:
        print(*ans)
