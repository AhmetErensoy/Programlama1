# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:12:48 2026

@author: ahmet
"""

# ogrenciler=[]
# sinif={"ad":"ahmet"}
# ogrenciler.append(sinif)
# print(sinif[0]["ad:"])
"""
kullanıcılar diye bir dizi oluştur, oluşturmuş olduğun kullanıcılar dizisine,
kullanıcı adı şifre mail anahtarlarını içeren bir sözlük oluştur sözlüğe en az bir veri girerek ekranda gösteriniz:
"""

# kullanıcılar=[{"ad":"test1","sifre":"12345","mail":"test1@mail.com"},{"ad":"test2","sifre":"1234567","mail":"test2@mail.com"}]
# print(kullanıcılar[0]["mail"])
"""
birinci indeksteki tüm key değerleri ekranda yazılsın
"""
# kullanıcılar=[{"ad":"test1","sifre":"12345","mail":"test1@mail.com"},{"ad":"test2","sifre":"1234567","mail":"test2@mail.com"}]
# print(kullanıcılar[1]["ad"],kullanıcılar[1]["mail"],kullanıcılar[1]["sifre"])
# döngü ile tüm elemanları göster


# kullanıcılar=[{"ad":"test1","sifre":"12345","mail":"test1@mail.com"},{"ad":"test2","sifre":"1234567","mail":"test2@mail.com"}]
# for bilgiler in kullanıcılar:
#     print("Kullanıcı adı: ", kullanıcılar[0]["ad"])
#     print("Şifre: ",kullanıcılar[0]["sifre"])
#     print("mail adresi:",kullanıcılar[0]["mail"])

"""İstenen çözüm alltaki"""

kullanıcılar=[{"ad":"test1","sifre":"12345","mail":"test1@mail.com"},{"ad":"test2","sifre":"1234567","mail":"test2@mail.com"}]
for kullanıcı in kullanıcılar:
    print(kullanıcı["ad"],kullanıcı["sifre"],kullanıcı["mail"])
    
    
    # döngüler,değişkenler ve karar yapıları ile ilgili teorik bilgiler
    python dictionary hakkında araştırma yap

    
    
    
    
    
    
    
    