# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types? *
def rucksack_reorganisation(filename):
    pack_list = open(filename, 'r')
    content = pack_list.readlines()
    pack_sum = 0

    for line in content:
        # print(int(len(line)/2))
        compartment_a = set(line[0:int(len(line)/2)])
        compartment_b = set(line[int(len(line)/2):int(len(line))])
        # print(compartment_a)
        # print(compartment_b)
        item = compartment_a.intersection(compartment_b).pop()
        # print(item)

        if item.islower():
            pack_sum += ord(item)-96
        else:
            pack_sum += ord(item)-38

    return pack_sum

    # print(ord('a')-96)
    # print(ord('z')-96)
    # print(ord('A')-38)
    # print(ord('Z')-38)

print(rucksack_reorganisation("day3/rucksack_reorg_test.txt")) # 157
print(rucksack_reorganisation("day3/rucksack_reorg_input.txt")) # 8018

# part 2 *
def rucksack_reorganisation_threes(filename):
    pack_list = open(filename, 'r')
    content = pack_list.readlines()
    pack_sum = 0
    line_number = 1
    items = set()

    for line in content:
        line = str(line.strip())
        if len(items) == 0:
            items = set(line)
        elif line_number%3 == 0:
            items = items.intersection(set(line))
            item = items.pop()
            # print(item)
            if item.islower():
                pack_sum += ord(item)-96
            else:
                pack_sum += ord(item)-38
            items = set()
        else:
            items = items.intersection(set(line))
        line_number += 1

    return pack_sum

print(rucksack_reorganisation_threes("day3/rucksack_reorg_test.txt")) # 70
print(rucksack_reorganisation_threes("day3/rucksack_reorg_input.txt")) # 2518
