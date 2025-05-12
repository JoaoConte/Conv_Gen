from Modulos import *

class Frames():

    def relacionamento(self):
        self.tela_relac = Toplevel()
        self.tela_relac.geometry("900x600+220+80")
        self.tela_relac.resizable(False,False)
        self.tela_relac.focus_force()
        self.tela_relac.grab_set()
        self.tela_relac.title('De-Para Contabilização')
        self.conecta_plan()     
        self.lista_contas()      

    def relaciona_cc(self):
        self.tela_relacc = Toplevel()
        self.tela_relacc.geometry("900x600+220+80")
        self.tela_relacc.resizable(False,False)
        self.tela_relacc.focus_force()
        self.tela_relacc.grab_set()
        self.tela_relacc.title('De-Para Centro de Custos')
        self.conecta_plan()     
        self.lista_contas()      

    def tela_apr(self):
        self.tela_aproc = Toplevel()
        self.tela_aproc.geometry("400x200+320+200")
        self.tela_aproc.resizable(False,False)
        self.tela_aproc.focus_force()
        self.tela_aproc.grab_set()
        self.busca_mascara()
        self.tela_aproc.title('Nova Mascara')
        self.lbl_apr = Label(self.tela_aproc, text = 'Mascara atual: '+ self.masc_ant)#self.masc_ant[0])
        self.lbl_apr.place(relx = 0.10 , rely = 0.12) 
        self.lbl_apr = Label(self.tela_aproc, text = 'Nova Mascara (preenchar com # e pontos)')
        self.lbl_apr.place(relx = 0.10 , rely = 0.25)
        self.ent_masc = Entry(self.tela_aproc, width=20)
        self.ent_masc.place(relx = 0.10 , rely = 0.50)
        self.btn_conf_apr = Button(self.tela_aproc, text = 'Confirma', fg = 'green', bg = '#D3D3D3', width=10, font = 'arial 10 bold', command = self.pre_exportacao)
        self.btn_conf_apr.place(relx = 0.20 , rely = 0.80)
        self.btn_canc_apr = Button(self.tela_aproc, text = 'Cancela', fg = 'red', bg = '#D3D3D3', width=10, font = 'arial 10 bold', command = self.fim_tela_aproc)       
        self.btn_canc_apr.place(relx = 0.50 , rely = 0.80) 
        self.ent_masc.focus()

    def tela_ini(self):
        self.conver.geometry("900x500+220+100")
        self.conver.title('Conversor Genérico '+self.versao)
        self.conver.resizable(False,False)

        self.lbl_tit = Label(self.conver, text = 'Conversor Genérico', font = 'Arial 25 bold')
        self.lbl_tit.place(relx = 0.33, rely = 0.05)
  
        self.btn_ler = Button(self.conver, text = 'Layout arquivo Entrada', bg = '#D3D3D3', font = 'Arial 15 bold', width= 40, height=2, command = self.abre_origem)
        self.btn_ler.place(relx = 0.23, rely = 0.20) 
# Depois do arquivo lido
        self.btn_conv = Button(self.conver, text = 'Layout arquivo Saida', bg = '#D3D3D3', font = 'Arial 15 bold', width= 40, height=2, command = self.relacionamento)
        self.btn_conv.place(relx = 0.23, rely = 0.35)


        self.btn_apr = Button(self.conver, text = 'Importa arquivo Entrada', bg = '#D3D3D3', font = 'Arial 15 bold', width=40, height=2, command = self.tela_apr)
        self.btn_apr.place(relx = 0.23, rely = 0.50)

        self.btn_exp1 = Button(self.conver, text = 'Gerar Arquivo Convertido', bg = '#D3D3D3', font = 'Arial 15 bold', width= 40, height=2, command = self.exporta_padrao)
        self.btn_exp1.place(relx = 0.23, rely = 0.65)   

        # self.btn_exp2 = Button(self.conver, text = 'Gerar Arquivo Convertido', bg = '#D3D3D3', font = 'Arial 15 bold', width= 40, height=2, command = self.exporta_padrao)
        # self.btn_exp2.place(relx = 0.23, rely = 0.80)  


