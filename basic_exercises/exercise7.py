#return count of a given substring from a string
#program to count how many times substring Emma appears in the given string

def count_substring_appearance():
    x = "Emma is good developer. Emma is a writer"
    substr = "Emma"

    count = x.count(substr)

    print(substr, "appeared", count, "times")

if __name__ == "__main__":
    count_substring_appearance()