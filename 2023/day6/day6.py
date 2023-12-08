import re

def parse_input(filepath):
    myfile = open(filepath)
    times, distances = myfile.readlines()
    times = re.findall("[0-9]+",times)
    distances = re.findall("[0-9]+",distances)
    races = []
    for index in range(len(times)):
        races.append((int(times[index]), int(distances[index])))
    
    return races

def find_winning_combos(time, distance):
    winning_times_held = []
    for temp_time_held in range(time):
        temp_distance = temp_time_held*(time-temp_time_held)
        if temp_distance > distance:
            winning_times_held.append(temp_time_held)

    return winning_times_held


if __name__ == "__main__":
    races = parse_input('2023\\day6\\day6_input.txt')
    error_margin = 1
    for race in races:
        combos = find_winning_combos(*race)
        error_margin *= len(combos)

    print(error_margin)