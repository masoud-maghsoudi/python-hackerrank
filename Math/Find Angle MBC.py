import math

AB = int(input())
BC = int(input())

print("{:.0f}{}".format(math.degrees(math.atan2(AB,BC)),u"\u00b0"))
