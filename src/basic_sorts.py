import random


def bubble_sort(arr):
    changed = False
    for i  in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                changed = True
        if not changed:
            return

def shaker_sort(arr):
    changed = True
    start = 0
    end = len(arr)-1
    while changed:
        changed = False
        for i in range(start, end):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                changed = True 
                
        if not changed: break
        end-=1
        for i in range(end-1, start-1, -1):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                changed = True
        start+=1

def comb_sort(arr):
    changed = True
    gap = len(arr)
    while gap!=1 or not changed:
        gap/=1.3
        gap = int(gap) if gap>1 else 1
        changed = False
        for i in range(len(arr)-gap):
            if arr[i]>arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                changed = True

def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap>0:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and key < arr[j-gap]:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = key
        gap//=2
        
def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0 or arr[index] >= arr[index-1]:
            index += 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index -= 1
            
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(min+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        
           
def merge_sort(array):
    if len(array) > 1:
        m = len(array)//2
        L = array[:m]
        R = array[m:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

arr = list(range(1, 11))
random.shuffle(arr)

print(arr)
merge_sort(arr)
print(arr)