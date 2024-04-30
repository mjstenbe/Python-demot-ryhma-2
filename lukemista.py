etsittava = input("Anna etsittävä sana:")

with open("example.txt") as new_file:
    count = 0
    total_length = 0
    for line in new_file:
        line = line.replace("\n", "")
        count += 1
        # if (line == etsittava):
        if line.find(etsittava) >= 0:
            print("Line", count, line, line.find(etsittava))
        length = len(line)
        total_length += length
    print("Total length of lines:", total_length)