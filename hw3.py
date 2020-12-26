#                              TAŞ----KAĞIT----MAKAS
secenek=["taş","kağıt","makas"]
tas=secenek[0]
kagit=secenek[1]
makas=secenek[2]
ad=input("Adınızı giriniz:")
ad=ad.upper()
skorkul=0
skorbil=0
print(f'Taş-Kağıt-Makas oyununa hoş geldiniz {ad}!!!')
import random
while True:
    secim=input("Taş mı Kağıt mı Makas mı?(Çıkış için 'q')")
    if secim=="q":
        print("Oyundan çıkılıyor...")
        print(f'{ad} {skorkul} : {skorbil} Bilgisayar'.format(ad,skorkul,skorbil))
        break
    otosecim=random.choice(secenek)
    if secim==tas:
        if otosecim==tas:
            print("Bilgsayarın seçimi  Taş: Berabere...")
        elif otosecim==kagit:
            print("Bilgsayarın seçimi  Kağıt: Bilgisayar kazandı...")
            skorbil+=1
        elif otosecim==makas:
            print("Bilgsayarın seçimi  Makas: Tebrikler kazandınız...")
            skorkul+=1
    if secim==kagit:
        if otosecim==kagit:
            print("Bilgsayarın seçimi  Kağıt: Berabere...")
        elif otosecim==tas:
            print("Bilgsayarın seçimi  Taş: Tebrikler kazandınız...")
            skorkul+=1
        elif otosecim==makas:
            print("Bilgsayarın seçimi  Makas: Bilgisayar kazandı...")
            skorbil+=1
    if secim==makas:
        if otosecim==makas:
            print("Bilgsayarın seçimi  Makas: Berabere...")
        elif otosecim==tas:
            print("Bilgsayarın seçimi  Taş: Bilgisayar kazandı...")
            skorbil+=1
        elif otosecim==kagit:
            print("Bilgsayarın seçimi  Kağıt: Tebrikler kazandınız...")
            skorkul+=1
