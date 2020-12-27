info=["ALİ","AY"]
tekrar=0
while tekrar<3:
    ad=input("Adınızı giriniz:")
    soyad=input("Soyadınızı giriniz:")
    if ad==info[0] and soyad==info[1]:
        break
    else:
        tekrar+=1
        if tekrar==3:
            print("program sonlandırılıyor...")
            break
        print("Lütfen daha sonra tekrar deneyiniz...")
dersler=[]
derssayisi=1
sayac=0
ders=" "
while True:
    ders=input(f'{derssayisi}. dersi yazınız:'.format(derssayisi))
    derssayisi+=1
    sayac+=1
    if ders=="" and sayac<4:
        print("Ders oluşturulamadı...")
        break
    
    if derssayisi==4:
        devam=input("Ders eklemeye devam etmek istiyor musunuz?(E/H)")
        if devam=="H":
            break
    if derssayisi==5:
        devam=input("Ders eklemeye devam etmek istiyor musunuz?(E/H)")
        if devam=="H":
            break
    dersler.append(ders)
    if derssayisi==6:
        print("Ders seçimi tamamlandı..")
        break
notlar={"midterm":50,"final":50,"project":50}
print(f'{dersler[3]} dersinden aldığınız notlar: Final={notlar["final"]} Midterm={notlar["midterm"]} Project={notlar["project"]}'.format(notlar["final"],notlar["midterm"],notlar["project"]))
puan=(notlar["midterm"]*30/100)+(notlar["final"]*50/100)+(notlar["project"]*20/100)
print(puan)
if puan>=90:
    print("AA")
elif puan>=70:
    print("BB")
elif puan>=50:
    print("CC")
elif puan>=30:
    print("DD")
else:
    print("Maalesef dersten geçemediniz: FF")
