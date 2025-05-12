from Modulos import *
from Funcoes import *
from ScreenFrames import *
from Con_DB import *

conver = Tk()

class Application(Func, Frames, Conexao):

    def __init__(self):
        self.conver = conver
        self.versao = 'v1.0'
        self.le_conexao()
        self.tela_ini()
        self.conver.mainloop() 
Application()

 