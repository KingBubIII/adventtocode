import re

with open('2023\\day3\\day3_input.txt',"r") as myfile:
    total = 0
    schematic = myfile.readlines()

    for line in range(len(schematic)):
        span = [None,None]

        for index in range(len(schematic[line])):
            if schematic[line][index].isnumeric() and span[0] is None:
                span[0] = index
            elif ( not schematic[line][index].isnumeric() ) and ( not span[0] is None ):
                span[1] = index
                added = False

                for curr_line in range(line-1,line+2):
                    if not (curr_line < 0) and (not added):
                        if span[0]-1 < 0:
                            left = 0
                        else:
                            left = span[0]-1

                        if span[1]+1 >= len(schematic[curr_line]):
                            right = len(schematic[curr_line])-1
                        else:
                            right = span[1]+1
                        sub_line = schematic[curr_line][left:right]
                        if re.search("[/$&+,:;=?@#|'<>^*()%!-]",sub_line):
                            total += int(schematic[line][span[0]:span[1]])
                            with open('2023\\day3\\added_values.txt','a') as out:
                                out.write(schematic[line][span[0]:span[1]] + "\n")
                            added = True
                span = [None, None]

    print(total)