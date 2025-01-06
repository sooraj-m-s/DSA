def insertion_sort(li):
    for i in range(1, len(li)):
        crnt = li[i]
        pos = i
        while crnt < li[pos-1] and pos > 0:
            li[pos] =  li[pos-1]
            pos -= 1
        li[pos] = crnt


li = [2, 4, 3, 5, 1]
insertion_sort(li)
print(li)
