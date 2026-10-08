# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:26:38 2026

@author: ahmet
"""

# isimler= ["ahmet","test1","test2","test3","test4",]
# bulundu_mu=False
# for isim in isimler:
#     if isim=="ahmet":
#         bulundu_mu=True 
#         break
#     else:
#         bulundu_mu=False
# if bulundu_mu==True:
#     print("Aranan isim bulundu")
# else:
#     print("Bulunamadı")
""" Bu yukarıdaki kodda listeleme mantığını öğrenmeye başlıyoruz. isimler adında bir
değişken oluşturup onun içindeki her bir değere de isim diyerek temeli atıyoruz. 
Ve bu sayede istediğiz değerin listenin içinde olup olmadığını kontrol edebiliriz.
 """
 
# isimler= ["AHMET","TEST1","TEST2","TEST3","TEST4",]
# bulundu_mu=False
# aranan=input("Hangi ismi aramak istiyorsunuz: ")

# for isim in isimler:
#     if isim==aranan.upper():
#         bulundu_mu=True
#         break
# if bulundu_mu==True:
#     print("Aranan isim bulundu")
# else:
#     print("Bulunamadı")
""" 
Burada ise aynı kodu biraz değiştirdik. Bu sefer aranan isim için 
kullanıcıdan bir girdi istiyor ve o girdi ile listeyi karşılaştırıp ona göre bir sonuç
gösteriyor
"""

# isimler=[]
# isim_sayisi=int(input("kaç isim gireceksin: "))
# for i in range(isim_sayisi):
#     eklenecek_isim=input("Eklemek istediğiniz ismi girin: ")
#     isimler.append(eklenecek_isim.upper())
# print(isimler)

"""Burada lisateye girdi yapmayı öğreniyoruz. -isimler- in içine -.append- kodu ile
-(parantezin içinde yazanı)- ekliyoruz."""


