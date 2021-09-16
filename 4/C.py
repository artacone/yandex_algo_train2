def sort_by_frequency():
    words = {}
    while True:
        try:
            line = input()
        except EOFError:
            break
        words_in_line = line.split()
        for word in words_in_line:
            if word not in words:
                words[word] = 0
            words[word] += 1
    words_sorted = sorted(sorted(words.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
    for w in words_sorted:
        print(w[0])


if __name__ == '__main__':
    sort_by_frequency()
