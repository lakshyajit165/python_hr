import math
AB = int(input())
BC = int(input())
angle = round(math.degrees(math.atan2(AB,BC)))
print(angle,chr(176),sep='')