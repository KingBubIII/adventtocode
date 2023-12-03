def get_ffd(myinput):
    word_digit_options = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    span = (0,0)
    while len(word_digit_options) > 0:
        if myinput[span[0]:span[1]] == word_digit_options[0]:
            return word_digit_options[0]
        
        curr_char = myinput[span[1]:span[1]+1]
        if curr_char.isnumeric():
            return curr_char
        
        span = (span[0], span[1]+1)
        word_digit_options = list( filter(lambda digit_word: str(myinput[span[0]:span[1]]) in digit_word, word_digit_options) )

    return get_ffd(myinput[span[0]+1:])

def get_fld(myinput):
    word_digit_options = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    span = (len(myinput)-1,len(myinput)-1)
    while len(word_digit_options) > 0:
        if myinput[span[0]:span[1]] == word_digit_options[0]:
            return word_digit_options[0]
        
        curr_char = myinput[span[0]-1:span[0]]
        if curr_char.isnumeric():
            return curr_char
        
        span = (span[0]-1, span[1])
        word_digit_options = list( filter(lambda digit_word: str(myinput[span[0]:span[1]]) in digit_word, word_digit_options) )

    return get_fld(myinput[:span[1]])

with open('2023\\day1_input.txt',"r") as myfile:
    all_lines = myfile.readlines()

    total = 0
    word_to_num = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

    for line in all_lines:
        digit1 = get_ffd(line)
        digit2 = get_fld(line)

        if len(digit1) > 1:
            digit1 = word_to_num[digit1]
        if len(digit2) > 1:
            digit2 = word_to_num[digit2]

        combined = digit1+digit2
        total += int(combined)

        print(combined)

    print(total)