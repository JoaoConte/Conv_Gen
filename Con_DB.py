from Modulos import *

class Conexao():

    def le_conexao(self):  # Lê ..\conexao.dat e conexao_par.dat(caso seja Oracle 32 bits)
        self.caminho = os.path.abspath(os.path.dirname('.')) # Pega diretorio atual

    def conecta(self):
        self.caminho = os.path.abspath(os.path.dirname('.')) # Pega diretorio atual
        self.banco = sqlite3.connect(self.caminho+"\Lay_Gen.db")
        self.cursor = self.banco.cursor()

    def desconecta(self):
        self.banco.close()