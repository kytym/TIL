from typing import List
import random

def cocktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    swaped = True
    start = 0
    end = len_numbers - 1
    while swaped:
        swaped = False

        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swaped = True
        
        if not swaped:
            break
        
        swaped = False
        end -= 1
        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swaped = True        
        start += 1
    return numbers

if __name__ == "__main__":
    #numbers = [4,1,5,7,3,8]
    numbers = [random.randint(1,1000) for _ in range(10)]
    print(cocktail_sort(numbers))
