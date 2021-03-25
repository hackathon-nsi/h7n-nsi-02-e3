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
   mot = "".join(lettres_mot)

# s'il reste des éléments dans la liste "lettres_mot":
if lettres_mot != []:

  # si le dernier mot se trouve dans le dictionnaire, on remplace notre mot avec l'emoji correspondant
  if mot in dic:
    mots_phrase.append(dic[mot])

  # si on ne trouve pas d'emoji, on laisse le mot tel qu'il est, et on ajoute a la liste 'mots_phrase'
  else:
    mots_phrase.append(mot)
 
# coller les éléments dans la liste "mots_phrase" et afficher 
print("".join(mots_phrase))
