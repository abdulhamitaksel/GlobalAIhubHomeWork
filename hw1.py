deger1=input("Birinci değeri giriniz:")
deger2=input("İkinci değeri giriniz:")
deger3=input("Üçüncü değeri giriniz:")
deger4=input("Dördüncü değeri giriniz:")
deger5=input("Beşinci değeri giriniz:")

#f-string metodu kullanılarak;
print(deger1,f'verisinin türü {type(deger1)}')
print(deger2,f'verisinin türü {type(deger2)}')
print(deger3,f'verisinin türü {type(deger3)}')
print(deger4,f'verisinin türü {type(deger4)}')
print(deger5,f'verisinin türü {type(deger5)}')

#format metodu kullanılarak
print(deger1,"verisinin türü {}".format(type(deger1)))
print(deger2,"verisinin türü {}".format(type(deger2)))
print(deger3,"verisinin türü {}".format(type(deger3)))
print(deger4,"verisinin türü {}".format(type(deger4)))
print(deger5,"verisinin türü {}".format(type(deger5)))
