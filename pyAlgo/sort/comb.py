import random 
from typing import List

def comb_sort(numbers: List[int]) -> List[int]:
    len_nums = len(numbers)
    gap = len_nums
    swapped = True

    while gap != 1 or swapped:
        gap = int(gap/1.3)
        if gap < 1:
            gap = 1
        
        swapped = False

        for i in range(0, len_nums - gap):
            if numbers[i] > numbers[i + gap]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
    
    return numbers




if __name__ == "__main__":
    numbers = [random.randint(0,100) for _ in range(10)]
    print(comb_sort(numbers))