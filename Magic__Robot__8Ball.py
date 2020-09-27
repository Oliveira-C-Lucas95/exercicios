import random
import PySimpleGUI as sg

class MagicRobot8Ball:
    def __init__(self):
        self.respostas = [
            "Fuckin' A"
            "vai lá lekjack!"
            "claro que não né"
            "talvez lek"
            "shit, sla, tenta mais tarde"
            "Não." 
        ]
    def iniciar(self):
        #layout
        layout=[
            [sg.text('Faça sua pergunta:')],
            [sg.input()],
            [sg.output(size=(50,10))],
            [sg.button("colfoi da parada?")]
        ]    
        #criar janela
        self.janela=sg.window("MagicRobot8Ball", layout=layout)
        while true:
            #ler valores
            self.eventos, self.valores = self.janela.read()
            if self.eventos == "colfoi da parada?":
                print(random.choice(self.respostas))
decida=MagicRobot8Ball()
decida.iniciar()