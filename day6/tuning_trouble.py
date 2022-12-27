# How many characters need to be processed before the first start-of-packet marker is detected? *
def tuning_trouble(filename):
    stack = open(filename,'r')
    content = stack.read()
    start_index = 0
    end_index = 3

    while len(set(content[start_index:end_index+1])) < 4:
        start_index += 1
        end_index += 1
        
    return end_index + 1

print(tuning_trouble("day6/tuning_trouble_test1.txt")) # 5
print(tuning_trouble("day6/tuning_trouble_test2.txt")) # 6
print(tuning_trouble("day6/tuning_trouble_test3.txt")) # 10
print(tuning_trouble("day6/tuning_trouble_test4.txt")) # 11
print(tuning_trouble("day6/tuning_trouble_input.txt")) # 1598

# How many characters need to be processed before the first start-of-message marker is detected? *
def tuning_trouble_message(filename):
    stack = open(filename,'r')
    content = stack.read()
    start_index = 0
    end_index = 13

    while len(set(content[start_index:end_index+1])) < 14:
        start_index += 1
        end_index += 1
        
    return end_index + 1

print(tuning_trouble_message("day6/tuning_trouble_message_test1.txt")) # 19
print(tuning_trouble_message("day6/tuning_trouble_message_test2.txt")) # 23
print(tuning_trouble_message("day6/tuning_trouble_message_test3.txt")) # 23
print(tuning_trouble_message("day6/tuning_trouble_message_test4.txt")) # 29
print(tuning_trouble_message("day6/tuning_trouble_message_test5.txt")) # 26
print(tuning_trouble_message("day6/tuning_trouble_input.txt")) # 2414