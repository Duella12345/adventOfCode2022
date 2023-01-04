# To begin, find all of the directories with a total size of at most 100000,
#  then calculate the sum of their total sizes. 
# In the example above, these directories are a and e;
#  the sum of their total sizes is 95437 (94853 + 584).
#  (As in this example, this process can count files more than once!)
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = {}

    def add_child(self, name, child):
        self.children[name] = child


def make_space(filename):
    stack = open(filename,'r')
    content = stack.readlines()
    current_dir = []
    folders = dict()
    total_size = 0

    for line in content:
        if line.find("$") != -1:
            if line.find("cd") != -1 and line.find("..") == -1:
                current_dir = current_dir + [line[5:len(line)-1]]
                if line[5:len(line)-1] not in folders.keys():
                    folders[line[5:len(line)-1]] = 0

                print(current_dir)

            elif line.find("cd") != -1 and line.find("..") != -1:
                current_dir = current_dir[0:len(current_dir)-1]
                print(current_dir)

        else:
            if line.find("dir") == -1:
                memory = int(line.split()[0])
                for folder in current_dir:
                    folders[folder] += memory
                print(folders)
    
    for folder in folders.values():
        if folder <= 100000:
            total_size += folder

    return total_size



print(make_space("day7/test.txt")) # 95437
print(make_space("day7/input.txt")) # 1160318 too low