# Define a function that accepts a string as input and uses
#  the for loop to iterates through the string and count the vowels

def count_vowels(str):
    vowels = "aeiou"
    count = 0
    for a in str:
        if a in vowels:
            count += 1
    return count
print(count_vowels("beautiful"))
   



        
