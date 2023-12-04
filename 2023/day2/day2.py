with open('2023\\day2\\day2_input.txt',"r") as myfile:
    all_lines = myfile.readlines()

    total_score = 0
    for game in all_lines:
        game_id, handfuls = game.strip().split(": ")
        game_id = int(game_id.replace("Game ",""))
        handfuls = handfuls.split("; ")
        game_amounts = []
        minimum_cube_counts = [0,0,0]
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
                if round_amount[i] > minimum_cube_counts[i]:
                    minimum_cube_counts[i] = round_amount[i]
        score = 1
        for i in range(3):
            score *= minimum_cube_counts[i]
        print(score)
        total_score += score
    print(total_score)