# function - calculating the volume
# function - get the length, width, and height from the user
# function - display the results

def calcVolume(a,b,c):
    V=a*b*c
    return V

def getUserInput():
    l = float(input('Length of rectangle:'))
    w = float(input('Width of rectangle:'))
    h = float(input('Height of prism:'))
    return l,w,h

def displayVolume(vol):
    print(vol)

length,width,height = getUserInput()

Volume = calcVolume(length,width,height)
displayVolume(Volume)