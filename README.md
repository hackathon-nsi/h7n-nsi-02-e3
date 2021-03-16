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

<br />

dic = {"princesse":"\U0001F478"}        &nbsp; &emsp; &emsp; **# creation d'un dictionnaire qui associe un mot a un emoji**<br /> 
origine = ["princesse", "am", "genius"] &emsp; &emsp; &emsp; &emsp; &emsp; **# chaque mot de la phrase est place dans une liste**<br /> 
phrase = []                             &emsp; **# creation d'une liste vide ou l'on va placer les mots remplaces**<br />
for i in range(len(origine)):           &emsp; **# pour le nombre de mots dans notre phrase**<br /> 
  &ensp; phrase.append(0) <br />
  &ensp; n = origine[i]                 &emsp; **# l'indice n prend le mot d'indice i dans la phrase d'origine**<br />
  &ensp; if n in dic:                   &emsp; **# si le mot d'indice n se trouve dans le dictionnaire**<br />
    &emsp; phrase[i] = dic[n]           &emsp; **# on remplace notre mot avec l'emoji correspondant**<br />
  &ensp; else: <br />
    &emsp; phrase[i] = origine[i]       &emsp; **# si on ne trouve pas d'emoji, on laisse le mot tel qu'il est**<br /> 
  &ensp; print(phrase[i],end=' ')       &emsp; **# affichage de notre phrase finale**<br />

<br />

3eme seance 16/03/2021 :<br />
creation d'un programme javascript<br />


