class divicion:
   def __init__(self):
      self.amigos={}

   def poniendo_plata(self):
      cantidad_de_personas = int(input("¿Entre cuantas personas se va a dividir?: "))
      i = 0
      while i < cantidad_de_personas:
         persona = input("Indique el nombre de un integrante: ")
         monto = float(input("indique cunta plata puso: "))
         integrante = {persona : monto}
         self.amigos.append(integrante)
         i = i+1






