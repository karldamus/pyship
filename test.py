# Pyship ©2020 Karl Damus, All Rights Reserved
# test.py

def main():
    display_grid()

def display_grid():
    positions = [(2,2)]
    size = 6 + 2
    outer_grid_list = []

    for i in range(size):
        inner_grid_list = []
        if (i == 0) or (i == size - 1):
            for j in range(size):
                inner_grid_list.append("#")
        else:
            for j in range(size):
                if (j == 0) or (j == size - 1): 
                    inner_grid_list.append("#")
                else:
                    inner_grid_list.append(" ")
        outer_grid_list.append(inner_grid_list)

    for marker in positions:
        x_coord = marker[0]
        y_coord = marker[1]
        if (x_coord == 0) or (x_coord == (size - 1)) or (y_coord == 0) or (y_coord == (size - 1)):
            print("\n\tYou have a faulty coordinate. Please refer to line 25 of test.py\n") 
        else:
            outer_grid_list[y_coord][x_coord] = "="

    for v in outer_grid_list:
        for w in v:
            print(w, end="  ")
        print("")

# # #

if __name__ == "__main__":
    main()