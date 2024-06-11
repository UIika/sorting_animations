def merge_sort(rects: list[Rectangle]):
    if len(rects) > 1:
        m = len(rects) // 2
        L = rects[:m]
        R = rects[m:]
        
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Слияние отсортированных списков L и R обратно в rects
        while i < len(L) and j < len(R):
            if L[i].height < R[j].height:
                rects[k].replace(L[i])
                i += 1
            else:
                rects[k].replace(R[j])
                j += 1
            k += 1
        
        while i < len(L):
            rects[k].replace(L[i])
            i += 1
            k += 1
        
        while j < len(R):
            rects[k].replace(R[j])
            j += 1
            k += 1

# Создаем список объектов Rectangle
l = [Rectangle(1, 1, 1, 1, i) for i in range(10, 0, -1)]
print([rect.height for rect in l])  # Выводим текущие высоты

merge_sort(l)  # Сортируем по высоте

print([rect.height for rect in l])  # Выводим отсортированные высоты
