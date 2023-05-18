# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:25:16 2023

@author: Eren Ulubay - 22210201050

"""

import colorama
from colorama import Fore
colorama.init(autoreset=True)
import time

ogrenciler = []
ogrenciSayisi = 0

while True:
    print(Fore.BLUE + "  -----------------------------------")
    print(Fore.BLUE + "  |" , Fore.RED + "1 - Öğrenci Ekle               ", Fore.BLUE + "|")
    print(Fore.BLUE + "  |" , Fore.RED + "2 - Öğrenci Düzenle            ", Fore.BLUE + "|")
    print(Fore.BLUE + "  |" , Fore.RED + "3 - Öğrencileri Listele        ", Fore.BLUE + "|")
    print(Fore.BLUE + "  |" , Fore.RED + "4 - Öğrenci Sayısını Öğren     ", Fore.BLUE + "|")
    print(Fore.BLUE + "  |" , Fore.RED + "5 - En Büyük Boyu Öğren        ", Fore.BLUE + "|")
    print(Fore.BLUE + "  |" , Fore.RED + "6 - En Küçük Boyu Öğren        ", Fore.BLUE + "|")
    print(Fore.BLUE + "  |" , Fore.RED + "7 - Boyların Toplamını Öğren   ", Fore.BLUE + "|")
    print(Fore.BLUE + "  |" , Fore.RED + "8 - Boyların Ortalamasını Öğren", Fore.BLUE + "|")
    print(Fore.BLUE + "  |" , Fore.RED + "9 - Programı Kapat             ", Fore.BLUE + "|")
    print(Fore.BLUE + "  -----------------------------------\n")

    secim = input(Fore.GREEN + "   Ne Yapmak İstiyorsun : ")
    
    print(Fore.BLUE + "  -----------------------------------\n")

    if secim == "1":
        isim = input(Fore.YELLOW + "   Öğrencinin ismi : ")
        numara = input(Fore.YELLOW + "   Öğrencinin numarası : ")
        boy = int(input(Fore.YELLOW + "   Öğrencinin boyu : "))
        ogrenci = {"isim": isim, "numara": numara, "boy": boy}
        ogrenciler.append(ogrenci)
        ogrenciSayisi += 1
        print(Fore.MAGENTA + "   Öğrenci Başarıyla Kaydedildi.\n")

    elif secim == "2":
        index = int(input("   Değiştirilecek öğrencinin indisini girin (1-{} arası): ".format(ogrenciSayisi)))
        if index < 1 or index > ogrenciSayisi:
            print("   Lütfen Doğru bir indis girin.\n")
            continue
        index -= 1
        isim = input(Fore.YELLOW + "   öğrencinin ismi : ")
        numara = input(Fore.YELLOW + "   öğrencinin numarası : ")
        boy = int(input(Fore.YELLOW + "   öğrencinin boyu : "))
        ogrenci = {"isim": isim, "numara": numara, "boy": boy}
        ogrenciler[index] = ogrenci
        print(Fore.MAGENTA + "   Öğrenci Başarıyla Değiştirildi.\n")

    elif secim == "3":
        if ogrenciSayisi == 0:
            print(Fore.RED + "   Kayıt Edilen Öğrenci YOK!\n")
        else:
            for i in range(1, ogrenciSayisi + 1):
                print(Fore.RED + f"   {i}. Öğrenci: ",
                      Fore.CYAN + f"İsim: ",Fore.YELLOW + f"{ogrenciler[i-1]['isim']} ",
                      Fore.CYAN + f"Numara: ",Fore.YELLOW + f"{ogrenciler[i-1]['numara']} ",
                      Fore.CYAN + f"Boy: ",Fore.YELLOW + f"{ogrenciler[i-1]['boy']}")
            print()


    elif secim == "4":
        print(Fore.YELLOW + f"   Öğrenci sayısı: {ogrenciSayisi}\n")

    elif secim == "5":
        if ogrenciSayisi == 0:
            print(Fore.RED + "   Kayıt Edilen Öğrenci YOK!\n")
        else:
            en_buyuk_boy = max(ogrenciler, key=lambda x:x["boy"])["boy"]
            print(Fore.YELLOW + f"   En büyük boy: {en_buyuk_boy}\n")

    elif secim == "6":
        if ogrenciSayisi == 0:
            print(Fore.RED + "   Kayıt Edilen Öğrenci YOK!\n")
        else:
            en_kucuk_boy = min(ogrenciler, key=lambda x:x["boy"])["boy"]
            print(Fore.YELLOW + f"   En küçük boy: {en_kucuk_boy}\n")

    elif secim == "7":
        if ogrenciSayisi == 0:
            print(Fore.RED + "   Kayıt Edilen Öğrenci YOK!\n")
        else:
            boy_toplami = sum(ogrenci["boy"] for ogrenci in ogrenciler)
            print(Fore.YELLOW + f"   Öğrencilerin boy toplamı: {boy_toplami}\n")

        
    elif secim == "8":
        if ogrenciSayisi == 0:
            print(Fore.RED + "   Kayıt Edilen Öğrenci YOK!\n")
        else:
            boy_ortalama = sum(ogrenci["boy"] for ogrenci in ogrenciler) / ogrenciSayisi
            print(Fore.YELLOW + f"   Öğrencilerin boy ortalaması: {boy_ortalama}\n")

    elif secim == "9":
        print(Fore.RED + "   Program 5 Saniye İçerisinde Sonlandırılacaktır...")
        time.sleep(1)
        print(Fore.YELLOW + "       1       - ", end=" ")
        time.sleep(1)
        print(Fore.BLUE +   "       2       - ", end=" ")
        time.sleep(1)
        print(Fore.GREEN +  "       3       - ", end=" ")
        time.sleep(1)
        print(Fore.CYAN +   "       4       - ", end=" ")
        time.sleep(1)
        print(Fore.MAGENTA +"       5         ", end=" ")
        time.sleep(1)
        break

    else:
        print(Fore.RED + "   Lütfen Doğru bir seçim yapın.\n")

    input("   Başka İşlem Yapmak İstiyorsan ENTER Bas...")
    print("\n" * 50)



