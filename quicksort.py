import random
from multiprocessing import Process

def swap (arr, firstIndex, secondIndex):
    """
    Swapping the places of two elements in an array
    """
    temp = arr[firstIndex]
    arr[firstIndex] = arr[secondIndex]
    arr[secondIndex] = temp

def partition(arr, lowIndex, highIndex, pivot):
    """
    Moving elements in the array according to 
    their relationship to the pivot element or
    in other words if they are smaller or not
    """
    lp = lowIndex
    rp = highIndex - 1
    while lp < rp:
        while(float(arr[lp]) <= float(pivot) and lp < rp): #move upon appearance of element greater than pivot
            lp += 1
        while(float(arr[rp]) >= float(pivot) and lp < rp): #move until appearance of element less than the pivot
            rp -= 1
        swap(arr, lp, rp)
    if arr[lp] > arr[highIndex]: #In case of last being out of order
        swap(arr, lp, highIndex)
    else:
        lp = highIndex
    return lp

def quicksort(arr, lowIndex, highIndex):
    """
    Performing quicksort for the given array
    """
    if lowIndex >= highIndex:
        return
    pivotIndex = random.randint(lowIndex, highIndex) #Choosing a random pivot element
    pivot = float(arr[pivotIndex])
    swap(arr, pivotIndex, highIndex) #Placing the pivot element at the end
    lp = partition(arr, lowIndex, highIndex, pivot)
    quicksort(arr, lowIndex, lp - 1)  #sorting the left side
    quicksort(arr, lp + 1, highIndex) #sorting the right side

def quicksort_parallel(arr, lowIndex, highIndex):
    """
    Performing parallel quicksort for the given array
    """
    if lowIndex >= highIndex:
        return
    pivotIndex = random.randint(lowIndex, highIndex) #Choosing a random pivot element
    pivot = float(arr[pivotIndex])
    swap(arr, pivotIndex, highIndex) #Placing the pivot element at the end
    lp = partition(arr, lowIndex, highIndex, pivot)
    p1 = Process(target=quicksort, args=(arr, lowIndex, lp - 1))  #sorting the left side
    p2 = Process(target=quicksort, args=(arr, lp + 1, highIndex)) #sorting the right side

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    

if __name__ == '__main__':
    list = [156, 1651, -955, 1, 20, 69, 31]
    print(list)
    quicksort(list, 0, len(list)-1)
    print(list)
