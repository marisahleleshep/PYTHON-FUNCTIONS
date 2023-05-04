# Write a function to reverse a string in Python without using any built-in functions.
def reverseString(str):
    newArr=""
    for i in range(len(str)-1,-1,-1):
        newArr+=str[i]

    return newArr

print(reverseString("marisah"))
    
# def reverseStr(str1):
#     emty=""
#     for i in     

def reverse_string(string):
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string

my_string = "hello, world!"
reversed_string = reverse_string(my_string)
print(reversed_string)

# Write a function that takes an array of integers and returns the sum of all the even numbers in the array.
def intergers(*int):
    sum=0
    for i in int:
        if i%2==0:
            sum+=i
    return sum

print(intergers(2,3,4,7,8,9))

def nums(num):
    if num<9:
      return nums
    
print(nums(12))

# Write a function that takes an array of integers and returns the sum of all the odd numbers in the array.
def addition(*arr):
    sum=0
    for i in arr:
        if i%2!=0:
            sum+=i

    return sum
print(addition(1,3,4,5,6,7))


# Write a function that takes an array of integers and returns the largest number in the array.
def numbers(*all):
    sum=all[0]
    for i in range(1,len(all)):
        if all[i]>sum:
            sum=all[i]
    return sum
print(numbers(1,12,7,56,80))


# Write a function that takes an array of integers and returns the smallest number in the array.
def smallestNum(*num):
    sum=num[0]
    for i in range(1,len(num)):
        if num[i]>sum:
            sum=num[i]
    return sum
print(smallestNum(12,70,67,90))

# Write a function that takes an array of integers and returns a new array with all the even numbers removed.
def evenNum(*arr1):
    empty=[]
    for x in arr1:
        if x%2!=0:
            empty.append(x)
    return empty
print(evenNum(1,2,4,5,7,8,10,12,9))


# Write a function that takes an array of integers and returns a new array with all the duplicates removed.

# Using for loop to remove duplicates
def duplicate(*num):               
    empty=[]
    for i in num:
        if i not in empty:
            empty.append(i)
    return empty

print(duplicate(1,2,2,5,5,8,9,10))

# Using an inbult function
def duplicates(*num):
    return list(set(num))
print(duplicate(1,2,2,5,5,8,8,90))

# Write a function that takes an array of integers and returns the product of all the numbers in the array.
def productNum(*num):
    product=1
    for i in range(len(num+1)):
        product*=i
    return product
print(productNum(2,3,4,5,6))
    
# def product(*pro):
#     empty=[]
#     for i in range(len(pro)):
#         if i%2==0:
#             empty.append(i)
#     return empty
# print(product(2,3,4,12,5,6))


def multiplication(*arr):
    product=1
    for i in arr:
        product*=i
    return product
print(multiplication(12,34,56,78))


    