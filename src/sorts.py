# from copy import copy
# from time import sleep
from colors import *
from config import LIST_LENGTH
# from rectangle import Rectangle


def bubble_sort(rects: list[int]):        
    for i in range(len(rects) - 1):
        changed = False
        
        for j in range(len(rects) - i - 1):
            if rects[j] > rects[j + 1]:
                rects[j],rects[j+1] = rects[j+1],rects[j]
                yield rects[j],rects[j+1]
                changed = True
            
        if not changed:
            return
    
def shaker_sort(rects: list[int]):
    start, end = 0, len(rects) - 1
    while start < end:
        changed = False
        for i in range(start, end):
            if rects[i] > rects[i + 1]:
                rects[i],rects[i+1] = rects[i+1],rects[i]
                yield rects[i],rects[i+1]
                changed = True

        if not changed:
            break
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if rects[i] > rects[i + 1]:
                rects[i],rects[i+1] = rects[i+1],rects[i]
                yield rects[i],rects[i+1]
                changed = True

        start += 1
        if not changed:
            break
        
def comb_sort(rects: list[int]):
    changed = True
    
    gap = len(rects)
    while gap!=1 or changed:
        gap = (gap * 10)/13
        gap = int(gap) if gap>1 else 1
        
        changed = False
        
        for i in range(len(rects)-gap):
            if rects[i]>rects[i+gap]:
                rects[i],rects[i+gap]=rects[i+gap],rects[i]
                yield rects[i],rects[i+gap]
                changed = True

def insertion_sort(rects: list[int]):
    n = len(rects)
    if n <= 1:
        return
    for i in range(1, n):
        key = rects[i]
        j = i - 1
        while j >= 0 and key < rects[j]:
            rects[j+1] = rects[j]
            yield rects[j], rects[j+1]
            j -= 1
        rects[j + 1] = key
        yield key, rects[j+1]

def shell_sort(rects: list[int]):
    n = len(rects)
    gap = n//2
    while gap>0:
        for i in range(gap, n):
            key = rects[i]
            j = i
            while j >= gap and key < rects[j-gap]:
                rects[j] = rects[j-gap]
                yield rects[j-gap], rects[j]
                j -= gap
            rects[j] = key
            yield key, rects[j]
        gap//=2

def gnome_sort(rects: list[int]):
    index = 0
    while index < len(rects):
        if index == 0 or rects[index] >= rects[index-1]:
            index += 1
        else:
            rects[index],rects[index-1] = rects[index-1],rects[index]
            yield rects[index], rects[index-1]
            index -= 1

def selection_sort(rects: list[int]):
    n = len(rects)
    for i in range(n):
        min = i
        for j in range(min+1, n):
            if rects[j] < rects[min]:
                min = j
        rects[i], rects[min] = rects[min], rects[i]
        yield rects[i], rects[min]

def merge_sort(rects: list[int], left=0, right=LIST_LENGTH-1):
    if left < right:
        mid = (left + right) // 2
        yield from merge_sort(rects, left, mid)
        yield from merge_sort(rects, mid + 1, right)
        yield from merge(rects, left, mid, right)

def merge(rects: list[int], left, mid, right):
    temp = rects[:]
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if temp[i] <= temp[j]:
            rects[k] = temp[i]
            yield rects[k], temp[i]
            i += 1
        else:
            rects[k] = temp[j]
            yield rects[k], temp[j]
            j += 1
        k += 1

    while i <= mid:
        rects[k] = temp[i]
        yield rects[k], temp[i]
        i += 1
        k += 1

    while j <= right:
        rects[k] = temp[j]
        yield rects[k], temp[j]
        j += 1
        k += 1
