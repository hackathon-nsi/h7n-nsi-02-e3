import requests
reponse = requests.get("https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-02/main/textes/La%20Princesse%20de%20Cl%C3%A8ves/lpdc-partie1.txt")
texte = reponse.text  # importe la phrase d'origine dans le variable "texte"



origine = [i for i in texte] # chaque mot de la phrase est mis en ordre dans la liste "origine"
lettres_mot = [] # création d'une liste vide où l'on va placer chaque lettre d'un mot
mots_phrase = [] # création d'une liste vide où l'on va placer chaque mot de la phrase recomposée

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

    
fin = "".join(mots_phrase) # coller les éléments dans la liste "mots_phrase" et mettre ce qu'on obtient dans le variable "fin"



print(fin) # affichage de notre phrase finale 


