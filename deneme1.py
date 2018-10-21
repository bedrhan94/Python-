def toplamciro(birim,miktar):
    global ciro
    ciro=miktar*birim
    return ciro
satis_miktari=int(input("Satiş Miktarini Giriniz = "))
birim_miktari=int(input("Kaç Birim Olduğunu Giriniz = "))
sonuc=toplamciro(satis_miktari,birim_miktari)
calisan_sayi=25
kisibasiciro=sonuc/calisan_sayi
print(kisibasiciro)
