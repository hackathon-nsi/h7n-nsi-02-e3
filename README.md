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
origine = ["princesse", "am", "genius"] 
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
La dernière version du programme qui est une combinaison des deux versions précédentes postée: <br />

<br />



<br />

4eme seance 16/03/2021 :<br />
creation d'un programme javascript<br />


