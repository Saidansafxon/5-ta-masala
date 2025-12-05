#1
class Kompyuter:
    def __init__(self,model,xotira):
        self.model=model
        self.xotira=xotira
class Noutbuk(Kompyuter):
    def __init__(self,model,xotira):
        super().__init__(model,xotira)
noutbuk1=Noutbuk("HP",256)
print(noutbuk1.model,noutbuk1.xotira)
class Planshet(Kompyuter):
    def __init__(self,model,xotira):
        super().__init__(model,xotira)
planshet1=Planshet("Samsung",168)
print(planshet1.model,planshet1.xotira)
#2
class xodim:
    def __init__(self,ism,yosh):
        self.ism=ism
        self.yosh=yosh
class Menejer(xodim):
    def __init__(self,ism,yosh):
        super().__init__(ism,yosh)
menejer1=Menejer("Ali",30)
print(menejer1.ism,menejer1.yosh)
class Dasturchi(xodim):
    def __init__(self,ism,yosh):
        super().__init__(ism,yosh)
dasturchi1=Dasturchi("Vali",26)
print(dasturchi1.ism,dasturchi1.yosh)
#3
class Transport:
    def __init__(self,model,yili):
        self.model=model
        self.yili=yili
class Avtobus(Transport):
    def __init__(self,model,yili):
        super().__init__(model,yili)
avtobus1=Avtobus("ISUZU","2019")
print(avtobus1.model,avtobus1.yili)
class Samolyot(Transport):
    def __init__(self,model,yili):
        super().__init__(model,yili)
samolyot1=Samolyot("Boeing",2019)
print(samolyot1.model,samolyot1.yili)
#4
class Animal:
    def __init__(self,ismi,yoshi):
        self.ismi=ismi
        self.yoshi=yoshi
class Cat(Animal):
    def __init__(self,ismi,yoshi):
        super().__init__(ismi,yoshi)
cat1=Cat("simba",4)
print(cat1.ismi,cat1.yoshi)
class Dog(Animal):
    def __init__(self,ismi,yoshi):
        super().__init__(ismi,yoshi)
dog1=Dog("kuchuk",10)
print(dog1.ismi,dog1.yoshi)
#5
class Phone:
    def __init__(self,model,xotira):
        self.model=model
        self.xotira=xotira
class Iphone(Phone):
    def __init__(self,model,xotira):
        super().__init__(model,xotira)
phone1=Phone("17 pro max",256)
print(phone1.model,phone1.xotira)
class Samsung(Iphone):
    def __init__(self,model,xotira):
        super().__init__(model,xotira)
phone2=Phone("S25 ultra",256)
print(phone2.model,phone2.xotira)
