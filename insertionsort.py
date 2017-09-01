class InsertionSort(object):
    def sort(self, a_list):
        for i in range(1, len(a_list)):
            key = a_list[i]
            j = i-1
            while j > -1 and a_list[j] > key:
                a_list[j+1] = a_list[j]
                j -=1
            a_list[j+1] = key


insertion_sort = InsertionSort()
a_list = [7,5,9,12,3,1]
insertion_sort.sort(a_list)
print a_list
