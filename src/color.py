print('Enter a color in RGB form:\n')

r = input('R: ')
#print (isinstance(r, int))
while((not isinstance(r, int))):
    try:
        r = int(r)
        if (r > 255 or r < 0 ):
            raise ValueError('Must be 0-255')
    except:
        print('R must be decimal value (0-255)')
        r = input('R: ')
g = input('G: ')
while(not isinstance(g, int)):
    try:
        g = int(g)
        if (g > 255 or g < 0 ):
            raise ValueError('Must be 0-255')
    except:
        print('G must be decimal value (0-255)')
        g = input('G: ')
b = input('B: ')
while(not isinstance(b, int)):
    try:
        b = int(b)
        if (b > 255 or b < 0 ):
            raise ValueError('Must be 0-255')
    except:
        print('B must be decimal value (0-255)')
        b = input('B: ')

print(r,g,b)

valR = r / 255
valG = g / 255
valB = b / 255

minVal = min(valR, valG, valB)
maxVal = max(valR, valG, valB)
diffVal = maxVal - minVal

L = (maxVal + minVal) / 2

if (maxVal == 0):
    H = 0
    S = 0
else:
    if (L < 0.5):
        S = diffVal / (maxVal + minVal)
    else:
        S = diffVal / (2 - maxVal - minVal)

    if(diffVal == 0):
        deltaR = deltaG = deltaB = 0
    else:
        deltaR = (((maxVal - valR) / 6) + (diffVal / 2)) / diffVal
        deltaG = (((maxVal - valG) / 6) + (diffVal / 2)) / diffVal
        deltaB = (((maxVal - valB) / 6) + (diffVal / 2)) / diffVal

    if (valR== maxVal):
        H = deltaB - deltaG
    elif (valG == maxVal ):
        H = (1 / 3) + deltaR - deltaB
    elif (valB == maxVal):
        H = (2 / 3) + deltaG - deltaR

    if (H < 0):
        H += 1
    if (H > 1):
        H -= 1
print(H,S,L)
H2 = (H + 0.5) % 1
print(H2)
