from collections import ChainMap

dict = {"A": 1, "N": 2, "C": 4}
dict1 = {"Z": 1, "D": 2, "P": 4}
dict2 = {"W": 1, "E": 2, "R": 4}
total = ChainMap(dict, dict1, dict2)
print(total["A"])