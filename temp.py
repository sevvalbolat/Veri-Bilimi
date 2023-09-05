9
9.2
9+9
9*9
print('hello guys')
"hello AI era"
type(9)
type(9.1)
type("hello ai era")
"a"*9
b="geleceği yazanlar"
c="geleceği yazanlar"
d=9
e=10
d*e
len(b)
b = "geleceği_yazanlar"
b.upper()
b.lower()
b.islower()
b.isupper()
cd = b.upper()
cd.isupper()
cd.islower()
b.replace("a","e")
c = b.replace("a","e")
c.replace("e", "i")
gel_yaz =" geleceği_yazanlar "
gel_yaz.strip()
gel_yaz="geleceği_yazanlar"
gel_yaz.strip("*")
dir(gel_yaz)
gel_yaz.__str__()
gel_yaz[0]
gel_yaz[0:]

birinci_top=input()
ikinci_top=input()
int(birinci_top)+int(ikinci_top)
type()
print("geleceği","yazanlar")
print("geleceği","yazanlar",sep="-")
ifade = "gelecek_geldi"
ifade.replace("i", "ı")
gel_yaz.replace()
type(4)
ifade = "selam"
type(ifade)
ifade = "Merhaba! "
ifade.strip("")
"_Python_".strip("_")
"_Python_".strip("_")
"10" + 2 
"a" + "b"
a = "bu uzun bir metindir"
a[2:5]
notlar = [50,80,89,97]
type(notlar)
liste = ["a",9.30,19]
type(liste)
list_genis = ["a",9.30,19,notlar]
len(list_genis)
list_genis[3]
type(list_genis[3])
tum_liste = [liste,list_genis]
tum_liste[0:]
tum_liste
tum_liste[1][1]
liste = ["ali","ayşe","taha","sevval"]
liste
liste[1]="tuba"
liste
del liste[0]
liste
liste= liste + ["berk"]
liste
dir(liste)
liste.append("aslı")
liste
liste.remove("aslı")
liste
liste.insert(0,"isik")
liste
liste.insert(len(liste),"furkan")
liste
liste.pop(1)
liste=["sevval","sevval","taha","sevval","taha"]
liste
liste.count("sevval")
yedek_liste = liste.copy()
liste.extend([10,50,"a"])
liste
liste.index(10)
liste = [20,78,12,63]
liste.sort()
liste
liste.reverse()
liste
t = ("ali","veli",1,2,3.2,[1,2,3,4])
t
type(t)
t = ("sevval",)
type(t)
sozluk = {"REG" : "Regresyon Model", 
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Red"}
sozluk
sozluk =  {"REG" : 10,
           "LOG" : 20,
           "CART" : 30}
sozluk
sozluk = {"REG" : ["RMSE",10],
          "LOG" : ["MSE",20],
          "CART": ["SSE",30]}
sozluk = {"REG" : "Regresyon Model", 
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Red"}
sozluk["GBM"] = "Gradient Boosting Mac"
sozluk

#set oluşturma
s = set()
s
l = [1,"a","ali",123]
s = set(l)
s
t = ("a","ali")
s = set(t)
s
ali = "lutfen_ata_bakma_uzaya_git"
type(ali)
s = set(ali)
s
len(s)
l = ["geleceği","yazanlar"]
s = set(l)
s
s.add("ali")
s
set1 = set([1,3,5])
set2 = set([1,2,3])
set1.difference(set2)
set2.difference(set1)

set1 = set([1,3,5])
set2 = set([1,2,3])
set1.intersection(set2)
set2.intersection(set1)
kesisim = set1 & set2
kesisim
birlesim = set1.union(set2)
birlesim
set1.intersection_update(set2)
set1
liste = ["a","b","c"]
liste.extend(liste)
liste

liste = [10,10,20,40]
liste.clear()
liste

set1 = set([5,7,9])
set2 = set([5,6,7])
set1.symmetric_difference(set2)

set1 = set([5,7,9])
set2 = set([5,6,7])
set1.union(set2)

def kare_al(x):
    print(x**2)
    
    kare_al(3)

def kup_Al(x):
    print("Girilen sayının kupu:" + str(x**3))
    
    kup_Al(2)
    
def kare_al(x):
    print("Girilen sayı:" + str(x) + " Sayının karesi:" + str(x**2))

kare_al(5)

def carpma(x,y):
    print(x*y)
    
    carpma(2,3)

def direk_hesap(ısı,nem,sarj):
    print((ısı+nem)/sarj)
    
    direk_hesap(20,78,45)
 
    def direk_hesap(ısı,nem,sarj):
        return((ısı+nem)/sarj)
    cikti = direk_hesap(20,70,80)
    print(cikti)
    
x = []
def eleman_ekle(y):
    x.append(y)
    print(str(y) + " elemanı eklendi")
eleman_ekle("sevval")
eleman_ekle("taha")
x

#if
sinir = 50000
gelir = 50000
gelir < sinir
if gelir < sinir:
    print("gelir sınırın altında")
elif gelir > sinir:
    print("gelir sınırın üstünde")
else:
    print("gelir sınıra eşittir")

#Örnek Uygulama
sinir = 5000
magaza_adi = input("mağaza adı nedir: ")
gelir = int(input("mağaza gelirini giriniz: "))
if gelir > sinir:
    print(magaza_adi + " geliri sınırı aştı")
elif gelir < sinir:
    print(magaza_adi + " gelir sınırı geçememiş")
else:
    print(magaza_adi + " tam sınırda")
    
#for
ogrenci = ["sevval","ali","veli","taha"]
for i in ogrenci:
    print(i)
    
maaslar = [15000,20000,30000,7000]
for i in maaslar:
    print(i)
    
#uygulama
maaslar = [1000,2000,3000,4000]
def yeni_maas(x):
    print(x*20/100 + x)
for i in maaslar:
    yeni_maas(i)
    
#uygulama-2
maaslar = [1000,2000,3000,4000,5000]
def maas_ust(x):
    print(x*10/100 + x)
def maas_alt(x):
    print(x*20 / 100 + x)
    
for i in maaslar:
    if i >=3000:
        maas_ust(i)
    else:
        maas_alt(i)
        
maaslar = [1000,9000,7000,5002,4200,6400,7400,8500]
maaslar.sort()
maaslar

for i in maaslar:
    if i < 7000:
        continue
    print(i)
    
    
for i in maaslar:
    if i >6000:
        print("kesildi")
        break
    print(i)
    
sayi = 1
while sayi < 10:
    sayi += 1
    print(sayi)
    
sayilar = [10,20,30]
 
for i in sayilar:
    if i > 20:
        print(i/2)
        
def islem(x):
    if (x<0):
        return "NO"
    else:
        print(x*5)
 
islem(2)

liste = ["a","b","c"]
liste.reverse()
print(liste)

def mesaj():
    print("Merhaba!")    
    
mesaj() 

def harf_say(x):
len(x)
 
harf_say("Merhaba!")

A = "*A*"    
if type(A) == str:
    A = A.strip("*")
    print(A)
    
?print

def islem(x, y):
    print(x - y)

islem(3)

A = []

for i in [1,2,3,4]:
    A.append(i)

A[0]

def harf_say(x):
    return len(x)
 
harf_say("Merhaba!")

A = 12    
if type(A) == str:
    A = A.strip("*")
    print(A)    
else:
    A  = "*" + str(A) + "*"
    print(A.strip())
    
for i in ["a",11]:
    print(i)
    
sayilar = [10,20,30,40]
 
for i in sayilar:
    if i == 30:
        break
    print(i)
    
def harf_say(x):
    len(x)
 
harf_say("Merhaba!")

if [1,2,3,4][1] == 2:
    print("YES".lower())
else:
    print("NO")   
    
def abs(*args, **kwargs):
    """Return the absolute value of the argument"""
pass

name = "VBO_Bootcamp"
type = "new_term"
f"Name:{name} type:{type}"

#class
class VeriBilimci():
    print("bu bir sınıftır")
    
#class attribute(özellikleri)
class VeriBilimci():
    bolum = "engineer"
    sql ="Evet"
    deneyim_yili = 0
    bildigi_diller =[]
    
VeriBilimci.bildigi_diller
VeriBilimci.bolum    
VeriBilimci.sql

#sınıf örneklendirmesi(instantiation)
ali = VeriBilimci
ali.bolum
ali.bildigi_diller.append("python")

veli = VeriBilimci
veli.deneyim_yili

#sınıf örneklendirmesi örnekleri
def __init__(self):
    self.bildigi_diller = []
    self.bolum = ''
    
ali = VeriBilimci()    
ali.bildigi_diller.append("R")
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller.append("python")
veli.bildigi_diller

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self,yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        
ali = VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

ali = VeriBilimci()
ali.dil_ekle("R")
ali.bildigi_diller

veli = VeriBilimci()
veli.dil_ekle("Python")
veli.bildigi_diller

#miras alma(inheritance)
class Employee():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""
        
class DataScience(Employee):
    def __init__(self):
        self.Programming = ""
        
class Marketing(Employee):
    def __init__(self):
        self.StoryTelling = ""
        
class Employee_new():
    def __init__(self,FirstName,LastName,Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address
        
#Bağımsızlık
A = 9
def impure_sum(b):
    return b + A

impure_sum(6)

def pure_sum(a,b):
    return a + b

pure_sum(8,4)

#isimsiz fonksiyonlar
sirasiz_liste = [('b',3),('a',8),('d',12),('c',1)]
sirasiz_liste

sorted(sirasiz_liste, key = lambda x: x[1])


import numpy as np
s = np.array([1,2,3,4])
t = np.array([2,3,4,5])
s*t

liste = [1,2,3,4,5]
list(map(lambda x: x*10, liste))

liste = [1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x:x % 2 == 0,liste))

from functools import reduce
list =[1,2,3,4]
reduce(lambda a,b: a+b,liste)

#zeroDevisionError
a = 10
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print("paydada 0 olmaz")
    
A = []
for i in ["ali","veli","isik"]:
    A.append(i.replace("i","a"))
print(A)

list(filter(lambda x: x < 2, [1,2,3,4,5]))

fun = lambda x: x**2
fun(3)

from functools import reduce
a = [1,2,3,4]
reduce(lambda a,b: a*b, a)

from functools import reduce
reduce(lambda a,b: a/b, [8,4,2])

from functools import reduce
reduce(lambda a,b: a+b, ["a","4","a"])

def yap(x,y,z):
    try:
        print(x/y*z)
    except ZeroDivisionError:
        print("gecersiz islem")

yap(1,2,0)

list(map(lambda x: x*1, [2,7,4]))


help(print)

def summer(arg1,arg2):
    print(arg1 + arg2)
summer(9,8)
