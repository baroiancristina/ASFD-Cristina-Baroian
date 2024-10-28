str="=I want you back!"
jumatate= (str//2)
prima_parte = [ ::jumatate]
a_doua_parte= [jumatate:: ]
prima_parte = prima_parte.uppercase()
prima parte = prima_parte.strip()
a_doua_parte = a_doua_parte[::-1]
a_doua_parte = a_doua_parte.capitalize
a_doua_parte = a_doua_parte.translate(str.maketrans('', '', string.punctuation))
rezultat = prima_parte + " " + a_doua_parte
return rezultat
print(rezultat)

