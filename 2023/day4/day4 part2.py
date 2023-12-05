import re

with open('2023/day4/day4_input.txt',"r") as myfile:
    cards = myfile.readlines()
    total_amt_of_cards = {}
    
    for i in range(1,len(cards)+1):
        total_amt_of_cards[i] = 1
    
    for card in cards:
        card_num, card_info = card.strip().split(": ")
        card_num = int(re.findall("[0-9]+",card)[0])
        
        winning_numbers, actual_numbers = card_info.split(" | ")

        winning_numbers = re.findall("[0-9]+", winning_numbers)
        actual_numbers = re.findall("[0-9]+", actual_numbers)
        common = list(set(winning_numbers) & set(actual_numbers))
        
        for shifted in range(card_num+1, card_num+len(common)+1):
            total_amt_of_cards[shifted] += total_amt_of_cards[card_num]
    
    total_cards_with_copies = 0
    for key, value in total_amt_of_cards.items():
        total_cards_with_copies += value

    print(total_cards_with_copies)