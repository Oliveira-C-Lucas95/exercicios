



import random

class MagicRobot8Ball:
    def __init__(self):
        self.respostas = [
            "Fuckin' A",
            "vai lá lekjack!",
            "claro que não né",
            "talvez lek",
            "shit, sla, tenta mais tarde",
            "Não." 
        ]
    def iniciar(self):
        pergunta="faz a pergunta__"
        input(pergunta)
                 
        while True:
            if input != None:
                print(random.choice(self.respostas))
                input(pergunta)
        
decida=MagicRobot8Ball()
decida.iniciar()
