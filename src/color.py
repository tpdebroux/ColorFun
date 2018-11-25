def HuetoRGB( v1, v2, vH ):
   if (vH < 0):
        vH += 1
   if (vH > 1):
        vH -= 1
   if ((6 * vH) < 1):
        return (v1 + (v2 - v1) * 6 * vH)
   if (( 2 * vH) < 1):
        return v2
   if (( 3 * vH) < 2):
        return (v1 + ( v2 - v1 ) * ((2 / 3) - vH) * 6)
   return v1

def HSLtoRGB( H, S, L):
    if (S == 0): #it is an easy conversion if there is no saturation
       R = L * 255
       G = L * 255
       B = L * 255
    else:
       if(L < 0.5):
           var_2 = L * (1 + S)
       else:
           var_2 = (L + S) - (S * L)

       var_1 = 2 * L - var_2

       R = 255 * HuetoRGB(var_1, var_2, H + (1 / 3))
       G = 255 * HuetoRGB(var_1, var_2, H)
       B = 255 * HuetoRGB(var_1, var_2, H - (1 / 3))
       return [R,G,B]

def RGBtoHSL( r, g, b):
    valR = r / 255
    valG = g / 255
    valB = b / 255

    minVal = min(valR, valG, valB)
    maxVal = max(valR, valG, valB)
    diffVal = maxVal - minVal

    L = (maxVal + minVal) / 2

    if (maxVal == 0):#this means all the values are 0 (aka black)
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

        return [H,S,L]
def getComplement( r, g, b ):
    HSL = RGBtoHSL(r, g, b)
    H = HSL[0]
    S = HSL[1]
    L = HSL[2]
    H = (H + 0.5) % 1
    RGB = HSLtoRGB(H, S, L)
    R = int(round(RGB[0]))
    G = int(round(RGB[1]))
    B = int(round(RGB[2]))
    print('Complement color: ')
    print(R,G,B)
def getAnalogous( r, g, b):
    HSL = RGBtoHSL(r, g, b)
    H = HSL[0]
    S = HSL[1]
    L = HSL[2]
    Hleft = (H + (1/12)) % 1
    RGBleft = HSLtoRGB(Hleft, S, L)
    Rleft = int(round(RGBleft[0]))
    Gleft = int(round(RGBleft[1]))
    Bleft = int(round(RGBleft[2]))
    Hright = (H - (1/12)) % 1
    RGBright = HSLtoRGB(Hright, S, L)
    Rright = int(round(RGBright[0]))
    Gright = int(round(RGBright[1]))
    Bright = int(round(RGBright[2]))
    print('Analogous colors: ')
    print(Rleft,Gleft,Bleft)
    print(Rright, Gright, Bright)
print('Enter a color in RGB form:\n')
#get rgb values from user, and catch bad input
r = input('R: ')

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

print('Input color: ')
print(r,g,b)
getComplement(r,g,b)
getAnalogous(r,g,b)
