def is_valid_bracket_sequence(s):
    count = 0
    for b in s:
        if b == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return "NO"
    if count == 0:
        return "YES"
    else:
        return "NO"


assert is_valid_bracket_sequence("(())()") == "YES"
assert is_valid_bracket_sequence("(()))()") == "NO"


if __name__ == '__main__':
    s = input()
    print(is_valid_bracket_sequence(s))
