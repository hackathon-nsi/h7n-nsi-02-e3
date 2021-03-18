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
1ere seance 16/02/2021 : <br />
Discussion sur le programme python: <br />
-utilisation de dictionnaire proposée. <br />
-recherche du code qui permet que le programme reconnaisse la phrase mot par mot. <br />
-base du programme du remplacement réalisée. <br />

<br />

2eme seance 9/03/2021 :<br />
La première version du programme du remplacement posté: <br />

<br />

```python
for i in range(len(origine)): # pour le nombre de mots dans notre phrase,
  
  if origine[i] == " ": # si il y a une espace à l'indice i de la phrase  
    x = "".join(lettres_mot) # coller les éléments dans la liste "lettres_mot" et mettre ce qu'on obtient dans le variable "x"
    lettres_mot = [] # réinitialisation de la liste "lettres_mot"
    mots_phrase.append(" ") # ajouter un élément contenant qu'une espace dans la liste "mots_phrase"    
    if x in dic: # si le mot d'indice x se trouve dans le dictionnaire, 
      mots_phrase[len(mots_phrase)-1] = dic[x] # on remplace notre mot avec l'emoji correspondant 
    else:
      mots_phrase[len(mots_phrase)-1] = x # si on ne trouve pas d'emoji, on laisse le mot tel qu'il est
    mots_phrase.append(" ") # ajouter un élément contenant qu'une espace dans la liste "mots_phrase"
    
  else:
    lettres_mot.append(" ") # ajouter un élément contenant qu'une espace dans la liste "lettres_mot"
    lettres_mot[len(lettres_mot)-1] = origine[i] # dans la liste "lettres_mot", ajouter la lettre qui est à l'indice i de la phrase d'origine
```

<br />

4eme seance 16/03/2021 :<br />
creation d'un programme javascript<br />


