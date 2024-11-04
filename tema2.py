string="I want you back!."
jumatate = len(string)//2
prima_parte = string[ :jumatate]
a_doua_parte = string[jumatate: ]
prima_parte = prima_parte.upper()
prima_parte = prima_parte.strip()
a_doua_parte = a_doua_parte[::-1]
a_doua_parte = a_doua_parte.capitalize()
a_doua_parte = a_doua_parte.translate(str.maketrans('', '', string.punctuation))
rezultat = prima_parte + " " + a_doua_parte
print(rezultat)

