# Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50. 
def prime_numbers():
    x=1
    while x<50:
        x+=1
        if x%2==0:
            continue
        print(x)

# Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
# def integers():
#     x=range(20)

#     for i in x:
#         if i%2!=0:
#             print(f"{i}is a prime number")
#     else:
#         print(f"{i}not prime")
def integers(n):
    if n<20:
        print("prime")
    else:
        print("not prime")
    for i in range(2,n):
        if n%i==0:
            print("prime")
            break
        print("not prime")
integers()


            

# # Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.
# def list_even_numbers(*nums):
#     sum=0
#     for i in nums:
#         if i%2==0:
#             sum+=i
#     return sum
# print(list_even_numbers(2,3,12,56,9))

# # Write a function that takes any two integers as input, and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
# def sum_all_numbers(a,b):
#     sum=0
#     for i in range(a,b+1):
#         if i%3==0:
#             sum+=i
#         return sum
#     print(sum_all_numbers(12,3))

   

   

   

