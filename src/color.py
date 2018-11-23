def Hue_2_RGB( v1, v2, vH ):
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

print('Input color: ')
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

H2 = (H + 0.5) % 1

if (S == 0):
   R_comp = L * 255
   G_comp = L * 255
   B_comp = L * 255
else:
   if(L < 0.5):
       var_2 = L * (1 + S)
   else:
       var_2 = (L + S) - (S * L)

   var_1 = 2 * L - var_2

   R_comp = 255 * Hue_2_RGB(var_1, var_2, H2 + (1 / 3))
   G_comp = 255 * Hue_2_RGB(var_1, var_2, H2)
   B_comp = 255 * Hue_2_RGB(var_1, var_2, H2 - (1 / 3))

R_comp = int(round(R_comp))
G_comp = int(round(G_comp))
B_comp = int(round(B_comp))
print ('Complimentary color: ')
print (R_comp, G_comp, B_comp)
