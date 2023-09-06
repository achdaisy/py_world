#printing a partner that looks like a staircase

def staircase_pattern():
    rows = 9

    for i in range(1, rows):
        for j in range(i):
            print(i, end="")
        print()




if __name__ == "__main__":
    staircase_pattern()