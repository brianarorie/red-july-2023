#By using the variable item it lists out the items in the list one by one each
#time that the loop iterates

fruit = ['apples','oranges','bananas']

for item in fruit:
    print(f'The best fruit now is {item}')

#To use the loop as a counter. Ex:

numbers = [0,1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(f'The next number is {number}')
    
#to print out a large amount of numbers without having to input each one, use the range() method.Ex:    
    
    
for number in range(10):
    print(f'The next number is {number}')
    
#you use the range method to start counting from 1 

for number in range(1,10):
    print(f'The next number is {number}')
    
# If you want to increment the counter by more than the default value of 1, 
#if you wanted only odd numbers or even numbers,you would add a third parameter to the range() function as shown below.   

for number in range(1,10,2):
    print(f'The next number is {number}')


