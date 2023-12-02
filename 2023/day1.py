with open('day1_input.txt',"r") as myfile:
    all_lines = myfile.readlines()

    total = 0
    digit_words = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

    for line in all_lines:
        digit1 = 0
        digit2 = len(line)-1
        while not line[digit1].isnumeric() or not line[digit2].isnumeric():
            if not line[digit1].isnumeric():
                digit1 += 1

            if not line[digit2].isnumeric():
                digit2 -= 1
        print(line[digit1] + line[digit2])
        total += int(line[digit1] + line[digit2])

    print(total)