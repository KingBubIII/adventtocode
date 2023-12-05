with open('2023/day4/day4_input.txt',"r") as myfile:
    cards = myfile.readlines()
    total = 0
    for card in cards:
        card_val = 1
        unnessessary, card_info = card.strip().split(": ")
        winning_numbers, actual_numbers = card_info.strip().replace("  "," ").split(" | ")

        winning_num_set = list(winning_numbers.split(' '))
        actual_numbers = list(actual_numbers.split(' '))
        common = list(set(winning_num_set) & set(actual_numbers))
        
        if len(common) > 0:
            card_val *= 2 ** (len(common) - 1)
        else:
            card_val = 0
        # print(common)
        print(card_val)
        total += card_val
    print(total)