# this is lamda expression to calculate lenght of string
string_length = lambda s: len(s)

# Take input from user
if __name__ == "__main__":
    text = input("Enter a string: ")
    result = string_length(text)
    print(f"Length of '{text}': {result}")
