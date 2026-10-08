# -*- coding: utf-8 -*-
"""

# for sayi in range(0,101):
#     print(sayi)
    
# for sayi in range(5,101,2):
#     print(sayi)
Created on Mon Sep 28 09:13:18 2026

@author: ahmet
"""

# birden yüze kadar olan tüm sayıları ekrana yazdır
    
# kullanıcıdan döngünün kaçta başlamasını istediğini sor kaça kadar devam edeceğini 
# sor ve artış miktarını sor girdilere göre döngüyü çalıştırıp sayıları ekrana yansıt

"""basla = int(input("Döngünün başlangıcını giriniz: "))
son = int(input("Döngünün kaçta bitmesini istediğinizi giriniz: ")) + 1
artis = int(input("Artış miktarını giriniz: "))

if basla < son:
    for sayi in range(basla,son,artis):
        print(sayi)

else:
    print("Başlangıçtaki sayı son sayıdan küçük veya eşit olamaz!")
"""

#while kullanarak

"""while True:
    basla = int(input("Döngünün başlangıcını giriniz: "))
    son = int(input("Döngünün kaçta bitmesini istediğinizi giriniz: ")) + 1
    artis = int(input("Artış miktarını giriniz: "))
    if basla < son: 
        for sayi in range(basla,son,artis):
            print(sayi)
        break
    else:
        print("Başlangıç bitişten küçük veya eşit olamaz! ")
        """
        
# """kullanıcı adı ve şifre al kullanıcı adı test şifre de birden dokuza kadar ise 
# hoşgeldin kullanıcı de değilse kullanıcı adı veya şifre yanlış de 
# kullanıcının giriş yapabilmesi için 3 defa yanlış giriş hakkı ver
# eğer 3 kere yanlış girerse giriş hakkın bitti de"""

"""
user_name = "test"
sifre = "123456789"
i = 0
while i<3:   
        g_user_name = input("Kullanıcı adını giriniz: ")
        g_sifre = input("Şifreyi giriniz: ")
        if g_user_name == user_name and g_sifre == sifre:
            print("Giriş başarılı! ")
            break
        else:
            print("Şİfre veya kullanıcı adı hatalı")
            i+=1
"""

#kullanıcı 50 sayısını girene kadar kullanıcıdan sayı girmesini iste

# while True.:
    
    
#kullanıcı en fazla 10 tahmin yapabilir her tahminde kaç hakkı kaldığını belirt
#10 dan fazla tahmin yapamasın

"""
i = 0
while i<10:
    sayi = int(input("Sayı gir: "))
    if sayi == 50:
        print("Doğru")
        break
    else:
        i+=1
        print("Kaç defa denedin: ",i)
        
    """
#sabit bir fatura numarası oluştur bir de fatura tutarı oluştur
#kullanıcıya ödemek istediğin fatura numarasını gir de ondan numarayı al
#kullanıcı ödemek istediği tutarı da girsin
#hesap numarası yanlış girilmişse
# kullanıcı doğru hesap numarasını girene kadar hesap numarasını sor
#fatura tutarından büyük veya küçük odeme yaptığında ise
# yine doğru girene kadar tekrar sor
#eğer tüm koşullar doğruysa ödeme gerçekleşsin ve döngüden çık
 
#buradan alttaki kodlar tamamlanmadı. Hatalı olabilir;
fatura_num = "12345678"
fatura_tutar = "80" 

while True:
    g_fatura_num = input("fatura numarasını girin: ")
    print("Fatura tutarınız: ",fatura_tutar)
    if fatura_num == g_fatura_num:
        break
    else:
        print("Fatura numarası hatalı")
        
while True:
    g_fatura_tutar = input("Ödemek istediğiniz tutarı giriniz: ")
    if g_fatura_tutar == fatura_tutar:
        print("Ödeme gerçekleşti")
        
    
    