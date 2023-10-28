import math

r = float(input("Dairenin yarıçapını giriniz:"))

alan = round(math.pi * r * r, 2)
cevre = round(2 * math.pi * r ,2)

print("Dairenin alanı : {}, Dairenin çevresi : {} " .format(alan,cevre))