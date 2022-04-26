from collections import ChainMap

dict = {"A": 1, "N": 2, "C": 4}
dict1 = {"Z": 1, "D": 2, "P": 4}
dict2 = {"W": 1, "E": 2, "R": 4, "A":7}
total = ChainMap(dict2, dict1, dict)
print(total["A"])