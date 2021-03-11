import requests
reponse = requests.get('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-02/main/textes/La%20Princesse%20de%20Cl%C3%A8ves/lpdc-partie1.txt')
texte = reponse.text
l = [i for i in texte] # chaque mot de la phrase est place dans une liste 
s = []
y = [] # creation d'une liste vide ou l'on va placer les mots remplacés
dic = {"PRINCESSE":"\U0001F478", "Mademoiselle":"\U0001F467", "mademoiselle":"\U0001F467", "chevalier":"\U0001F40E"} # creation d'un dictionnaire qui associe un mot a un emoji 
u = 0
n = 0
for i in range(len(l)): # pour le nombre de mots dans notre phrase,
  if l[i] == ' ':
    x = ''.join(s) # l'indice x prend le mot composé dans l'indice s dans la phrase d'origine
    s = []
    y.append(" ")
    if x in dic: # si le mot d'indice x se trouve dans le dictionnaire, 
      y[n] = dic[x] # on remplace notre mot avec l'emoji correspondant 
    else:
      y[n] = x # si on ne trouve pas d'emoji, on laisse le mot tel qu'il est
    y.append(" ")
    u = 0
    n = n + 2
  else:
    s.append(' ')
    s[u] = l[i]
    u = u + 1
fin = ''.join(y)

print(fin) # affichage de notre phrase finale 