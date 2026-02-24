import random
def random_numbers():
    
    for _ in range(5):
        yield random.randint(1, 100)  # return the value of the function without ending it.

if __name__ == "__main__":
    print("5 random numbers between 1 and 100:")
    for number in random_numbers():
        print(number)
