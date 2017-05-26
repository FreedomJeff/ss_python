#!/usr/bin/env python
#-*-coding:utf-8-*-
data = [1,2,4,6,12,14,16,20,25,26,28,30,34,40,44,45,56,59,77,99]
print(data, len(data))

def binary_search(dataset, wanted):
    if len(dataset) > 1:
        mid = int(len(dataset) / 2)
        if dataset[mid] == wanted:
            print("find the number [%s], index[%d]" % (dataset[mid], mid))
            find_x = int(dataset[mid])
        elif dataset[mid] < wanted:
            print("wanted number is in right side, mid number[%s]" % dataset[mid])
            return binary_search(dataset[mid + 1: ], wanted)
        else:
            print("wanted number is left side, mid number[%s]" % dataset[mid])
            return binary_search(dataset[0:mid], wanted)
    else:   
        if dataset[0] == wanted:
            print("find the number[%s]" % dataset[0])
            find_x = int(dataset[0])
        else:
            print("no wanted number [%s] in dataset" % wanted)
            
binary_search(data, 6)

# lambda
find_x = 9
func = lambda x : x**2
print(func(find_x))
