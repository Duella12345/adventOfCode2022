# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying? *
# Find top 3 elves carrying the most calories and total *

# count cals
def max_calorie_counter(filename):
    cal_list = open(filename, 'r')
    content = cal_list.readlines()
    max_calorie_count = 0
    current_calorie_count = 0

    for line in content:
        if line.strip() == '':
            if max_calorie_count < current_calorie_count:
                max_calorie_count = current_calorie_count
            current_calorie_count = 0
        else:
            current_calorie_count+= int(line.strip())

    return max_calorie_count

# count cals
def max_calorie_counter_top3(filename):
    cal_list = open(filename, 'r')
    content = cal_list.readlines()
    max_calorie_count = 0
    second_max_calorie_count = 0
    third_max_calorie_count = 0
    current_calorie_count = 0

    for line in content:
        if line.strip() == '':
            if max_calorie_count < current_calorie_count:
                third_max_calorie_count = second_max_calorie_count
                second_max_calorie_count = max_calorie_count
                max_calorie_count = current_calorie_count

            elif second_max_calorie_count < current_calorie_count:
                third_max_calorie_count = second_max_calorie_count
                second_max_calorie_count = current_calorie_count

            elif third_max_calorie_count < current_calorie_count:
                third_max_calorie_count = current_calorie_count
            current_calorie_count = 0
        else:
            current_calorie_count+= int(line.strip())

    print("max_calorie_count: " + str(max_calorie_count) + " second max calorie count: " + str(second_max_calorie_count) + " third max: " + str(third_max_calorie_count))
    return max_calorie_count + second_max_calorie_count + third_max_calorie_count


print(max_calorie_counter("day1/calorie_counting_test.txt"))
print(max_calorie_counter("day1/calorie_counting_test2.txt"))
print(max_calorie_counter("day1/calorie_counting_input.txt"))

print(max_calorie_counter_top3("day1/calorie_counting_test.txt"))
print(max_calorie_counter_top3("day1/calorie_counting_input.txt"))
