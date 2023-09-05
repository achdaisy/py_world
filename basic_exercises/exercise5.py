#check if the first and last number of a list is the same

#returns true if the first and last number are the same otherwise false

def compare():
    x = [10, 20, 30, 40, 10]
    y = [75, 65, 35, 75, 30]

    index = 0
    last_index_x = (len(x) - 1)
    last_index_y = (len(y) - 1)

    if (x[index] == x[last_index_x]):
        print("Given list [10, 20, 30, 40, 10]")
        print("result is true")
    else:
        print("result is false")

    if (y[index] == y[last_index_y]):
        print("numbers_y = [75, 65, 35, 75, 30]")
        print("result is true")
    else:
        print("y = [75, 65, 35, 75, 30]")
        print("result is false")
        
    
if __name__ == "__main__":
    compare()