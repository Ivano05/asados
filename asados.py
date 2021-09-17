cantidad_de_personas = int(input("¿Entre cuantas personas se va a dividir?: "))
amigos = []
i = 0
while i < cantidad_de_personas:
   persona = input("Indique el nombre de un integrante: ")
   monto = float(input("indique cunta plata puso: "))
   integrante = {persona : monto}
   amigos.append(integrante)
   i = i+1
#total = (sum(amigos.values()))
print(total)


