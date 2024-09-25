import random

def in_order(numbers):
    return  all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
    # for i in range(len(numbers)-1):
    #     if numbers[i] > numbers[i+1]:
    #         return False
    # return True

def bogo_sort(numbers):
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers

if __name__ == "__main__":
    numbers = [1,5,3,2,6,10,4]
    print(bogo_sort(numbers))
    