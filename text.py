with open("BANGLORE.txt" , "r") as file:
    data = file.readlines()
    for line in data:
        print(line)
        word = line.split()
        print(word)
