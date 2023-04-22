# find the largest number in the unknown array

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left_sorted = mergesort(left)
        right_sorted = mergesort(right)
        return merge(left_sorted, right_sorted)
        
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [90,5, 2, 9, 1, 7, 3,23]
arr_sorted = mergesort(arr)
largest = arr_sorted[-1]
print(largest)



#  // Given unsorted array of numbers return the sorted array in descending order
#   // let array=[123,89,5,23,9,56]

def merge_sort(arr):
   
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
   
    left = merge_sort(left)
    right = merge_sort(right)
    

    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

array = [123, 89, 5, 23, 9, 56]
sorted_array = mergesort(array)
print(sorted_array)




# How do you handle duplicate values when implementing mergesort in Python?

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result

arr = [3, 2, 1, 5,2,4,5,1]
sorted_arr = mergesort(arr)
print(sorted_arr)

# Sort a list of strings in alphabetical order using mergesort:

def sort_list(arr1):
    if len(arr1):
        return arr1
    mid=len(arr1)//2
    left=arr1[ :mid]
    right=arr1[mid: ]
    
    left=sort_list(left)
    right=sort_list(right)

    return sorted(left,right)

def sorted(left,right):
    emptyArr=[]

    l=0
    r=0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            emptyArr.append(left[l])
            l+=1
        else:
            emptyArr.append(right[r])
            r+=1
    emptyArr+=left[l:]
    emptyArr+=right[r:]
    return emptyArr

arr1=("apple","mango","banana","pears")
sorted_list = merge_sort(arr1)
print(sorted_list) 


#  Implement a merge sort function that takes an array of integers as input and returns the number
# of inversions in the array (an inversion occurs when two elements are out of order).

def arrayIntegers(num):
    if len(num)<=1:
        return num,0
    mid=len(num)//2
    left=num[ :mid]
    right=num[mid :]

    left=arrayIntegers(left)
    right=arrayIntegers(right)

    return sorted(left,right)

def sortde(left, right):
        newArray=[]

        i=0
        j=0
        k=0


        while i < len(left) and j <= len(right):

            if left[i] <= right[j]:

                result.append(left[i])

                i += 1

            else:

                result.append(right[j])

                j += 1

                k += len(left) - i


            result += left[i:]
            result += right[j:]

            return result, k


num = [5, 3, 2, 4, 1]
sorted_arr, k = arrayIntegers(num)
print(f"Sorted Array: {sorted_arr}")
print(f"Number of Inversions: {k}")





    
    







