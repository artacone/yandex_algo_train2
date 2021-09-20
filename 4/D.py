def construct_parlament():
    parties = []
    order = 0
    total_votes = 0
    while True:
        try:
            line = input()
        except EOFError:
            break
        words = line.split()
        votes = int(words[-1])
        party = ' '.join(words[:-1])
        parties.append([party, int(votes), order])
        order += 1
        total_votes += votes
    first_number = total_votes / 450
    places_left = 450
    for party in parties:
        places, priority = divmod(party[1], first_number)
        party.append(places)
        party.append(priority)
        places_left -= places
    parties.sort(key=lambda x: x[4], reverse=True)
    for i in range(int(places_left)):
        parties[i][3] += 1
    parties.sort(key=lambda x: x[2])
    for party in parties:
        print(party[0], int(party[3]))


if __name__ == '__main__':
    construct_parlament()
