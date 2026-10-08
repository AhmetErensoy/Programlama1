# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 00:44:42 2026

@author: ahmet
"""


# ilk_bakiye = float(input("Bakiyenizi giriniz: "))
# eklenen_bakiye = float(input("Eklemek istediğiniz bakiyeyi giriniz: "))
# print("Son bakiyeniz: ", ilk_bakiye+eklenen_bakiye)


# rakam = int(input("rakam giriniz: "))

# rakam_2 = int(input("2. rakamı giriniz:"))

# if rakam>5 and rakam_2>5:
    
#     print("iki rakam da beşten büyük")
    
    
# elif rakam == 5 and rakam_2 ==5:
    
#     print("İki rakam da beş")
    

# elif rakam<5 and rakam_2<5:
#     print("İki rakam da beşten küçük")
    
    
# else:
    
#     print("İki rakamın 5 e olan eşitlik değeri farklı")

# meyveler = ["elma", "armut", "muz"]

# for meyve in meyveler:
#     print(meyve)

# pythonda karar yapıları nelerdir nasıl kullanılır

# kullnıcıdan iki sayı al ve iki sayının da sıfırdan büyük olması 
# zorunlu değilse kullanıcıya sıffırdan büyük olmalı demesi gerek

# rakam = int(input("ilk sayıyı giriniz: "))
# rakam_2 = int(input("2. rakamı giriniz:"))

# if rakam>0 and rakam_2>0:
    
#     print("iki rakam da sıfırdan büyük :D")
    
# else:
    
#     print("İki rakam da sıfırdan büyük olmalı!")


# kullanıcı adı ve şifreyi kullanıcıdan iste eğer
#  kullanıcı adı test şifresi 1234 ise ekrana hoşgeldin kullanıcı yaz

# user= "test" 
# sifre = "1234"

# g_user= input("Kullanıcı adını giriniz: ")

# g_sifre= input("Şifreyi giriniz: ")
  
# if g_user == user and g_sifre == sifre:
#     print("Hoşgeldin kullanıcı :D İki sayı gir toplama yapalım:")
    
#     sayi_1= int(input("1. sayıyı giriniz:" ))
#     sayi_2= int(input("2. sayıyı giriniz: "))
#     print(sayi_1+sayi_2)                  
# else:
#     print("Kullanıcı adı veya şifre yanlış! ")

# kullanıcı adı ve sifre soruldukran sonra eğer doğruysa 
# bana sayı bir ve sayı2 sor ve toplamını ekrana yaz

# iç içe if kullanımı nedir nasıl kullanılır?
# sayı bir ve sayı 2 girilince kullanıcıya yapmak istediği işlemi sor
# dort işlemi yapabilecek ve kullanıcının istediği işlem yapılabilir olacak


# user= "test" 
# sifre = "1234"

# g_user= input("Kullanıcı adını giriniz: ")

# g_sifre= input("Şifreyi giriniz: ")
  
# if g_user == user and g_sifre == sifre:
#     print("Hoşgeldin kullanıcı :D")
    
#     sayi_1= int(input("1. sayıyı giriniz:" ))
#     sayi_2= int(input("2. sayıyı giriniz: "))
#     islem= input("Yapmak istediğiniz işlemi giriniz(toplama-çıkarma-çarpma-bölme): ")
    
#     # x= islem.lower()
    
#     if islem.lower() == "toplama":
#         print(sayi_1+sayi_2)
        
#     elif islem.lower() == "çıkarma":
#         print(sayi_1-sayi_2)
        
#     elif islem.lower() == "çarpma":
#         print(sayi_1*sayi_2)
    
#     elif islem.lower() == "bölme":
#         print(sayi_1/sayi_2)
#     else:
#         print("böyle bir işlem bulunmamakta!")
# else:
#     print("Kullanıcı adı veya şifre yanlış! ")


# user= "test" 
# sifre = "1234"

# g_user= input("Kullanıcı adını giriniz: ")

# g_sifre= input("Şifreyi giriniz: ")
  
# if g_user == user and g_sifre == sifre:
#     print("Hoşgeldin kullanıcı :D")
    
#     sayi_1= int(input("1. sayıyı giriniz:" ))
#     sayi_2= int(input("2. sayıyı giriniz: "))
#     islem= input("Yapmak istediğiniz işlemi giriniz(toplama-çıkarma-çarpma-bölme): ")
    
#     # x= islem.lower()
    
#     if islem.lower() == "toplama":
        
#         if sayi_1>-1 and sayi_2>-1 :
#             print(sayi_1+sayi_2)
#         else:
#             print("sayılar 0 veya daha büyük olmalıdır! ")
#     elif islem.lower() == "çıkarma":
#         print(sayi_1-sayi_2)
        
#     elif islem.lower() == "çarpma":
#         print(sayi_1*sayi_2)
    
#     elif islem.lower() == "bölme":
#         print(sayi_1/sayi_2)
#     else:
#         print("böyle bir işlem bulunmamakta!")
# else:
#     print("Kullanıcı adı veya şifre yanlış! ")

# 2 tane sabit iban tanımla: alıcı - gönderici iban. içerisine örnek iban gir(tr00000.tr111111)
# kullanıcıya sor kime para göndereceksin diye ve iban al. Kullanıcıdan da kendi iban bilgilerini iste.
# eğer kullanıcıların girdileri tanımlılar ile uyuşuyorsa kullanıcıya ne kadar para göndereceğini sor.
# kullanıcının yazacağı miktar 0 da küçük veya 1 milyondan fazla olamaz eğer koşullar uyuyorsa ekrana 
# paranız gönderildi yaz.

# iban_1 = "TR0000000000"
# iban_2 = "TR1111111111"

# k_iban= input("Kendi ibanınızı giriniz: ")
# g_iban= input("Para göndermek istediğiniz ibanı giriniz: ")

# if iban_1 == k_iban and iban_2==g_iban:
#     para=float(input("Göndermek istediğiniz para nedir? "))
    
#     if para>0 and para<1000000:
#         print("Paranız gönderildi")
#     else:
#         print("gönderilen para 0 dan küçük veya 1 milyondan fazla olamaz")
        
# else:
#     print("İbanlar uyuşmuyor")
    
# iban tr ile başlamıyorsa tr ile başlamalıdır de




# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# iban_1 = "TR0000000000"
# iban_2 = "TR1111111111"

# k_iban= input("Kendi ibanınızı giriniz: ")
# g_iban= input("Para göndermek istediğiniz ibanı giriniz: ")

# if "TR" in iban_1 and iban_1 == k_iban and "TR" k_iban and "TR" in iban_2== g_iban and "TR"in g_iban:
#      para=float(input("Göndermek istediğiniz para nedir? "))
    
#     if para>0 and para<1000000:
#         print("Paranız gönderildi")
#     else:
#         print("gönderilen para 0 dan küçük veya 1 milyondan fazla olamaz")
        
# else:
#     print("İbanlar uyuşmuyor")
    
    
    
    # kullanıcı kayıt formu için gerekli alanları yaz
    # kullanıcı adı şifre şifre tekrarı mail
    # koşullar 
    # kullanıcı adı en az sekiz karakter olmalı 
    # şifre en az sekiz karakter olmalı ve şifreler uyuşmalı
    # mailde ise "@" işaretinin olması zorunlu. eğer yoksa hatalı desin
    
    

user_name = input("Kullanıcı Adı Oluşturun: ")
sifre = input("Şifre oluşturun:")
sifre_t = input("Şifreyi tekrar giriniz: ")
mail= input("Mail adresinizi giriniz: ")
sifre_uzunluk = len(sifre)
user_name_uzunluk = len(user_name)
if "@" in mail and ".com" in mail : 
    
    if sifre_uzunluk>7 and user_name_uzunluk>=8:
        
        if sifre==sifre_t:
            print("Hesabınız Oluşturuldu")
        
        else:
            print("şifreler uyuşmuyor")
    else:
        print("Şifre ve kullanıcı adı 8 karakter veya daha fazla olmalı")
else:
    print("Mail Hatalı!")