# **H7N~NSI-02 - EQUIPE 3**

**SUJET** : https://github.com/hackathon-nsi/h7n-nsi-02

**PROGRESSION** (*changer les - par des # | # = 5%*)<br />
niveau 1 : |------# = 50%-------------|<br />
niveau 2 : |--------------------|<br />
niveau 3 : |--------------------|<br />
niveau 4 : |--------------------|<br />

<hr />
<!-- ne pas effacer les lignes ci-dessus et mettre à jour la progression régulièrement -->

<br />
1ère séance 16/02/2021 : <br />
1ère heure: Discussion sur le programme python: <br />
&emsp; -utilisation de dictionnaire proposée. <br />
&emsp; -recherche du code qui permet que le programme reconnaisse la phrase mot par mot. <br />
&emsp; -base du programme du remplacement réalisée. <br />

<br />

2ème heure: La première version du programme qui remplace certains mots par des emojis a été posté: <br />

```python
# création d'un dictionnaire qui associe un mot à un emoji
# chaque mot de la phrase est placé dans une liste
# création d'une liste vide où l'on va placer la phrase après remplacement
dic = {"princesse":"\U0001F478"} 
origine = ["princesse", "is", "genius"] 
phrase = [] 

# pour le nombre de mots dans notre phrase:
# la liste "phrase" apprend un nouvel élément "0"
# l'indice n prend le mot d'indice i dans la phrase d'origine
for i in range(len(origine)):  
  phrase.append(0) 
  n = origine[i] 
  
  # si le mot d'indice n se trouve dans le dictionnaire:
  # on remplace notre mot avec l'emoji correspondant 
  if n in dic:  
    phrase[i] = dic[n] 
    
  # si on ne trouve pas d'emoji: 
  # on laisse le mot tel qu'il est
  else:
    phrase[i] = origine[i] 
    
  # affichage de notre phrase finale 
  print(phrase[i],end=' ') 
```

<br />

2ème séance 9/03/2021 :<br />
La deuxième version du programme qui permet de recomposer la phrase mot par mot a été posté: <br />

```python
# pour le nombre de mots dans notre phrase "origine":
for i in range(len(origine)): 
  
  # si il y a une espace à l'indice i de la phrase:
  # coller les éléments dans la liste "lettres_mot" et mettre ce qu'on obtient dans le variable "x",
  # réinitialiser la liste "lettres_mot",
  # ajouter un élément contenant qu'une espace dans la liste "mots_phrase".
  if origine[i] == " ": 
    x = "".join(lettres_mot) 
    lettres_mot = [] 
    mots_phrase.append(" ")    
    
    # si le mot du variable x se trouve dans le dictionnaire:
    # remplacer notre mot avec l'emoji correspondant.
    if x in dic:  
      mots_phrase[len(mots_phrase)-1] = dic[x] 
      
    # si on ne trouve pas d'emoji correspondant, 
    # laisser le mot tel qu'il est.
    else:
      mots_phrase[len(mots_phrase)-1] = x 
      
    # ajouter un élément contenant qu'une espace dans la liste "mots_phrase"    
    mots_phrase.append(" ") 
    
  # si l'élément à l'indice i de la phrase n'est pas une espace,
  # ajouter un élément contenant qu'une espace dans la liste "lettres_mot",
  # dans la liste "lettres_mot", ajouter la lettre qui est à l'indice i de la phrase d'origine
  else:
    lettres_mot.append(" ") 
    lettres_mot[len(lettres_mot)-1] = origine[i] 
```

<br />

3eme seance 11/03/2021 :<br />
La troisieme version du programme qui est une combinaison des deux versions précédentes postée: <br />
Le probleme d'apparition du derneier mot du texte; il ne s'addapte au retour de la ligne.<br />

```python
# importe la phrase d'origine dans le variable "texte"
import requests
reponse = requests.get("https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-02/main/textes/La%20Princesse%20de%20Cl%C3%A8ves/lpdc-partie1.txt")
texte = reponse.text  



# chaque mot de la phrase est mis en ordre dans la liste "origine"
# création d'une liste vide où l'on va placer chaque lettre d'un mot
# création d'une liste vide où l'on va placer chaque mot de la phrase recomposée
origine = [i for i in texte] 
lettres_mot = [] 
mots_phrase = [] 

dic = {"PRINCESSE":"\U0001F478", "Princesse":"\U0001F478", "princesse":"\U0001F478",  # creation d'un dictionnaire qui associe un mot a un emoji
       "MADEMOISELLE":"\U0001F467", "Mademoiselle":"\U0001F467", "mademoiselle":"\U0001F467", "Mlle":"\U0001F935",
       "CHEVALIER":"\U0001F40E", "Chevalier":"\U0001F40E", "chevalier":"\U0001F40E",
       "MADAME":"\U0001F469", "Madame":"\U0001F469", "madame":"\U0001F469", "Mme":"\U0001F935",
       "MONSIEUR":"\U0001F935", "Monsieur":"\U0001F935", "monsieur":"\U0001F935", "M.":"\U0001F935", "Mr":"\U0001F935",
       "FRANCE":"\U0001F1EB", "France":"\U0001F1EB", "Fr":"\U0001F1EB", 
       "ESPAGNE":"\U0001F1EA", "Espagne":"\U0001F1EA",
       "AMOUREUX":"\U0001F60D", "Amoureux":"\U0001F60D", "amoureux":"\U0001F60D",
       "ROI":"\U0001F934", "Roi":"\U0001F934", "roi":"\U0001F934",
       "FILS":"\U0001F9D1", "Fils":"\U0001F9D1", "fils":"\U0001F9D1"}



# pour le nombre de mots dans notre phrase:
for i in range(len(origine)): 
  
  # si il y a une espace à l'indice i de la phrase:
  if origine[i] == " ":   
  
    # coller les éléments dans la liste "lettres_mot" et mettre ce qu'on obtient dans le variable "x"
    # réinitialisation de la liste "lettres_mot"
    # ajouter un élément contenant qu'une espace dans la liste "mots_phrase"
    x = "".join(lettres_mot) 
    lettres_mot = [] 
    mots_phrase.append(" ")   
    
    # si le mot d'indice x se trouve dans le dictionnaire, on remplace notre mot avec l'emoji correspondant
    if x in dic:  
      mots_phrase[len(mots_phrase)-1] = dic[x]  
      
    # si on ne trouve pas d'emoji, on laisse le mot tel qu'il est  
    else:
      mots_phrase[len(mots_phrase)-1] = x 
    
    # ajouter un élément contenant qu'une espace dans la liste "mots_phrase"
    mots_phrase.append(" ") 
  
  # si il y a d'autre chose qu'une espace à l'indice i de la phrase:
  else:
  
    # ajouter un élément contenant qu'une espace dans la liste "lettres_mot"
    # dans la liste "lettres_mot", ajouter la lettre qui est à l'indice i de la phrase d'origine
    lettres_mot.append(" ") 
    lettres_mot[len(lettres_mot)-1] = origine[i]



# coller les éléments dans la liste "mots_phrase" et mettre ce qu'on obtient dans le variable "fin"       
# affichage de notre phrase finale 
fin = "".join(mots_phrase) 
print(fin) 
```

<br />

4eme seance 16/03/2021 :<br />
Progrés sur l'adaptation du programme python en javascript.<br />

<br />

5eme seance 16/03/2021 :<br />
Progrés sur l'adaptation du programme python en javascript.<br />

<br />

6eme seance 23/03/2021 :<br />
Progrés sur l'adaptation du programme python en javascript.<br />
La version final du programme publié:<br />

```python
# importe la phrase d'origine dans le variable "texte"
import requests
reponse = requests.get("https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-02/main/textes/La%20Princesse%20de%20Cl%C3%A8ves/lpdc-partie1.txt")
texte = reponse.text
 
# création d'une liste vide où l'on va placer chaque lettre d'un mot
# création d'une liste vide où l'on va placer chaque mot de la phrase recomposée
lettres_mot = []
mots_phrase = []

dic = {"PRINCESSE":"\U0001F478", "Princesse":"\U0001F478", "princesse":"\U0001F478",
"MADEMOISELLE":"\U0001F467", "Mademoiselle":"\U0001F467", "mademoiselle":"\U0001F467", "Mlle":"\U0001F935",
"CHEVALIER":"\U0001F40E", "Chevalier":"\U0001F40E", "chevalier":"\U0001F40E",
"MADAME":"\U0001F469", "Madame":"\U0001F469", "madame":"\U0001F469", "Mme":"\U0001F935",
"MONSIEUR":"\U0001F935", "Monsieur":"\U0001F935", "monsieur":"\U0001F935", "M.":"\U0001F935", "Mr":"\U0001F935",
"FRANCE":"\U0001F1EB", "France":"\U0001F1EB", "Fr":"\U0001F1EB",
"ESPAGNE":"\U0001F1EA", "Espagne":"\U0001F1EA",
"AMOUREUX":"\U0001F60D", "Amoureux":"\U0001F60D", "amoureux":"\U0001F60D",
"ROI":"\U0001F934", "Roi":"\U0001F934", "roi":"\U0001F934",
"FILS":"\U0001F9D1", "Fils":"\U0001F9D1", "fils":"\U0001F9D1"}

# pour le nombre de mots dans notre texte:
for i in range(len(texte)):   

 # si il y a une espace ou retour a la ligne à l'indice i du texte:
 if texte[i] == " " or texte[i] == "\n":       
    
   # réinitialisation de la liste "lettres_mot"
   lettres_mot = []    
   
   # si le mot d'indice du variable 'mot' se trouve dans le dictionnaire, on remplace notre mot avec l'emoji correspondant
   if mot in dic:
     mots_phrase.append(dic[mot])
   
   # si on ne trouve pas d'emoji, on laisse le mot tel qu'il est
   else:
     mots_phrase.append(mot)
   
   # si l'indice i du texte est le retour a la ligne, on ajoute le retour a la ligne a 'mots_phrase'
   if texte[i] == "\n":
     mots_phrase.append("\n")
     
   # sinon, on ajoute un élément contenant qu'une espace dans la liste "mots_phrase"
   else:
     mots_phrase.append(" ")
     
   # initialisation de la variable 'mot' 
   mot = ""
 
 # si il y a d'autre chose qu'une espace à l'indice i de la phrase:
 else:
    
   # ajouter un élément contenant qu'une espace dans la liste "lettres_mot"
   # dans la liste "lettres_mot", ajouter la lettre qui est à l'indice i du texte
   lettres_mot.append(texte[i])
   x = "".join(lettres_mot)
   
# si le dernier mot se trouve dans le dictionnaire, on remplace notre mot avec l'emoji correspondant
if mot in dic:
 mots_phrase.append(dic[mot])

# si on ne trouve pas d'emoji, on laisse le mot tel qu'il est, et on ajoute a la liste 'mots_phrase'
else:
 mots_phrase.append(mot)
 
# coller les éléments dans la liste "mots_phrase" et afficher 
print("".join(mots_phrase))
```


