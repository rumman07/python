def main():
    result = cubeVolume(3)
    print("The calculated volume", result)

def cubeVolume(sideLength):
    if(sideLength >= 0):
        volume = sideLength ** 3
    else:
        volume = 0
    return volume
        
main()
