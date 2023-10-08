#To Create A List, You Assign Values To A Variable .Ex:

fruit = ["pineapple", "avocado", "pear"]

#To Add Items Later Create An Empty List & Store It In A Variable

supplies = []

#or

supplies = list()

#Objects stored in list are given an index number starting at 0.
#To read an element from a list, use the index number of the stored value. Ex:

fruit = ["apples", "oranges","bananas"]
print(fruit[1])

#To get the length of a list, use the len function. Ex:

print(len(fruit))

# To Get The Output Of The End Of The List, Use Negative Numbers In The Indexes.
#Ex:

print(fruit[-1])
print(fruit[-2])

#Lists are mutable, which means they can be changed after you create them. 
#You can add, update, delete and reorder elements in a list. You Can Add An Element
#By Appending It To The List Ex:

fruit.append("strawberries")
print(fruit)

#If you want add an element at a specific point in the list you can use the index 
# value with the insert() method. Ex:

fruit.insert(1 , "pears")
print(fruit)

# To Temporarily Sort The Order Of A List, You Would Use The Sorted Function.Ex:

print(sorted(fruit))
print(fruit)

#To Permanently Sort The List Items. Ex:

fruit.sort()
print(fruit)

#To reverse the order of a list you can use the reverse() method. 
#This will permanently reverse the order of the list. Ex:

fruit.reverse()
print(fruit)

#You can remove elements from a list using the del statement if you know the index position.
#Ex:

del fruit[0]
print(fruit)

#If you want to use the value after removing it from a list you use the pop() method.
#To use pop(),you need to store the value you have removed from the list inside another variable.
#Ex:

favorite_fruit = fruit.pop()
print(favorite_fruit)

# You can return any element with the pop() by using the index value. Ex:

fresh_fruit = fruit.pop(1)
print(fresh_fruit)

#If you don't know the index position, or you don't want to remove the last item in the list,
#you can use the remove() method to specify the value of the element you want to remove. Ex:

fruit.remove('apples')
print(fruit)

replay = fruit.pop(0)
print(replay)