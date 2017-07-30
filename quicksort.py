def swap(_list, x, y):
    tmp = _list[x]
    _list[x] = _list[y]
    _list[y] = tmp

def partition(_list, left, right):
    x = _list[right]
    j = left -1
    for i in range(left, right):
        if _list[i] <= x:
            j +=1
            swap(_list, j, i)
    swap(_list,j+1, right)
    return j+1

def quicksort(_list, left, right):
    if left < right:
        s = partition(_list, left, right)
        quicksort(_list, left, s-1)
        quicksort(_list, s, right)


a = [25, 15, 9, 76, 32, 8, 2, 19]
print "a before sorting is ", a
print "passing in %s as right" %(len(a) -1)
quicksort(a, 0, len(a) -1)
print "a after sorting is ", a
