# Josh Freeman
# 5/20/2022
# A4 Functions
# Designing and Implementing functions
# Calculates the volume of a cone

def coneVolume(height, radius):

    v = (1/3) * 3.14 * (radius * radius) * height

    return v

def main():

    height = float(input("Enter the height of the cone: "))
    radius = float(input("Enter the base radius of the cone: "))
    volume = coneVolume(height, radius)
    volumeFormat = round(volume, 2)
    print(volumeFormat)

main()
