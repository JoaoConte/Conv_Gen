from Modulos import *

class Consolida():
    def apropriacoes(self):
        self.id_masc = 0
        self.conecta_plan()
        self.cursor_plan.execute('select mascara from mascara_original')
        self.masc_ant =  self.cursor_plan.fetchone()
        self.pm1 = self.masc_ant.find('.')
        self.pm2 = self.masc_ant.find('.', self.pm1+1)
        self.pm3 = self.masc_ant.find('.', self.pm2+1)
        self.pm4 = self.masc_ant.find('.', self.pm3+1)
        self.pm5 = self.masc_ant.find('.', self.pm4+1)
        self.tela_apr()
        if len(self.ent_masc.get()) != 0:
            self.mascara = self.ent_masc.get()
            self.pm1 = self.mascara.find('.')
            self.pm2 = self.mascara.find('.', self.pm1+1)
            self.pm3 = self.mascara.find('.', self.pm2+1)
            self.pm4 = self.mascara.find('.', self.pm3+1)
            self.pm5 = self.mascara.find('.', self.pm4+1)
            self.id_masc = 1

    def grava_masc(self):
        self.conecta_plan()
        conta_lida = self.cursor_plan.execute('select * from plano_espelhado')
        for conta in conta_lida:
            if len(conta[3])==self.pm1:
                gravaconta = conta[3]
            if len(conta[3]== self.pm2-1):
                pass
            if len(conta[3]==self.pm3-2):
                pass
            if len(conta[3]== self.pm4-3):
                pass
            if len(conta[3]== self.pm5-4):
                pass

        pass