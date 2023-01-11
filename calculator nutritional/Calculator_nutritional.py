#BMI calculator

run=True
while True:
    try:
        tip_program=input('''Alegeti tipul de program pe care doriti sa il rulati:
        1. Calculator BMI
        2. Calculator procentaj grasime
        3. Calculator greutate ideala
        4. Calculator necesar caloric:''' )
        if tip_program=="1":
            metric=input("algeti sistemul metric utilizat: kg/m=1, lbs/in=2 ")
            mass=input("introdugeti greutatea dumneavoastra in kg/lbs: ")
            height=input("introduceti inaltimea dumneavoastra in cm/in: ")
            def Bmi():
                if metric=="1":
                    height2=float(height)*0.3937
                    mass2=float(mass)*2.2046
                elif metric=="2":
                    height2=height
                    mass2=mass
                else:
                    print("eroare inaltime")
                bmi=int(mass2)/(float(height2)**2)*703
                
                return bmi
            BMI=Bmi()
            print("indicele dumneavoastra de masa este: ", BMI)
            if float(BMI)<=18.5:
                print("Indicele dumneavoastra de masa corporala corespunde unei persoane cu o greutate sub limita")
            elif float(BMI)>18.5 and float(BMI)<=24.9:
                print("Indicele dumneavoastra de masa corporala corespunde unei persoane cu o greutate  normala")
            elif float(BMI)>24.9 and float(BMI)<=29.9:
                print("Indicele dumneavoastra de masa corporala corespunde unei persoane cu o greutate  usor crescuta")
            elif float(BMI)>29.9 and float(BMI)<=34.9:
                print("Indicele dumneavoastra de masa corporala corespunde unei persoane cu obezitate de gradul I")
            elif float(BMI)>34.9 and float(BMI)<=39.9:
                print("Indicele dumneavoastra de masa corporala corespunde unei persoane cu obezitate de gradul II")
            elif float(BMI)>39.9:
                print("Indicele dumneavoastra de masa corporala corespunde unei persoane cu obezitate de gradul III")
            else:
                Print("datele introduse nu sunt valide")
    #calculator body fat
        if tip_program=="2":
            metric=input("algeti sistemul metric utilizat: kg/m=1, lbs/in=2 ")
            Gen=input("Introdugeti genul dumneavoastra, Masculin=1, Feminin=0: ")
            Varsta=input("Introduceti varsta dumenavoastra: ")
            mass=input("introdugeti greutatea dumneavoastra in kg/lbs: ")
            height=input("introduceti inaltimea dumneavoastra in cm/in: ")
            if metric=="1":
                mass=int(mass)*2.2
                height=int(height)*0.393701
            elif metric=="2":
                mass=mass
                height=height
            else:
                print("Nu ati introdus o obtiune valida")
            def bodyfat():
                    bmi=int(mass)/int(height)**2*703
                    BFP=1.2*int(bmi)+0.23*int(Varsta)-10.8*int(Gen)-0.54
                    return BFP
            BFP=bodyfat()
            print("Procentajul dumneavoastra de grasime corporala este:", bodyfat(),"%")
            if Gen=="1" and int(Varsta)<=39 and float(BFP)<=8:
                print("Nivelul dumneavoastra de grasime corporala este prea scazut")
            elif Gen=="1" and int(Varsta)<=39 and float(BFP)>=8 and float(BFP)<20:
                print("Nivelul dumneavoastra de grasime corporala este unul normal")
            elif Gen=="1" and int(Varsta)<=39 and float(BFP)>=20 and float(BFP)<25:
                print("Nivelul dumneavoastra de grasime corporala este usor crescut")
            elif Gen=="1" and int(Varsta)<=39 and float(BFP)>=25:
                print("Nivelul dumneavoastra de grasime corporala este foarte crescut")
           
            
            elif Gen=="1" and int(Varsta)>39 and int(Varsta)<=59 and float(BFP)<=10:
                print("Nivelul dumneavoastra de grasime corporala este prea scazut")
            elif Gen=="1" and int(Varsta)>39 and int(Varsta)<=59 and float(BFP)>10 and float(BFP)<=22:
                print("Nivelul dumneavoastra de grasime corporala este unul normal")
            elif Gen=="1" and int(Varsta)>39 and int(Varsta)<=59 and float(BFP)>22 and float(BFP)<=29:
                print("Nivelul dumneavoastra de grasime corporala este usor crescut")
            elif Gen=="1" and int(Varsta)>39 and int(Varsta)<=59 and float(BFP)>29:
                print("Nivelul dumneavoastra de grasime corporala este foarte crescut")
            
                
            elif Gen=="1" and int(Varsta)>59  and float(BFP)<=12:
                print("Nivelul dumneavoastra de grasime corporala este prea scazut")
            elif Gen=="1" and int(Varsta)>59  and float(BFP)>12 and float(BFP)<=25:
                print("Nivelul dumneavoastra de grasime corporala este unul normal")
            elif Gen=="1" and int(Varsta)>59 and float(BFP)>25 and float(BFP)<=30:
                print("Nivelul dumneavoastra de grasime corporala este usor crescut")
            elif Gen=="1" and int(Varsta)>59 and float(BFP)>30:
                print("Nivelul dumneavoastra de grasime corporala este foarte crescut")
            
            
            elif Gen=="0" and int(Varsta)<=39 and float(BFP)<=21:
                print("Nivelul dumneavoastra de grasime corporala este prea scazut")
            elif Gen=="0" and int(Varsta)<=39 and float(BFP)>21 and float(BFP)<=33:
                print("Nivelul dumneavoastra de grasime corporala este unul normal")
            elif Gen=="0" and int(Varsta)<=39 and float(BFP)>33 and float(BFP)<=39:
                print("Nivelul dumneavoastra de grasime corporala este usor crescut")
            elif Gen=="0" and int(Varsta)<=39 and float(BFP)>39:
                print("Nivelul dumneavoastra de grasime corporala este foarte crescut")
            
            
            elif Gen=="0" and int(Varsta)>39 and int(Varsta)<=59 and float(BFP)<=23:
                print("Nivelul dumneavoastra de grasime corporala este prea scazut")
            elif Gen=="0" and int(Varsta)>39 and int(Varsta)<=59 and float(BFP)>23 and float(BFP)<=34:
                print("Nivelul dumneavoastra de grasime corporala este unul normal")
            elif Gen=="0" and int(Varsta)>39 and int(Varsta)<=59 and float(BFP)>34 and float(BFP)<=40:
                print("Nivelul dumneavoastra de grasime corporala este usor crescut")
            elif Gen=="0" and int(Varsta)>39 and int(Varsta)<=59 and float(BFP)>40:
                print("Nivelul dumneavoastra de grasime corporala este foarte crescut")
            
            
            elif Gen=="0" and int(Varsta)>59  and float(BFP)<=24:
                print("Nivelul dumneavoastra de grasime corporala este prea scazut")
            elif Gen=="0" and int(Varsta)>59  and float(BFP)>24 and float(BFP)<=36:
                print("Nivelul dumneavoastra de grasime corporala este unul normal")
            elif Gen=="0" and int(Varsta)>59 and float(BFP)>36 and float(BFP)<=42:
                print("Nivelul dumneavoastra de grasime corporala este usor crescut")
            elif Gen=="0" and int(Varsta)>59 and float(BFP)>42:
                print("Nivelul dumneavoastra de grasime corporala este foarte crescut")
            else:
                print("Datele introduse de dumneavoastra nu sunt corecte")
    #Calculator Greutate ideala
        if tip_program=="3":
            Gen=input("Introdugeti genul dumneavoastra, Masculin=1, Feminin=0: ")
            height=input("introduceti inaltimea dumneavoastra in cm/in: ")
            ideal=0
            if Gen=="1":
                ideal=50
            elif Gen=="0":
                ideal=45.5
            def GI():
                greutate=float(ideal)+(0.91*(int(height)-152.4))
                return greutate
            greutate=GI()
            print("Greutatea dumneavoastra ideala este: ",greutate,"Kg")
            
            
    #Calculator necesar caloric
        if tip_program=="4":
            metric=input("Introduceti tipul de sistem metric utilizat Kg/m=1 sau lbs/in=2: ")
            Gen=input("Introdugeti genul dumneavoastra, Masculin=1, Feminin=0: ")
            Varsta=input("Introduceti varsta dumenavoastra: ")
            mass=input("introdugeti greutatea dumneavoastra in kg: ")
            height=input("introduceti inaltimea dumneavoastra in cm/in: ")
            print(''' 
                1. sedentar (job de birou, activitate fizica minimala spre deloc)
        2. usor activ (job de presupune mers/ stat in picioare, activitate minimala in restul zilei )
        3. moderar (job ce presupune activitate fizica, ex: bucatar, ospatar/ antrenament fizic/alergat, mers pe bicicleta 2h/zi)
        4. activ(job ce presupune activitate fizica cel putin 4 h pe zi, ex: consctructii, dansuri, atletism)
        5. foarte activ (activitate fizica moderata spre grea, timp de 8 h pe zi ): ''')
            tip_activitate=input('Selectati tipul dumneavoastra de activitate:')
                
            if metric=="1":
                mass=int(mass)*2.2
                height=int(height)*0.393701
                mass2=int(mass)/2.2
            elif metric=="2":
                mass=mass
                height=height
                mass2=int(mass)/2.2
            else:
                print("Nu ati introdus o obtiune valida")
            def bodyfat():
                    bmi=float(mass)/float(height)**2*703
                    BFP=1.2*float(bmi)+0.23*int(Varsta)-10.8*int(Gen)-0.54
                    return BFP
            BFP=bodyfat()
            CT=0
            if Gen=="1":
                CT=1.0
            elif Gen=="0":
                CT=0.9
            else:
                print("Datele introduse nu sunt corecte")
            LF=0
            if Gen=="1" and float(BFP)>=10 and float(BFP)<14:
                LF=1.0
            elif Gen=="1" and float(BFP)>=14 and float(BFP)<20:
                LF=0.95
            elif Gen=="1" and float(BFP)>=20 and float(BFP)<28:
                LF=0.9
            elif Gen=="1" and float(BFP)>=28:
                LF=0.85
            elif Gen=="0" and float(BFP)>=14 and float(BFP)<18:
                LF=1.0
            elif Gen=="0" and float(BFP)>=18 and float(BFP)<28:
                LF=0.95
            elif Gen=="0" and float(BFP)>=29 and float(BFP)<38:
                LF=0.9
            elif Gen=="0" and float(BFP)>=38:
                LF=0.85
            def BMR():
                bmr=float(mass2)*float(CT)*24*float(LF)
                return bmr
            bmr=BMR()
            print ("Rata dumneavoastra metabolica bazala este:", bmr,"kcal")
            need=0
            if tip_activitate=="1":
                need=1.2
            elif tip_activitate=="2":
                need=1.375
            elif tip_activitate=="3":
                need=1.55
            elif tip_activitate=="4":
                need=1.725
            elif tip_activitate=="5":
                need=1.9
            else:
                print("datele introduse nu sunt valide")
            
            
            def necesar_mentinere():
                necesar=bmr*float(need)
                return necesar
            necesar=necesar_mentinere()
            print("Necesarul dumneavoastra caloric pentru mentinere ese:", necesar,'kcal')
                
    except:
        pass
        
            
        
    
            
    din_nou=input("Doriti sa efectuati un alt calcul? da/nu:")
                
    if input=="da":
        run=True
    else:
        run=False