maas = float(input("Lütfen mevcut maaşınızı giriniz: "))
zamOrani = float(input("Lütfen zam oranınızı(% olarak) giriniz: "))
zamMiktari = maas * (zamOrani / 100)
zamliMaas = maas + zamMiktari 
print("Zamlı Maaşınız:", zamliMaas)

