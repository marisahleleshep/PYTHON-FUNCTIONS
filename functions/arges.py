def my_country(country="Rwanda"):
    print(f"Hello from {country}")

def greet(*names):
    for name in names:
        print(name)  

def sum(*numbers):
    answer=0
    for number in numbers:
        answer+=number

    return answer

def multiply(*intergers):
    result=1
    for interger in intergers:
        result*=interger
    return result 

# accepts any number of keyword arguments
def student_attribute(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

#  A function named concatenate_args that takes any number of string 
#  arguments in positional arguments format and concatenates them into a single string       
      
def concatenate(*maths):
    return "".join(maths)
    x=concatenate()
    print(x)
  




# A function named concatenate_kwargs that takes any number of string arguments in 
# keyword arguments  format and concatenates them into a single string    
def concatenate_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

