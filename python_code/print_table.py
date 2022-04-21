'''
Given a 2D list this function will print a table.
'''

list = [[1,2,3],["_","_","_"],["A","B","C"]]

def print_table(arr):
  for row in arr:
    for elem in row:
      print(elem, end=" ")
    print()
    
print_table(list)