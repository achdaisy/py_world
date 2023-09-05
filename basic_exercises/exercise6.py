#Display numbers divisible by 5 from a list

#iterate the given list of numbers and print only those numbers divisible by 5

def divisibility_by_5():
    x = [10, 20, 33, 46, 55]

    index = 0
    xlen = len(x)

    while index < xlen:
        div = x[index] % 5
        if div == 0:
            print(x[index])
        index += 1


if __name__ == "__main__":
    divisibility_by_5()
