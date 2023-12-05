with open('2023/day4/day4_input.txt',"r") as myfile:
    cards = myfile.readlines()
    total = 0
    for card in cards:
        unnessessary, card_info = card.strip().split(": ")
        winning_numbers, actual_numbers = card_info.strip().split(" | ")

        winning_num_set = set(winning_numbers.split(' '))
        actual_numbers = set(actual_numbers.split(' '))
        card_val = 0
        for number in actual_numbers:
            if number in winning_num_set:
                if card_val == 0:
                    card_val += 1
                else:
                    card_val *= 2
                
        print(card_val)
        total += card_val
    print(total)