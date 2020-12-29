def logo():
    with open("art/logo.txt","r") as f:
        for line in f:
            print(line, end="")