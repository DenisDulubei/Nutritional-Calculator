# Health calculator app
class calculator:
    def __init__(self,name,choice,age,gender,mass,height,activ):
        self.name=name
        self.choice=choice
        self.mass=mass
        self.age=age
        self.gender=gender
        self.height=height
        self.activ=activ
    #metoda pentru calculul BMI
    def bodymass(self):

        return(self.mass/((self.height/100)**2))
    def commbmi(self,bmi):
      print(f"Indicele dumneavoastra de masa corporala ese de:{bmi}")
      if float(bmi)<=18.5:
        print("Indicele dumneavoastra de masa corporala corespunde unei persoane cu o greutate sub limita")
      elif float(bmi)>18.5 and float(bmi)<=24.9:
        print("Indicele dumneavoastra de masa corporala corespunde unei persoane cu o greutate  normala")
      elif float(bmi)>24.9 and float(bmi)<=29.9:
        print("Indicele dumneavoastra de masa corporala corespunde unei persoane cu o greutate  usor crescuta")
      elif float(bmi)>29.9 and float(bmi)<=34.9:
        print("Indicele dumneavoastra de masa corporala corespunde unei persoane cu obezitate de gradul I")
      elif float(bmi)>34.9 and float(bmi)<=39.9:
        print("Indicele dumneavoastra de masa corporala corespunde unei persoane cu obezitate de gradul II")
      elif float(bmi)>39.9:
        print("Indicele dumneavoastra de masa corporala corespunde unei persoane cu obezitate de gradul III")
      else:
        print("datele introduse nu sunt valide")
    
    #Metoda pentru a calcula procentul de grasime corporala 
    def bodyfat(self,bmi):
      if self.gender=="male":
        genderct=1
      elif self.gender=="female":
        genderct=0
      else:
        print("datele introduse nu sunt corecte")
      return 1.2*float(bmi)+0.23*int(self.age)-10.8*int(genderct)-0.54
    
    def commbfp(self, bfp):
      print(f"Procentajul dumneavoastra de grasime corporala este de {bfp}")
      if self.gender=="male" and int(self.age)<=39 and float(bfp)<=8:
          print("Nivelul dumneavoastra de grasime corporala este prea scazut")
      elif self.gender=="male" and int(self.age)<=39 and float(bfp)>=8 and float(bfp)<20:
          print("Nivelul dumneavoastra de grasime corporala este unul normal")
      elif self.gender=="male" and int(self.age)<=39 and float(bfp)>=20 and float(bfp)<25:
          print("Nivelul dumneavoastra de grasime corporala este usor crescut")
      elif self.gender=="male" and int(self.age)<=39 and float(bfp)>=25:
          print("Nivelul dumneavoastra de grasime corporala este foarte crescut")
      
      
      elif self.gender=="male" and int(self.age)>39 and int(self.age)<=59 and float(bfp)<=10:
          print("Nivelul dumneavoastra de grasime corporala este prea scazut")
      elif self.gender=="male" and int(self.age)>39 and int(self.age)<=59 and float(bfp)>10 and float(bfp)<=22:
          print("Nivelul dumneavoastra de grasime corporala este unul normal")
      elif self.gender=="male" and int(self.age)>39 and int(self.age)<=59 and float(bfp)>22 and float(bfp)<=29:
          print("Nivelul dumneavoastra de grasime corporala este usor crescut")
      elif self.gender=="male" and int(self.age)>39 and int(self.age)<=59 and float(bfp)>29:
          print("Nivelul dumneavoastra de grasime corporala este foarte crescut")
      
          
      elif self.gender=="male" and int(self.age)>59  and float(bfp)<=12:
          print("Nivelul dumneavoastra de grasime corporala este prea scazut")
      elif self.gender=="male" and int(self.age)>59  and float(bfp)>12 and float(bfp)<=25:
          print("Nivelul dumneavoastra de grasime corporala este unul normal")
      elif self.gender=="male" and int(self.age)>59 and float(bfp)>25 and float(bfp)<=30:
          print("Nivelul dumneavoastra de grasime corporala este usor crescut")
      elif self.gender=="male" and int(self.age)>59 and float(bfp)>30:
          print("Nivelul dumneavoastra de grasime corporala este foarte crescut")
      
      
      elif self.gender=="female" and int(self.age)<=39 and float(bfp)<=21:
          print("Nivelul dumneavoastra de grasime corporala este prea scazut")
      elif self.gender=="female" and int(self.age)<=39 and float(bfp)>21 and float(bfp)<=33:
          print("Nivelul dumneavoastra de grasime corporala este unul normal")
      elif self.gender=="female" and int(self.age)<=39 and float(bfp)>33 and float(bfp)<=39:
          print("Nivelul dumneavoastra de grasime corporala este usor crescut")
      elif self.gender=="female" and int(self.age)<=39 and float(bfp)>39:
          print("Nivelul dumneavoastra de grasime corporala este foarte crescut")
      
      
      elif self.gender=="female" and int(self.age)>39 and int(self.age)<=59 and float(bfp)<=23:
          print("Nivelul dumneavoastra de grasime corporala este prea scazut")
      elif self.gender=="female" and int(self.age)>39 and int(self.age)<=59 and float(bfp)>23 and float(bfp)<=34:
          print("Nivelul dumneavoastra de grasime corporala este unul normal")
      elif self.gender=="female" and int(self.age)>39 and int(self.age)<=59 and float(bfp)>34 and float(bfp)<=40:
          print("Nivelul dumneavoastra de grasime corporala este usor crescut")
      elif self.gender=="female" and int(self.age)>39 and int(self.age)<=59 and float(bfp)>40:
          print("Nivelul dumneavoastra de grasime corporala este foarte crescut")
      
      
      elif self.gender=="female" and int(self.age)>59  and float(bfp)<=24:
          print("Nivelul dumneavoastra de grasime corporala este prea scazut")
      elif self.gender=="female" and int(self.age)>59  and float(bfp)>24 and float(bfp)<=36:
          print("Nivelul dumneavoastra de grasime corporala este unul normal")
      elif self.gender=="female" and int(self.age)>59 and float(bfp)>36 and float(bfp)<=42:
          print("Nivelul dumneavoastra de grasime corporala este usor crescut")
      elif self.gender=="female" and int(self.age)>59 and float(bfp)>42:
          print("Nivelul dumneavoastra de grasime corporala este foarte crescut")
      else:
          print("Datele introduse de dumneavoastra nu sunt corecte")
#metoda calculator Greutate ideala
    def gideal(self):
        if self.gender=="male":
            idct=50
        elif self.gender=="female":
            idct=45.5
        else:
            print("datele introduse nu sunt valide")
        ideal=float(idct)+(0.91*(int(self.height)-152.4))
        print(f"Greutatea dumneavoastra ideala este: {ideal}")
#metoda calculare necesar caloric bazal
    def BMR(self,bfp):
        kg=int(self.mass*2.2)
        height=int(self.height)*0.393701
        if self.gender=="male":
            CT=1.0
        elif self.gender=="female":
            CT=0.9
        if self.gender=="male" and float(bfp)>=10 and float(bfp)<14:
            LF=1.0
        elif self.gender=="male" and float(bfp)>=14 and float(bfp)<20:
            LF=0.95
        elif self.gender=="male" and float(bfp)>=20 and float(bfp)<28:
            LF=0.9
        elif self.gender=="male" and float(bfp)>=28:
            LF=0.85
        elif self.gender=="female" and float(bfp)>=14 and float(bfp)<18:
            LF=1.0
        elif self.gender=="female" and float(bfp)>=18 and float(bfp)<28:
            LF=0.95
        elif self.gender=="female" and float(bfp)>=29 and float(bfp)<38:
            LF=0.9
        elif self.gender=="female" and float(bfp)>=38:
            LF=0.85
        
        return float(self.mass)*float(CT)*24*float(LF)
    def combmr(self,bmr):
        print(f"Rata dumneavoastra metabolica bazala este de: {bmr} kcal")    
#metoda calcul necesar caloric zilnic
    def necesar(self,bmr):
        
        if  self.activ=="1":
            need=1.2
        elif self.activ=="2":
            need=1.375
        elif self.activ=="3":
            need=1.55
        elif self.activ=="4":
            need=1.725
        elif self.activ=="5":
            need=1.9
        else:
            print("datele introduse nu sunt valide")
        
        return float(bmr)*float(need)
    def comnec(self,nec):
        print(f"necesarul dumneavoastra pentru mentinere este de: {nec} kcal")
run=True
while run==True:
    pacient=calculator(input("introduceti numele dumenavoastra: "),input('''Alegeti tipul de program pe care doriti sa il rulati:
            1. Calculator BMI
            2. Calculator procentaj grasime
            3. Calculator greutate ideala
            4. Calculator necesar caloric: '''),
            int(input("introduceti varsa dumneavoastra: ")), 
            input("introduceti genul dumneavoiastra: male/female: "),
            int(input("Introduceti greutatea dumneavoastra in kg: ")),
            float(input("Introduceti inaltimea dumneavoastra in cm: ")),
            input('''Selectati tipul dumneavoastra de activitate:  
            1. sedentar (job de birou, activitate fizica minimala spre deloc)
            2. usor activ (job de presupune mers/ stat in picioare, activitate minimala in restul zilei )
            3. moderar (job ce presupune activitate fizica, ex: bucatar, ospatar/ antrenament fizic/alergat, mers pe bicicleta 2h/zi)
            4. activ(job ce presupune activitate fizica cel putin 4 h pe zi, ex: consctructii, dansuri, atletism)
            5. foarte activ (activitate fizica moderata spre grea, timp de 8 h pe zi ): '''))

    bmi=pacient.bodymass()
    bfp=pacient.bodyfat(bmi)
    bmr=pacient.BMR(bfp)
    nec=pacient.necesar(bmr)
    if pacient.choice=="1":
        pacient.commbmi(bmi)
    elif pacient.choice=="2":
        pacient.commbfp(bfp)
    elif pacient.choice=="3":
        pacient.gideal()
    elif pacient.choice=="4":
        pacient.combmr(bmr)
        pacient.comnec(nec)
    answer=input("doriti sa efectuati alt calcul? da/nu: ")
    if answer=="da":
        run=True
    else:
        run=False






