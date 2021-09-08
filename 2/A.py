def count_max():
    current_max = int(input())
    count = 1
    while True:
        n = int(input())
        if n == 0:
            break
        if n > current_max:
            current_max = n
            count = 1
        elif n == current_max:
            count += 1
    return count


if __name__ == '__main__':
    print(count_max())
