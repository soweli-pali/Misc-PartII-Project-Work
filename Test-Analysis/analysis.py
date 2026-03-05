import os

directories = ["With-Moves", "Without-Moves"]
cycles = {}
file_counts = {}
for directory_name in directories:
    cycles[directory_name] = 0
    file_counts[directory_name] = 0
    directory = os.fsencode(directory_name)
    for filename in os.listdir(directory):
        filepath = os.path.join(directory_name, os.fsdecode(filename))
        with open(filepath, "r") as file:
            file_counts[directory_name] += 1
            lines = file.readlines()
            n = len(lines)
            cycles[directory_name] += int(lines[n-2].split(":")[0])
    print(directory_name + ":")
    print("File count: " + str(file_counts[directory_name]))
    print("Total Cycles: " + str(cycles[directory_name]))
    
print("Summary:\nPercent reduction: " + str((-(cycles[directories[0]]/cycles[directories[1]]) + 1)*100) + "%")
