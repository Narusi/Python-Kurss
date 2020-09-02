#!/usr/bin/env python
# coding: utf-8

# # Klases Uzdevumi - Lists

# ## 1.a Vidējā vērtība

# Uzrakstīt programmu, kas liek lietotājam ievadīt skaitļus(float).
# Programma pēc katra ievada rāda visu ievadīto skaitļu vidējo vērtību.
# PS. 1a var iztikt bez lists
# 
# 1.b Programma rāda gan skaitļu vidējo vērtību, gan VISUS ievadītos skaitļus
# PS Iziešana no programmas ir ievadot "q"
# 
# 1.c Programma nerāda visus ievadītos skaitļus bet gan tikai TOP3 un BOTTOM3 un protams joprojām vidējo.

# In[2]:


numbs = []
while True:
    numberStr = input("\nIevadiet skaitli: ")

    if "q" not in numberStr.lower():
        if "," in numberStr:
            numberStr = numberStr.replace(',','.').strip()

        numbs.append(float(numberStr))
        print("Vidējā vērtība:",sum(numbs)/len(numbs))
        numbs.sort()
        print("Visi ievadītie skaitļi:",numbs)
        if len(numbs) >= 6:
            print("TOP3 un BOTTOM3:",numbs[:3] + numbs[-3:])
                    
        print("Pēdējais ievadītais skaitlis:",float(numberStr))
    else:        
        break


# ## 2. Kubu tabula

# Lietotājs ievada sākumu (veselu skaitli) un beigu skaitli.
# Izvads ir ievadītie skaitļi un to kubi
# <br>Piemēram: ievads 2 un 5 (divi ievadi)
# <br>Izvads 
# <br>2 kubā: 8
# <br>3 kubā: 27
# <br>4 kubā: 64
# <br>5 kubā: 125
# <br>Visi kubi: [8,27,64,125]
# <br><br>PS teoretiski varētu iztikt bez list, bet ar list būs ērtāk

# In[1]:


pirmaisSk = int(input("Ievadiet sākotnējo skaitli: "))
otraisSk = int(input("Ievadiet noslēdzošo skaitli: "))
kubi = []

for i in range(pirmaisSk, otraisSk+1):
    print("{} kubā: {}".format(i, i**3))
    kubi.append(i**3)
print('Visi kubi:', kubi)


# ## 3. Apgrieztie vārdi

# Lietotājs ievada teikumu. 
# Izvadam visus teikuma vārdus apgrieztā formā. 
# <br>Alus kauss -> Sula ssuak
# <br>PS Te varētu noderēt split un join operācijas.

# In[3]:


teikums = input("Ievadiet teikumu: ")
smukiet = []
jaunsTeik = True

for vards in teikums.split(" "):
    if "." in vards:
        smukiet.append(vards[:-1][::-1].lower()+".")
        jaunsTeik = True        
    elif "!" in vards:
        smukiet.append(vards[:-1][::-1].lower()+"!")
        jaunsTeik = True        
    elif "?" in vards:
        smukiet.append(vards[:-1][::-1].lower()+"?")
        jaunsTeik = True
    else:
        if jaunsTeik:
            smukiet.append(vards[::-1].title())
            jaunsTeik = False
        else:
            smukiet.append(vards[::-1].lower())
print(" ".join(smukiet))


# ## 4. Pirmskaitļi

# šis varētu būt nedēļas nogales uzdevums, klasē diez vai pietiks laika
# Atrodiet un izvadiet pirmos 20 (vēl labāk iespēja izvēlēties cik pirmos pirmskaitļus gribam) pirmskaitļus saraksta veidā t.i. [2,3,5,7,11,...]

# In[5]:


numbCount = int(input("Ieavadiet pirmskaitļu skaitu: "))
nCount = 2
numb = 3
pirmsskaitli = [1, 2]

while nCount <= numbCount:
    irPSkaitlis = True
    
    for i in range(2,numb):
        if numb % i == 0:
            irPSkaitlis = False
    
    if irPSkaitlis:
        nCount += 1
        pirmsskaitli.append(numb)
    
    numb += 1

print(pirmsskaitli)


# In[ ]:




