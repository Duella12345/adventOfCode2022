import re
# final letters at the top of each stack x
def supply_stack(filename, cols):
    stack = open(filename,'r')
    content = stack.readlines()
    stacks = []
    for x in range(cols):
        stacks.append([])

    moves = False
    for line in content:
        line = line.replace('[','').replace(']','').replace('    ', ' x ')
        pattern = r'\s+'
        line = re.split(pattern, line)
        if (line[0] == ''):
            line = line[1:]
        if (line[len(line)-1] == ''):
            line = line[0:len(line)-1]
        if len(line) == 0:
            moves = True
        if not moves:
            for x in range(cols):
                if line[x] != 'x' and str(line[x]).isalpha():
                    stacks[x] = [line[x]] + stacks[x]
        
        if moves and  8 > len(line) > 5:
            for x in range(int(line[1])):
                stacks[int(line[5])-1].append(stacks[int(line[3])-1].pop())

    result = ""
    for x in range(len(stacks)):
         result += stacks[x].pop()
    return result

#print(supply_stack("day5/supply_stack_test.txt", 3)) # CMZ
#print(supply_stack("day5/supply_stack_input.txt", 9)) #DHBJQJCCW

# final letters at the top of each stack boxes stay in order x
def supply_stack_v2(filename, cols):
    stack = open(filename,'r')
    content = stack.readlines()
    stacks = []
    for x in range(cols):
        stacks.append([])

    moves = False
    for line in content:
        line = line.replace('[','').replace(']','').replace('    ', ' x ')
        pattern = r'\s+'
        line = re.split(pattern, line)
        if (line[0] == ''):
            line = line[1:]
        if (line[len(line)-1] == ''):
            line = line[0:len(line)-1]
        if len(line) == 0:
            moves = True
        if not moves:
            for x in range(cols):
                if line[x] != 'x' and str(line[x]).isalpha():
                    stacks[x] = [line[x]] + stacks[x]
        
        if moves and  8 > len(line) > 5:
            first_stack_length = len(stacks[int(line[3])-1])
            number_boxes = int(line[1])

            stacks[int(line[5])-1] = stacks[int(line[5])-1] + stacks[int(line[3])-1][first_stack_length-number_boxes:first_stack_length]
            stacks[int(line[3])-1] = stacks[int(line[3])-1][0:first_stack_length-number_boxes]

    result = ""
    for x in range(len(stacks)):
        if len(stacks[x]) != 0:
            result += stacks[x].pop()
    return result

#print(supply_stack_v2("day5/supply_stack_test.txt", 3)) # MCD
print(supply_stack_v2("day5/supply_stack_input.txt", 9)) #