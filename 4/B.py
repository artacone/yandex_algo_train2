def count_votes():
    import sys
    votes = {}
    for line in sys.stdin:
        if line == '\n':
            break
        name, num = line.split()
        if name not in votes:
            votes[name] = 0
        votes[name] += int(num)
    for name, num in sorted(votes.items()):
        print(f'{name} {num}')


if __name__ == '__main__':
    count_votes()
