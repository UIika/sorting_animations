from copy import copy
from time import sleep
from colors import *
from rectangle import Rectangle


def bubble_sort(rects: list[Rectangle]):        
    for i in range(len(rects) - 1):
        changed = False
        
        for j in range(len(rects) - i - 1):
            if rects[j] > rects[j + 1]:
                yield from rects[j].swap(rects[j+1])
                changed = True
            
        if not changed:
            return
    
def shaker_sort(rects: list[Rectangle]):
    start, end = 0, len(rects) - 1
    while start < end:
        changed = False
        for i in range(start, end):
            if rects[i] > rects[i + 1]:
                yield from rects[i].swap(rects[i+1])
                changed = True

        if not changed:
            break
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if rects[i] > rects[i + 1]:
                yield from rects[i].swap(rects[i+1])
                changed = True

        start += 1
        if not changed:
            break
        
def comb_sort(rects: list[Rectangle]):
    changed = True
    
    gap = len(rects)
    while gap!=1 or changed:
        gap = (gap * 10)/13
        gap = int(gap) if gap>1 else 1
        
        changed = False
        
        for i in range(len(rects)-gap):
            if rects[i]>rects[i+gap]:
                yield from rects[i].swap(rects[i+gap])
                changed = True

def insertion_sort(rects: list[Rectangle]):
    n = len(rects)
    if n <= 1:
        return
    for i in range(1, n):
        key = copy(rects[i])
        j = i - 1
        while j >= 0 and key < rects[j]:
            yield from rects[j+1].replace(rects[j])
            j -= 1
        yield from rects[j + 1].replace(key)

def shell_sort(rects: list[Rectangle]):
    n = len(rects)
    gap = n//2
    while gap>0:
        for i in range(gap, n):
            key = copy(rects[i])
            j = i
            while j >= gap and key < rects[j-gap]:
                yield from rects[j].replace(rects[j-gap])
                j -= gap
            yield from rects[j].replace(key)
        gap//=2

def gnome_sort(rects: list[Rectangle]):
    index = 0
    while index < len(rects):
        if index == 0 or rects[index] >= rects[index-1]:
            index += 1
        else:
            yield from rects[index].swap(rects[index-1])
            index -= 1

def selection_sort(rects: list[Rectangle]):
    n = len(rects)
    for i in range(n):
        min = i
        for j in range(min+1, n):
            if rects[j] < rects[min]:
                min = j
        yield from rects[i].swap(rects[min])
        
def merge_sort(rects: list[Rectangle]):
    if len(rects) > 1:
        m = len(rects)//2
        L = rects[:m]
        R = rects[m:]

        yield from merge_sort(L)
        yield from merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                yield from rects[k].replace(L[i])
                i += 1
            else:
                yield from rects[k].replace(R[j])
                j += 1
            k += 1
        while i < len(L):
            yield from rects[k].replace(L[i])
            i += 1
            k += 1
        while j < len(R):
            yield from rects[k].replace(R[j])
            j += 1
            k += 1