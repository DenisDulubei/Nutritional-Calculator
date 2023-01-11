#metoda pentru interpretarea rezulatelor BMI
from Calculator_nutritional import calculator
def commbmi(bmi):
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

def commbfp(bfp):
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