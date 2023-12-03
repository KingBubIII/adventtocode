with open('2023\\day2_input.txt',"r") as myfile:
    all_lines = myfile.readlines()

    total_ids = 0
    thresholds = (12, 13, 14)
    for game in all_lines:
        game_id, handfuls = game.strip().split(": ")
        game_id = int(game_id.replace("Game ",""))
        handfuls = handfuls.split("; ")
        game_amounts = []
        for handful in handfuls:
            grouping = handful.split(", ")
            temp_amounts = [0,0,0]
            for group in grouping:
                amount, color = group.split(" ")
                match color:
                    case "red":
                        temp_amounts[0] += int(amount)
                    case "green":
                        temp_amounts[1] += int(amount)
                    case "blue":
                        temp_amounts[2] += int(amount)
            game_amounts.append(temp_amounts)
        possible = True
        for round_amount in game_amounts:
            for i in range(3):
                if round_amount[i] > thresholds[i]:
                    possible=False
                    break
        if possible:
            total_ids += game_id
            print(game_id)
    print(total_ids)