#raiz quadrada ax²+bx+c=0
import math
a=1
b=-10
c=21

delta = (b**2)-4 * a * c

basPos = (-b+math.sqrt(delta))/2*a
basNeg = (-b-math.sqrt(delta))/2*a

if basPos == 0 and basNeg == 0:
    print("a raiz quadrada é 0")

else:
    print("as raízes são:",basPos,"e",basNeg)
