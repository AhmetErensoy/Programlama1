# bir apt ye gelen istek sayısı saniyede 5'i geçmemelidir

# requestCount değişkenindeki değeri kontrol ederek limit aşılmışsa
#  "limit aşıldı" aksi durumda "istek kabul edildi" yazdıran 
#  python kodunu yazınız
'''
x = int(input("Saniyede kaç istek geldi"))
if x<=5:
    print("İstek kabul edildi")
else:
    print("limit aşıldı")
'''

#bir e ticaret sisteminde müşterinin alışveriş tutarı 1000tl üzerindeyse %20.
# 500tl ile 1000 tl arasındaysa ¶%10 indirim uygula
"""
fiyat=int(input("Fiyat ne?: "))
b_indirim=20
k_indirim=10

if fiyat>=1000:
    print("İndirim kazandınız: %20 yeni fiyat: ",fiyat-(fiyat*b_indirim/100) )
elif fiyat>=500 and fiyat<1000:
    print("İndirim kazandın. %10 yeni fiyat: ", fiyat-(fiyat*k_indirim/100))
else:
    print("indirim yok")
"""

sayfa_1= "ilk sayfadaki kayıtlar"
sayfa_2= "ikinci sayfadaki kayıtlar"
sayfa_3= "üçüncü sayfadaki kayıtlar"
sayfa_4= "dördüncü sayfadaki kayıtlar"
sayfa_5= "beşinci sayfadaki kayıtlar"
while True:
    x=int(input("Sayfa sayısını giriniz: ")) 
    if x==1:
        print(sayfa_1)
    elif x==2:
        print(sayfa_2)
    elif x ==3:
       print(sayfa_3)
    elif x ==4:
       print(sayfa_4)
    elif x ==5:
       print(sayfa_5)
    else:
        print("böyle bir sayfa yok")
        
        