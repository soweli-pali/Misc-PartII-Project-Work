import os

directories = ["With-Moves", "Without-Moves"]
cycles = {}
for directory_name in directories:
    cycles[directory_name] = 0
    directory = os.fsencode(directory_name)
    for filename in os.listdir(directory):
        filepath = os.path.join(directory_name, os.fsdecode(filename))
        with open(filepath, "r") as file:
            lines = file.readlines()
            n = len(lines)
            cycles[directory_name] += int(lines[n-2].split(":")[0])
    print(directory_name + ":\nCycles: " + str(cycles[directory_name]))
    
print("Summary:\nPercent reduction: " + str((-(cycles[directories[0]]/cycles[directories[1]]) + 1)*100) + "%")
