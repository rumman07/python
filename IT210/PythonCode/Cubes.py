##
#This program computes the volume of two cubes.
#

def main():
    result1 = cubeVolume(2)
    result2 = cubeVolume(10)
    print("A cube with side length has volume", result1)
    print("A cube with side length has volume", result2)

##Computes the volume of a cube.
#@param sideLength the length of a side of the cube.
#@return the volume of the cube
#
def cubeVolume(sideLength):
    volume = sideLength**3
    return volume

#Call the main function to begin executing the program.
main()
