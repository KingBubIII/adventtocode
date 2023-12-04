import re

def find_gears(schematic):
    gears = []
    for line in range(len(schematic)):
        for index in range(len(schematic[line])):
            if schematic[line][index] == "*":
                gears.append((line,index))
    return gears

def get_gear_parts(schematic, line, index):
    parts = []
    for row in range(line-1,line+2):
        # num_of_parts = re.findall("[0-9]+",schematic[row][index-1:index+2])
        left, right = index-1,index+1
        
        while schematic[row][left].isnumeric() or  schematic[row][right].isnumeric():
            if schematic[row][left].isnumeric():
                left-=1
            if schematic[row][right].isnumeric():
                right+=1
        if schematic[row][index].isnumeric():
            parts.append(schematic[row][left+1:right])
        else:
            left_part = schematic[row][left+1:index]
            right_part = schematic[row][index+1:right]
            if len(left_part) > 0:
                parts.append(left_part)
            if len(right_part) > 0:
                parts.append(right_part)
    return parts

with open('2023\\day3\\day3_input.txt',"r") as myfile:
    total_gear_ratios = 0
    schematic = myfile.readlines()

    gears = find_gears(schematic)
    for gear in gears:
        gear_parts = get_gear_parts(schematic, *gear)
        
        if len(gear_parts) == 2:
            gear_ratio = int(gear_parts[0])*int(gear_parts[1])
            print(gear_ratio)
            total_gear_ratios += gear_ratio
    print(total_gear_ratios)