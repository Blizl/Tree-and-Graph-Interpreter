class QuickSort(object):

    def swap(self, _list, x, y):
        tmp = _list[x]
        _list[x] = _list[y]
        _list[y] = tmp

    def partition(self, _list, left, right):
        x = _list[right]
        j = left -1
        for i in range(left, right):
            if _list[i] <= x:
                j +=1
                self.swap(_list, j, i)
        self.swap(_list,j+1, right)
        return j+1

    def quicksort(self, _list, left, right):
        if left < right:
            s = self.partition(_list, left, right)
            self.quicksort(_list, left, s-1)
            self.quicksort(_list, s, right)

    def selection_sort(self, alist):
        for i in range(len(alist)):
            min = alist[i], i
            for j in range(i,len(alist)):
                if alist[j] < min[0]:
                    min = alist[j], j
            self.swap(alist, i, min[1])

a = [25, 15, 9, 76, 32, 8, 2, 19]
print "a before sorting is ", a
print "passing in %s as right" %(len(a) -1)
q= QuickSort()
# q.quicksort(a, 0, len(a) -1)
q.selection_sort(a)
print "a after sorting is ", a
