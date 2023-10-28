
sayi = input("Bir Sayı Giriniz: ")
tersSayi = sayi[::-1]  #[::-1]
if sayi == tersSayi:
    print("Bu sayı bir palindrom sayıdır.")
else: 
    print("Bu sayı bir palindrom sayı değildir.")