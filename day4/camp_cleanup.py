import re

# In how many assignment pairs does one range fully contain the other? *
def camp_cleanup_overlaps(filename):
    cleanup_list = open(filename, 'r')
    content = cleanup_list.readlines()
    overlaps = 0

    # a-b,c-d
    for line in content:
        pattern = r'\W+'
        areas = re.split(pattern,line.strip())

        if (((int(areas[0]) <= int(areas[2])) and (int(areas[1]) >= int(areas[3]))) or 
        ((int(areas[0]) >= int(areas[2])) and (int(areas[1]) <= int(areas[3])))):
            overlaps += 1

    return overlaps

# print(camp_cleanup_overlaps("day4/camp_cleanup_test.txt")) # 2
# print(camp_cleanup_overlaps("day4/camp_cleanup_test2.txt")) # 2
# print(camp_cleanup_overlaps("day4/camp_cleanup_test3.txt")) # 5
# print(camp_cleanup_overlaps("day4/camp_cleanup_input.txt")) # 588

# In how many assignment pairs do the ranges overlap?
def camp_cleanup_overlaps_any(filename):
    cleanup_list = open(filename, 'r')
    content = cleanup_list.readlines()
    overlaps = 0

    # a-b,c-d
    for line in content:
        pattern = r'\W+'
        areas = re.split(pattern,line.strip())
        a = int(areas[0])
        b = int(areas[1])
        c = int(areas[2])
        d = int(areas[3])

        if (((a >= c) and (a <= d)) or ((b >= c) and (b <= d))):
            overlaps += 1
        elif (((c >= a) and (c <= b)) or ((d >= a) and (d <= b))):
            overlaps += 1

    return overlaps

print(camp_cleanup_overlaps("day4/camp_cleanup_test.txt")) # 2
print(camp_cleanup_overlaps_any("day4/camp_cleanup_test4.txt")) # 5
print(camp_cleanup_overlaps_any("day4/camp_cleanup_test5.txt")) # 9
print(camp_cleanup_overlaps_any("day4/camp_cleanup_input.txt")) # 911