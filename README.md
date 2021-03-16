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

2eme seance 11/03/2021 :<br />
La première version du programme du remplacement posté: <br />
dic = {"princesse":"\U0001F478"} # creation d'un dictionnaire qui associe un mot a un emoji 
origine = ["princesse", "am", "genius"] # chaque mot de la phrase est place dans une liste 
phrase = [] # creation d'une liste vide ou l'on va placer les mots remplaces
for i in range(len(origine)): # pour le nombre de mots dans notre phrase, 
  phrase.append(0) 
  n = origine[i] # l'indice n prend le mot d'indice i dans la phrase d'origine
  if n in dic: # si le mot d'indice n se trouve dans le dictionnaire, 
    phrase[i] = dic[n] # on remplace notre mot avec l'emoji correspondant 
  else:
    phrase[i] = origine[i] # si on ne trouve pas d'emoji, on laisse le mot tel qu'il est 
  print(phrase[i],end=' ') # affichage de notre phrase finale  <br />

<br />

3eme seance 16/03/2021 :<br />
creation d'un programme javascript<br />


