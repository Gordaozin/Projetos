import math
cor_x1 = float(input())
cor_y1 = float(input())
cor_x2 = float(input())
cor_y2 = float(input())

dist = math.sqrt(((cor_x1-cor_x2)**2)+((cor_y1-cor_y2)**2))

if dist >= 10:
    print("longe")
else:
    print("perto")
