def left(i):
   return   (2 * i)

def right(i):
   return (2 * i) + 1
def max_heapify(aList, i, heap_size):
    l = left(i)
    r = right(i)
    print "l is %d, r is %d i is %d" % (l, r, i)
    print "l < len(aList) - 1", l <= len(aList) -1
    if (l <= heap_size) and (aList[l] > aList[i]):
        largest = l
    else:
        largest = i
    if (r <= heap_size) and (aList[r] > aList[largest]):
        largest = r
    if largest != i:
        print "before swap, largest index is %d, i index is %d" % (largest, i)
        swap(aList, i, largest)
        print "swapped new list is", aList
        print 'largest is', largest
        max_heapify(aList, largest, heap_size)

def build_max_heap(aList, heap_size):
    for i in range((len(aList)/2), -1, -1):
        max_heapify(aList, i, heap_size)

def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def heapsort(aList):
    heap_size = len(aList) -1 
    build_max_heap(aList, heap_size)
    print "\nDone building initial max heap\n"
    print aList
    for i in range(len(aList)-1, 0, -1):
        print "i is %d" % i
        swap(aList, 0, i)
        heap_size = heap_size - 1
        max_heapify(aList, 0, heap_size)

A = ["hello","hi",'bye','hotpot','advark','sat']
print A
heapsort(A)
print A

