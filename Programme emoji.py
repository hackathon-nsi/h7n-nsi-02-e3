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
  print(phrase[i],end=' ') # affichage de notre phrase finale 
