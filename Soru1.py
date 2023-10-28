#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
name=input("İsminiz:")
boy = float(input("Boyunuzu metre (m) cinsinden giriniz: "))
kilo = float(input("Kilonuzu kilogram (kg) cinsinden giriniz: "))

VKİ = round(kilo / (boy ** 2) ,1)
print("Vücut Kitle İndeksiniz (VKİ): ", VKİ)

