#!/usr/bin/python3.8
def printTriangle(sideLength): 
    if sideLength < 1 :
        return
    printTriangle(sideLength - 1)
    print("[]" * sideLength)

printTriangle(2)
