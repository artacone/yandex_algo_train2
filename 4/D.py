def get_votes_by_party():
    votes_by_party = {}
    while True:
        try:
            line = input()
        except EOFError:
            break
        party, votes = line.split()
        if party not in votes_by_party:
            votes_by_party[party] = 0
        votes_by_party[party] += int(votes)
    return votes_by_party


def construct_parlament():
    votes_by_party = get_votes_by_party()
    total_votes = sum(votes_by_party.values())
    first_number, places_left = divmod(total_votes, 450)

    places_by_party = []
    for party in votes_by_party:
        places_by_party.append([party, first_number])

    while places_left > 0:

        places_left -= 1




if __name__ == '__main__':
    construct_parlament()
