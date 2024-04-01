def insertion_sort(n):
    for i in range(1, len(n)):
        anchor = n[i]
        j = i - 1
        while j >= 0 and anchor < n[j]:
            n[j+1] = n[j]
            j = j - 1
        n[j+1] = anchor

li = [ 6, 8, 9, 3, 5, 2,]
insertion_sort(li)
print(li)
