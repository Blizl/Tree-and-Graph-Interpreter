class MergeSort(object):
    def merge_sort(self, a_list):

        if len(a_list) > 1:
            mid = len(a_list)/2
            left = a_list[:mid]
            right = a_list[mid:]

            self.merge_sort(left)
            self.merge_sort(right)
            i=0
            j=0
            k=0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    a_list[k] =  left[i]
                    i+=1
                else:
                    a_list[k] = right[j]
                    j+=1
                k+=1

            while i < len(left):
                a_list[k] = left[i]
                i+=1
                k+=1
            while j < len(right):
                a_list[k] = right[j]
                j+=1
                k+=1


a_list = [6,5,8,2,1]
obj = MergeSort()
obj.merge_sort(a_list)
print a_list
