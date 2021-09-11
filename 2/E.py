def get_min_time(folders):
    return sum(folders) - max(folders)


assert get_min_time([2, 1]) == 1


if __name__ == '__main__':
    n_folders = int(input())
    folders = list(map(int, input().split()))
    print(get_min_time(folders))
