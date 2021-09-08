def find_support(l, cubes):
    centre, is_odd = divmod(l, 2)
    prev = 0
    for cube in cubes:
        if cube < centre:
            prev = cube
        elif cube == centre and is_odd:
            return [cube]
        else:
            return [prev, cube]


if __name__ == '__main__':
    l, k = map(int, input().split())
    cubes = list(map(int, input().split()))
    print(' '.join(map(str, find_support(l, cubes))))
