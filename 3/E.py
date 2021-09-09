def ask_witness(witness_n):
    testimonies = []
    for _ in range(witness_n):
        s = input()
        testimonies.append(set(s))
    return testimonies


def check_numbers(suspects, testimonies, cars_n):
    max_test = 0
    count_suspects = dict.fromkeys(suspects, 0)
    for s in count_suspects:
        ss = set(s)
        for t in testimonies:
            if t.issubset(ss):
                count_suspects[s] += 1
        if count_suspects[s] > max_test:
            max_test = count_suspects[s]

    suspicious_suspects = []
    for s in suspects:
        if count_suspects[s] == max_test:
            suspicious_suspects.append(s)
    return suspicious_suspects


def print_suspects(suspects):
    for s in suspects:
        print(s)


if __name__ == '__main__':
    witness_n = int(input())
    testimonies = ask_witness(witness_n)

    cars_n = int(input())
    suspects = []
    for _ in range(cars_n):
        s = input()
        suspects.append(s)

    suspicious_suspects = check_numbers(suspects, testimonies, cars_n)
    print_suspects(suspicious_suspects)
