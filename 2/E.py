def get_min_time(folders):
    total_diplomas = 0
    min_folder = 0
    for folder in folders:
        total_diplomas += folder
        if folder > min_folder:
            min_folder = folder
    return total_diplomas - min_folder


assert get_min_time([2, 1]) == 1


if __name__ == '__main__':
    n_folders = int(input())
    folders = list(map(int, input().split()))
    print(get_min_time(folders))
