def print_sum_by_color(n_boxes):
    colors = {}
    for _ in range(n_boxes):
        color, num = map(int, input().split())
        if color not in colors:
            colors[color] = 0
        colors[color] += num
    for color, sum in sorted(colors.items()):
        print(f'{color} {sum}')


if __name__ == '__main__':
    n_boxes = int(input())
    print_sum_by_color(n_boxes)
