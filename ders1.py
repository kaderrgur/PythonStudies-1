#SAYILAR VE STRİNGLERE GİRİŞ
print("HELLO AI")
"HELLO AI"
'HELLO AI'

9
9,2
9.2
9*9

type(9)
type("Kader")

#STRİNGLERE YAKINDAN BAKALIM
123
type(123)
"123"
type("123")

"a"+"b"
"a""b"
"a"*3
"a "*3

#STRİNG METODLARI-LEN
a="gelecegi_yazanlar"
len(a)
len("gelecegi_yazanlar")

#UPPER-LOWER
a.upper()
a.lower()
a.islower() #hepsi küçük mü
a.isupper() #hepsi büyük mü

#REPLACE
a.replace("e","a") #karakter değiştirme

#STRİP default olarak cümledeki boşlukları kırpar
a="*gelecegi_yazanlar*"
a.strip("*") #baştaki ve sondaki istenmeyen karakterleri kırpar

#METODLARA GENEL BAKIŞ
dir(str) #elimizdeki veri tipine uggulanabilecek olan veri tiplerini verir
dir(a)

a.capitalize() #baş harfi büyütür
a.title() #her kelimenin baş harfini büyütür

#SUBSTRİNGLER
a[0] #ilk karakteri getirir
a[:3] #ilk üç karakteri getirir
a[14:]
a[3:7]

#DEĞİŞKENLER
x=9999
y="KADER"
x*6

type(100)
type(100.2)
type(100+2j)

#TİP DÖNÜŞÜMÜ
sayi1=input()
sayi2=input()
type(sayi1)
type(int(sayi1))

#PRİNT
print("geleceği","yazanlar", sep = "_")
?print #detaylı özellikler getirilir

#VERİ YAPILARI
#LİSTELER
notlar=[90,80,70,50]
type(notlar)
liste=["a", 6, 2.18, ["m"]]
type(liste[0])

tumliste=[notlar,liste]
liste[0]
tumliste[1][1] #listenin içindeli listenin elemanına ulaşma

liste1=["ali", "veli", "kader", "kerem"]
liste1[1]="velinin babası" #liste elemanlarını değiştirme
liste1[0:3]="alinin babasi","velinin babasi","berkcanın babası"

liste1=liste1 + ["kemal"] #listeye eleman ekleme
liste1

del liste1[0] #listeden eleman silme
liste1

#methodlar ile ekleme silme
liste2=["a", "b", "c"]
liste2.append("d") #eleman ekleme
liste2

liste2.remove("d") #eleman silme
liste2

#indekse göre eleman ekleme silme
liste2.insert(0,"a") #ilk indekse eleman ekledik
liste2
liste2.insert(len(liste),"d") #listenin en sonuna eklemiş olduk
liste2

liste2.pop(0) #ilk indeksi silme
liste2

liste2.count("a") #belirtilen elemandan kaç tane olduğu  

liste3=liste2.copy() #listenin kopyasını oluşturduk

liste2.extend(liste3) #iki listeyi birleştirme

liste3.index("b") #verilen elemanın kaçıncı indekste olduğunu verir

liste3.reverse() #elemanları terse çevirir
liste3

liste3.sort() #listeyi küçükten büyüğe sıralar. değişkenler aynı türde olmalı
liste3

#TUPLE-DEMET değişiklik yapılamaz
t=("kader", "kerem", 1, [1,2,3])
t1="kader", "kerem", 1, [1,2,3]
t2=("eleman",) #sonuna virgül koymazsak str olarak alır
t[0]
t[0:3]

#SÖZLÜK-DİCTİONARY sıralama yapılamaz, indeksleme yoktur
sozluk={"kader":"Kader Gur", 
        "kerem":"kerem Gur"}
len(sozluk)
sozluk["kader"] #eleman seçme anahtar kelimeler ile yapılır

dir(dict)
sozluk1={"A":{"B":10, #sözlük içinde sözlük
             "C":20,
             "D":30},
        "E":40,
        "F":50}
sozluk1["A"]["D"] #iç içe sözlükte eleman çağırma

sozluk["furkis"] = "furkan" #yeni eleman ekleme
sozluk["kerem"] = "keros" #guncelleme

#SETLER-KÜME eşşsiz değerlerden oluşur ve performansı yüksektir. indeksleme yok
s=set()
l=[1,"a",10.5]
s=set(l)
t=("a",1)
s1=set(t)
a="kerem okula gitti"
s2=set(a) #her harfi birer kez aldı

l=["gelecegi", "yazanlar"]
s=set(l)
s
s.add("ile") #eleman ekleme
s
s.remove("ile") #eleman silme
s
#difference kümelerin farkını alma
set1=set([1,2,3])
set2=set([1,3,5])
set1.difference(set2) #♠set1 de olup set2 de olamyan elemanları getirir
set1-set2
set2-set1

set1.symmetric_difference(set2) #ikisinin de farklı olan elemanları
#intersection-union
set1.intersection(set2) #kesişim. eğer güncellemek istersek intersection_update fonksiyonu kullanılır
set1&set2

set1.union(set2) #birleşim
set1|set2
#sorgu işlemleri
set1.isdisjoint(set2) #iki kümenin kesişimi boş mu
set1.issubset(set2) #bir kümenin TÜM elemanlarının başka bit küme içerisinde yer alıp almadığı yanı alt kümesi olup olmadığı
set1.issuperset(set2) #set1, set2'yi kapsıyor mu

#FONKSİYONLAR
print("a","b", sep="_")

def kare_al(x):
    print(x**2)
kare_al(2)

def kareal(y):
    print("Girilen sayının karesi: " + str(y**2)) #stringe çevrilmesi gerek
kareal(3)

def kareal1(z):
    print(str(z) + " sayısının karesi: " + str(z**2) + " dir.")
kareal1(4)

def carpma(x, y):
    print(x*y)
carpma(2, 3)

def carpmayap(x, y=1):
    print(x*y)
carpmayap(2)

def hesap(isi, nem, sarj):
    return (isi+nem)/sarj #2eğer fonk. çıktısını başka bir fonk. girdisi olarak kullanacaksak return kullanılır
hesap(25,45,30)*10

#LOKAL VE GLOBAL DEĞİŞKENLER
x=[]
def elemanekle(y): #global alana lokal alandan eleman ekleme
    x.append(y)
elemanekle(2)

#KOŞUL YAPILARI
a=5
a==6
a==5

x=40
y=50
if x<y:
    print("x, y'den küçüktür.")
elif x>y:
    print("x, y'den büyüktür")
else :
    print("x ve y eşittir")
    
#MİNİ UYGULAMA
sinir=50000
magazaadi = input("Mağaza adi nedir?: ")
gelir = int(input("Gelirinizi Giriniz?: "))
if gelir>sinir:
    print("Tebrikler! " + magazaadi + "promosyon kazandiniz! ")
elif gelir<sinir:
    print("Çok düşük gelir! " + str(gelir))
else:
    print("Takibe devam! ")
    
#DÖNGÜLER
ogrenci=["ali", "veli", "kader", "kerem"]
for i in ogrenci:
    print(i)

maaslar=[1000,2000,3000,4000,5000]
for i in maaslar:
    print(i*2)
    
#MİNİ UYGULAMA
maaslar=[1000,2000,3000,4000,5000]
def zam(q):
    print(q*1/5+q)
for i in maaslar:
    zam(i)
    
#MİNİ UYGULAMA
maaslar=[1000,2000,3000,4000,5000]
def zam1(a):
    print(a*1/3+a)
def zam2(a):
    print(a*1/4+a)
def zam3(a):
    print(a*1/5+a)
for i in maaslar:
    if i<3000:
        zam1(i)
    elif i>3000:
        zam3(i)
    else:
        zam2(i)
        
#BREAK VE CONTİNUE
maaslar=[1000,2000,3000,4000,5000]
maaslar.sort() #küçükten büyüğe sıralama
maaslar
for i in maaslar:
    if i==3000:
        print("kesildi")
        break #donguyu sonlandırır
    print(i)

for i in maaslar:
    if i==3000:
        print("kesildi")
        continue # o kısmı atlar
    print(i)

sayi=1
while sayi<10:
    sayi+=1
    print(sayi*2)
    
    
#NOT
def islem(x,y):
    A = [x,y]
    return A[0] + A[1]
 islem(1,3)
 
#CLASS
#Sınıflar benzer özellikler ortak amaçlar taşıyan, içerisinde metod veya değişkenler olan yapılardır.
class veribilimci():
    print("Bu bir sınıftır")
    bolum=''
    sql='Evet'      #sınıfların özellikleri
    deneyim=0
    dil=[]
  
veribilimci.bolum
veribilimci.sql     #sınıfların özelliklerini çağırma

veribilimci.sql='Hayir' #sınıf özelliklerini depğiştirme
veribilimci.sql

kader=veribilimci() #sınıf örneklendirmesi
kader.sql
kader.dil.append("Python")  #sınıfın içine ekledi, bundan sonraki tüm kayıtlara getirir
kader.dil
kerem=veribilimci()
kerem.dil

#yukarıdaki sorunu çözmek için; yani sınıf özelliklerini belirlemek için kulalnılır
class veribilimci():
    def __init__(self):     #örnek özelliği tanımlama, self örnekleri temsil eder
        self.dil=[]
kader.dil.append("Python")  #sınıfın içine ekledi, bundan sonraki tüm kayıtlara getirir
kader.dil
kerem=veribilimci() 
kerem.dil            #böylelikle sadece kadere python eklendi
kerem.dil.append("R")
kerem.dil
veribilimci.dil
veribilimci.bolum
kader.bolum='Bilişim'
veribilimci.bolum
kerem.bolum
kerem.bolum='Bilgisayar'

#ornek metodları
class veribilimciler():
    calisanlar=[]
    def __init__(self):     #örnek özelliği tanımlama
        self.diller=[]
        self.bolumu=''
    def dilekle(self, yenidil):
        self.diller.append(yenidil)
dir(veribilimciler)

kader=veribilimciler() 
kader.dilekle("R")    #calışana dil eklenmiş oldu
kader.diller

#MİRAS YAPILARI
class Employees():
    def __init__(self, FirstName, LastName, Address):
        self.FirstName=FirstName
        self.LastName=LastName
        self.Address=Address
        
class DataScience(Employees):  #miras yapısı kullanıldı
    def __init__(self):
        self.Programming=""
DataScientists1=DataScience()
DataScientists1.

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling=""
Marketing1=Marketing()        
Marketing1.        
  
kader=Employees("KADER", "GÜR", "BİLECİK")      
kader.FirstName

#FONKSİYONEL PROGRAMLAMA
A=5
def impure_sum(b):  #dışardan bağımlılığı olan fonksiyon, yan etki
    return A+b       
impure_sum(6) 

def pure_sum(a,b):
    return a+b
pure_sum(5,6) 

#isimsiz fonksiyonlar
sirasizliste=[('b', 3), ('a', 8), ('d', 12), ('c', 1)]       
sorted(sirasizliste, key=lambda x:x[1])        

#vektörel operasyonlar
#oop
a=[1,2,3,4]
b=[2,3,4,5]
ab=[]        
for i in range(0, len(a)):
    ab.append(a[i]*b[i])
ab      
 
#fp
import numpy as np       
a=np.array([1,2,3,4])        
b=np.array([2,3,4,5])        
a*b       

#map, filter, reduce
liste=[1,2,3,4,5]
for i in liste:
    print(i+10)

list(map(lambda x: x+10, liste)) #daha partik hali, map verilen bir nesnenin içinde tanımlanacak bir fonksiyonu çalıştırmata izin verir

liste1=[1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x:x%2==0, liste1)) #istenilenleri getiren filtreleme metodu

from functools import reduce
reduce(lambda a,b:a+b,liste1) #liste içindeki tüm ifadeleri topladı

#HATALAR
v=10
z=0
try:
    print(v/z)
except ZeroDivisionError:
    print("Paydada sıfır olmaz")
    
k=10
s="s"
try:
    print(k/s)
except TypeError:
    print("Sayı ve string işleme sokulamaz!..")






















        
        
        



