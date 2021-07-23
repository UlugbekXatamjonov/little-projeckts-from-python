# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:50:36 2021

@author: Ulug'bek
"""

# Restoran uchun MealGuide dasturi

mijozlar = []
buyurtmalar = []

def ummumiy_malumot(): 
    info = "Assalomu ayeykum!\n"
    info += "'Fayz' restoraniga hush kelibsiz!\n"
    info += "Bizning restoran o'z mijozlariga 15 yildan buyon o'z hizmatini ko'rsatib kelmoqda. " 
    info += "Shu vaqtdan buyon restoranimiz o'zining mingdan ziyod doimiy mijozlariga hamda o'z qadiryatlariga ega bo'ldi. "
    info += "Restoranimiz bir vaqtning o'zida 500 kishini o'z bag'riga sig'dira oladi va ularni mamnun qila oladi. "
    info += "Sizni ham bizning doimiy mijozlarimiz qatoriga qo'shilishingizdan mamnunmiz!"
   
ummumiy_malumot()            


def buyurtma_ol():
    mijozlar = list(range(int(input("Stol atrofida necha nafar mijoz bor: "))))
    
    taom1 = {'Osh':10000,"Norin":12000,"Kabob":7000,"Somsa":5000,"Qovurilgan Baliq":11000,"Dimlama":8000,"Qotirma":8000,"Bishtexs":6000}
    taom2 = {"Qozon kabob":9000,"Uyg'ur Lag'mon":8000,"sho'rva":6000,"Mastava":6000,"Lag'mon":6000}
    disert = {"Pirojni":4000,"Mazzaloi yogurt":3000,"Qaymoqli musqaymoq":5000,"Shirinlik":6000,"Issiq shkolad":3000,}
    ichimlik = {"Qora choy":2000,"Kok choy":2000,"Suv":0,"Qora qahva":3000,"Sutli qahva":3000,"Pepsi":7000,"Coca Cola":5000,"Fanta":5000,"Dena":4000,"Bliss":5000,"Tabiy sharbat":7000,"Limonat":4000,"Gali suv":3000,"Shampan vinosi":12000}
    
    print("Marhamat bizning Menu: ")
    royhat = ["Birinchi taom","Ikkinchi taom","Disertlar","Ichimliklar"]
    print(f"Birinchi taom: \n {taom1} \n Ikkincchi taom: \n {taom2} \n Disertlar: \n {disert} \n Ichimliklar: \n {ichimlik}")
    
    while True:
        for m in mijozlar:
            print(f"Hurmatli {m+1}-mijoz.")
            buyurtma1 = input("Marhamat birinchi taomni tanlang: ")
            buyurtma1 = buyurtma1.title()
            buyurtma2 = input("Marhamat ikkinchi taomni tanlang: ")
            buyurtma2 = buyurtma2.title()
            buyurtma3 = input("Marhamat disertni tanlang: ")
            buyurtma3 = buyurtma3.title()
            buyurtma4 = input("Marhamat ichimlikni tanlang: ")
            buyurtma4 = buyurtma4.title()
           
            m=m+1
        if m != mijozlar:
            break
        




























