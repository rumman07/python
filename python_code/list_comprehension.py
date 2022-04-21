'''
List comprehension

'''

l1 = [i for i in range(0,20,2)]

even_number = [num for num in range(0,11) if num%2 ==0]
print(even_number)

# if else statement inside list comprehension
if_else = [x if x%2 ==0 else 'ODD' for x in range(0,11)]
print(if_else)

# nested for loop inside list comprehension
l2 = [2,3,4]
l3 = [1,10,1000]
nested_for = [x*y for x in list(l2) for y in list(l3)]
print(nested_for)
