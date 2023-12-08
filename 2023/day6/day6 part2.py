import re

def parse_input(filepath):
    myfile = open(filepath)
    times, distances = myfile.readlines()
    time = re.findall("[0-9]+",times.replace(" ",""))[0]
    distance = re.search("[0-9]+",distances.replace(" ",""))[0]
    race = (int(time), int(distance))
    
    return race

def find_winning_combos(time, distance):
    winning_times_held = []
    for temp_time_held in range(time):
        temp_distance = temp_time_held*(time-temp_time_held)
        if temp_distance > distance:
            winning_times_held.append(temp_time_held)

    return winning_times_held


if __name__ == "__main__":
    race = parse_input('2023\\day6\\day6_input.txt')
    error_margin = len(find_winning_combos(*race))

    print(error_margin)