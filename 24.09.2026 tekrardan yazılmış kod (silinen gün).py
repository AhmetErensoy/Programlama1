# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 02:36:35 2026

@author: ahmet
"""
user_name = "Ahmet_123"
mail = "ahmet@mail.com"
tel_no = "0530"
sifre = "1235"
giris_tur = input("Mail veya telefon numarası giriniz: ")
sifre_g = input("Şifrenizi giriniz: ")
kod = "5555"

if giris_tur == mail and sifre == sifre_g:
    print("Giriş başarılı! ")
    
elif giris_tur == tel_no and sifre == sifre_g:
    print("Telefonunuza gelen kod: ",kod)
    g_kod=input("Gelen kodu giriniz: ")
    if g_kod == kod:
        print("Giriş başarılı!")
    else:
        print("Girdiğiniz kod hatalı! ")
    
    
else:
    print("Girdiğiniz bilgiler hatalı! ")
    

