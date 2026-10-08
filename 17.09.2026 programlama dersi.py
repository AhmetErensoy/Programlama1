# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 13:01:55 2026

@author: ahmet
"""

    #değişken olarak iban tutulan bir değişken oluştur /string
    #Ad ve Soyad tutacak ayrı ayrı /string
    #Hesap bakiyesini tutacak  /float
    
    
#iban = "TR123456789123456"

#ad = "Ahmet"

#soy_ad = "Erensoy"

#hesap_bakiyesi = 9550.65

#print(iban + "\n"+ ad+ soy_ad+"\n"+str(hesap_bakiyesi))

#iban = input("İban bilgilerinizi giriniz: ")

#ad = input("Adınızı giriniz: ")

#soy_ad = input("Soyadınızı giriniz: ")

#hesap_bakiyesi = 9550.65

#print(iban + "\n"+ ad+ soy_ad+"\n"+str(hesap_bakiyesi))

#bakiye 100 milyondan fazla olamaz iban da 11 karakterden fazla olamaz

#iban = input("İban bilgilerinizi giriniz:")
 #if len(iban) > 11:
  #  print("11 karakterden fazla giremezsiniz")
    
   #100.000.000

#ad = input("Adınızı giriniz: ")

#soy_ad = input("Soyadınızı giriniz: ")

#hesap_bakiyesi = input("hesap bakiyesi giriniz: ")
#if len(iban) > 8:
 #   print("Hesap bakiyeniz 99.999.999'dan fazla olamaz")

#print(iban + "\n"+ ad+ soy_ad+"\n"+str(hesap_bakiyesi))


#ilk_sayi = int(input("İLk sayıyı giriniz: "))

#iki_sayi = input("İkinci sayıyı giriniz: ")

#islem = input("Yapmak istediğiniz işlemi giriniz ")

#print()


#kullanıcıdan adını soy adını istediğin yapıyı oluştur 

# ad = input("Adınızı giriniz: ")

# soy_ad = input("Soyadınızı giriniz: ")

# print(ad,soy_ad)

#sayı bir ile sayı ikiuyi al ikisinin dort işlem halini yaz

ilk_sayi = int(input("İlk sayıyı giriniz: "))

iki_sayi = int(input("İkinci sayıyı giriniz: "))

islem = input("yapmak istediğiniz işlemi giriniz: ")

toplam = ilk_sayi+iki_sayi
fark = ilk_sayi-iki_sayi
carp = ilk_sayi*iki_sayi
bolme= ilk_sayi/iki_sayi
if islem == "+":
    print("İki sayının toplamı: ",ilk_sayi+iki_sayi)

elif islem == "-":
                print("İki sayının farkı: ",ilk_sayi-iki_sayi)

elif islem == "*":
                 print("İki sayının çarpımı: ",ilk_sayi*iki_sayi)

elif islem == "/":
                print("İki sayının bölümü: ",ilk_sayi/iki_sayi)

else:
        print("Böyle bir işlem bulunamadı!")
# python açıklama satırı nedir ?

# print("""Uzun uzun metin Uzun uzun metin Uzun uzun metin Uzun uzun metin 
#       Uzun uzun metin Uzun uzun metin Uzun uzun metin Uzun uzun metin 
#       Uzun uzun metin Uzun uzun metin Uzun uzun metin Uzun uzun metin 
#       Uzun uzun metin Uzun uzun metin Uzun uzun metin 
#       Uzun uzun metin Uzun uzun metin Uzun uzun metin Uzun uzun metin 
#       Uzun uzun metin Uzun uzun metin Uzun uzun metin Uzun uzun metin """)

