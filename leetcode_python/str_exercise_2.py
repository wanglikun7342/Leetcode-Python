if __name__ == '__main__':
    string = "2018-11-13"
    print(string.replace("-", ""))
    string = "201812"
    print(string.count("2"))
    string = "12345678901234567890"
    for i in range(len(string)):
        print(string[i], end="")
        if (i + 1) % 4 == 0:
            print("\n")
    string = "12345678901234567890"
    column_num = 1
    last_i = 0
    for i in range(len(string)):
        print(string[i], end="")
        if (i - last_i) % column_num == 0:
            last_i = i
            column_num += 1
            print("\n")
    string = "123abcABCDE"

    print("\n")
    subline_num = 0
    digit_num = 0
    alpha_num = 0
    for ch in string:
        if ch.isdigit():
            digit_num += 1
        elif ch.isalpha():
            alpha_num += 1
        else:
            subline_num += 1
    print(subline_num)
    print(digit_num)
    print(alpha_num)
