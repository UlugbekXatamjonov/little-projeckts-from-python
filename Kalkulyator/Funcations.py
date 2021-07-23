from math import *

def kopaytir():
    """Ikki sonni ko'pytiruvchi funksia:"""
    print("Ikki sonni ko'paytiruvchi funksia")
    try:
        kopaytuvchi1 = int(input("1-sonni kiriting: "))
        kopaytuvchi2 = int(input("2- sonni kiriting: "))
    except ValueError:
        print("Butun son kiritmadingiz!  Qaytadan urining.")
    else:
        kopaytma = kopaytuvchi1 * kopaytuvchi2
        print(kopaytma)


def qosh():
    """Ikki sonni qo'shuvchi funksia:"""
    print("Ikki sonni qo'shuvchi funksia")
    try:
        qoshiluvchi1 = float(input("1-sonni kiriting: "))
        qoshiluvchi2 = float(input("2- sonni kiriting: "))
    except ValueError:
        print("Iltimos son kiriting! Va qaytadan urining.")
    else:
        yigindi = qoshiluvchi1 + qoshiluvchi2
        print(yigindi)


def ayr():
    """Ikki sonni ayruvchi  funksia"""
    print("Ikki sonni ayruvchi funksia:")
    try:
        ayriluvchi = float(input("1-sonni kiriting: "))
        ayruvchi = float(input("2- sonni kiriting: "))
    except ValueError:
        print("Iltimos son kiriting! Va qaytadan urining. ")
    else:
        ayrma = ayriluvchi - ayruvchi
        print(ayrma)


def bol():
    """Ikki sonni bo'luvchi  funksia"""
    print("Ikki sonni bo'luvchi funksia:")
    try:
        bolinuvchi = float(input("1-sonni kiriting: "))
        boluvchi = float(input("2- sonni kiriting: "))
    except ValueError:
        print("Iltimos son kiriting! Va qaytadan urining. ")
    if boluvchi == 0.0:
        print("Sonni 0 ga bo'lib bo'lmaydi! Qaytadan urining. ")
            
    else:
        bolinma = bolinuvchi / boluvchi
        print(bolinma)


def darajaga_kotar():
    """"Sonni darajaga ko'taruvchi funksia:"""
    print("Sonni darajaga ko'taruvchi funksia: ")
    try:
        son = float(input("Darajaga ko'tarmoqchi bo'lgan soningizni kiriting: "))
        daraja = float(input("Daraja=" ))
    except ValueError:
        print("Iltimos son kiriting! Va qaytadan urining. ")

    try:
        natija = pow(son,daraja)
        print(natija)
    except OverflowError:
        print("Natija juda ham katta son !!! Men buni hisoblay olmayman. Uzur!")  
 

def ildizdan_chiqar():
    """Sonni ildizdan chiqaruvchi funkisa: """
    print("Sonni ildizdan chiqaruvchi funkisa: ")
    
    try:
        son2 = float(input("ILdizdan chiqarmoqchi bo'lgan soningizni kiriting: "))
    except ValueError:
        print("Iltimos butun son kiriting! Va qaytadan urining. ")
    try:
        natija2 = sqrt(son2)
    except ValueError:
        print("Iltimos butun son kiriting! Va qaytadan urining. ")
    except UnboundLocalError:
        print("Iltimos butun son kiriting! Va qaytadan urining. ")
    else:
        print(natija2)


def sonning_foizi():
    """Sonning foizini ko'rsatuvchi funksia: """
    print("Sonning foizini ko'rsatuvchi funksia: ")
    try:
        son3 = float(input("Soninni kiriting: "))
        son4 = float(input("Sonning necha foizi kerak: "))
    except ValueError:
        print("Iltimos butun son kiriting! Va qaytadan urining. ")
    else:
        natija3 = (son3*son4)/100 
        print(f"{son3} ning {son4}% , {natija3} ga teng bo'ladi.")


