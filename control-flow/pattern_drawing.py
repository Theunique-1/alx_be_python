pattern_size = 0
while pattern_size <= 0:
    pattern_size = int("Enter the size of the pattern: ")
    i = 0
    while i < pattern_size:
        j = 0
        while j < pattern_size:
            print("*", end="")
            j += 1
        print()
        i += 1
