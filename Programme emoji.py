﻿dic = {"princesse":"\U0001F478"}
origine = ["princesse", "am", "genius"]
phrase = []
for i in range(len(origine)):
  phrase.append(0)
  n = origine[i]
  if n in dic:
    phrase[i] = dic[n]
  else:
    phrase[i] = origine[i]
  print(phrase[i],end=' ')