from lista_tari import countryes
from lista_tari import capitals
from lista_tari import cars
import random
import string
play=True
# fai user sa aleaga categoria de joc
while play:
    def sa_jucam ():
        
        tip=input('''Selectati tipul de joc:
        1. Tari
        2. Capitale
        3. Masini ''')
        if tip == "1":
            word=random.choice(countryes)

        elif tip =="2":
            word=random.choice(capitals)

        elif tip== "3":
            word=random.choice(cars)

            
        word_letters=set(word)
        alphabet=set(string.ascii_uppercase)
        used_letters= set()

        lives=7


        while len(word_letters)>0 and lives>0:
            print("In acest moment ai ", lives," vieti ramase, si ai folosit urmatoarele litere", " ".join(used_letters))

            word_list=[letter if letter in used_letters else "_" for letter in word]
            print ("Cuvantul este :", " ".join(word_list))
            user_letter=input("Ghiceste o litera ")
            if user_letter in alphabet-used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print('')
                else:
                    lives=lives-1
                    print("litera aleasa de tine,", user_letter, "nu este in cuvant.")
                
                    if lives==6:
                        print('''    
    ____
    |   |
    |   
    |   
    |  
    |
    =====''')
                    if lives==5:
                        print('''    
    ____
    |   |
    |   O
    |   
    |  
    |
    =====''')
                    if lives==4:
                        print('''    
    ____
    |   |
    |   O
    |   |
    |  
    |
    =====''')
                    if lives==3:
                        print('''    
    ____
    |   |
    |   O
    |  /|
    |  
    |
    =====''')
                    if lives==2:
                        print('''    
    ____
    |   |
    |   O
    |  /|/
    |  
    |
    =====''')
                    if lives==1:
                        print('''    
    ____
    |   |
    |   O
    |  /|/
    |  /
    |
    =====''')
            elif user_letter in used_letters:
                    print("Ai ales deja aceasta litera")

            else:
                print("caracter invalid")

        if lives==0:
            print('''    
    ____
    |   |
    |   O
    |  /|/
    |  //
    |
    =====''',"Off, ai pierdut, cuvantul era: ", word)
        else: print("Ai castigat, cuvantul ghicit a fost", word)

    sa_jucam()
    again=input("vrei sa mai jucam odata? DA sau NU: ")
    if again=="DA":
        play=True
    elif again=="NU":
        play=False