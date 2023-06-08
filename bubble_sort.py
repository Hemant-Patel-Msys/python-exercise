def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0,len(array) -i -1):
            if array[j]>array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            #return temp
array = [12,-324,543,654,234]
bubble_sort(array)
print(array)