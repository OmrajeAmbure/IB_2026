"""
Nested Function:
Number Analyzer

Create:
analyze_numbers(numbers)
Inside it create three nested functions:
find_even()
find_odd()
find_positive()

Display:

All even numbers
All odd numbers
All positive numbers
"""
def analyze_numbers(*numbers):
    def find_even(*numbers):
        print("Enven Number : ",end="")
        for num in numbers:
            if num%2==0:
                print(num,end=",")
    def find_odd(*numbers):
        print("\nEnven Number : ",end="")
        for num in numbers:
            if num%2==1:
                print(num,end=",")
    def find_positive(*numbers):
        print("\nEnven Number : ",end="")
        for num in numbers:
            if num > 0:
                print(num,end=",")
    find_even(*numbers)
    find_odd(*numbers)
    find_positive(*numbers)
numbers = [1,3,4,6,7,8,10,12,11,15,17,18]
analyze_numbers(*numbers)
