# The Collatz Conjecture program - Shih-Yuan Wang

def collatz(num):
    # the number is even
    if num % 2 == 0:
        num = num //2
        print(num)
        return num
    
    # the number is odd
    elif num % 2 ==1:
        num = 3 * num + 1
        print(num)
        return num

try:
    # Prompts for user input
    number = int(input('Enter a positive integer number greater than 1: '))
    
    # if input number is less than or equal to 1
    if number <= 1:
        print('Please enter a positive integer number greater than 1.')
        
    else:    
        while number != 1:
            number = collatz(number)
            
except ValueError: # wrong input data type
    print('Invalid Value. Please enter a positive integer number greater than 1.')





    
    



