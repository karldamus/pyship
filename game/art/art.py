ART_DIRECTORY = "game/art/"

def logo():
    with open(ART_DIRECTORY + "logo.txt","r") as f:
        for line in f:
            print(line, end="")