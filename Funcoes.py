from Modulos import *

class Func(): 

   def exporta_padrao(self):
      # Plano de contas
      nulo = 'NULL'
      self.padrao_conta = "INSERT INTO CTB_CONTA (EMPRESA,REVENDA,CONTA,CONTA_SUPERIORA,CONTA_EDITADA,COSIF,DES_CONTA,NATUREZA,NIVEL,REDUZIDO,RELATORIOS,LANCAMENTO_DIVIDIDO,ACEITA_SUMARIZACAO,CODIGO,OPERACAO,CONTA_REFERENCIAL,COD_AGLUTINADORA,NATUREZA_GRUPO,NIVEL_DIVISAO,CONTA_HARLEY,CONTA_REFERENCIAL_FCONT,INATIVO_CONSULTAS,DTA_INCLUSAO,CONTA_TRANSFERENCIA,ANOMES_TRANSFERENCIA,COD_CENTRO_CUSTO_ECF) VALUES"
      self.conecta_plan()
      with open('CTB_CONTA.SQL', 'w') as ctbconta:
         self.plano_pre = self.cursor_plan.execute("SELECT * FROM plano_espelhado ORDER BY conta_nova")
         for pl_ex in self.plano_pre:
            self.grava_conta_nova = self.padrao_conta +"("+pl_ex[0]+","+pl_ex[1]+",'"+pl_ex[3]+"','"+pl_ex[5]+"','"+pl_ex[7]+"','"+pl_ex[8]
            self.grava_conta_nova = self.grava_conta_nova +"','"+pl_ex[10]+"','"+pl_ex[11]+"','"+pl_ex[12]+"',"+pl_ex[13]+",'"+pl_ex[14]
            self.grava_conta_nova = self.grava_conta_nova +"','"+pl_ex[15]+"','"+pl_ex[16]+"',"
            if pl_ex[17] == 'None':
               self.grava_conta_nova = self.grava_conta_nova + nulo +","
            else:
               self.grava_conta_nova = self.grava_conta_nova + "'"+pl_ex[17]+"',"
            if pl_ex[18] == 'None':
               self.grava_conta_nova = self.grava_conta_nova + nulo +","
            else:
               self.grava_conta_nova = self.grava_conta_nova + "'"+pl_ex[18]+"',"
            if pl_ex[19] == 'None':
               self.grava_conta_nova = self.grava_conta_nova + nulo +","
            else:
               self.grava_conta_nova = self.grava_conta_nova + "'"+pl_ex[19]+"',"
            if pl_ex[20] == 'None':
               self.grava_conta_nova = self.grava_conta_nova + nulo +","
            else:
               self.grava_conta_nova = self.grava_conta_nova + "'"+pl_ex[20]+"',"
            if pl_ex[21] == 'None':
               self.grava_conta_nova = self.grava_conta_nova + nulo +","
            else:
               self.grava_conta_nova = self.grava_conta_nova + "'"+pl_ex[21]+"',"
            if pl_ex[22] == 'None':
               self.grava_conta_nova = self.grava_conta_nova + nulo +","
            else:
               self.grava_conta_nova = self.grava_conta_nova + pl_ex[22]+","
            if pl_ex[23] == 'None':
               self.grava_conta_nova = self.grava_conta_nova + nulo +","
            else:
               self.grava_conta_nova = self.grava_conta_nova + "'"+pl_ex[23]+"',"
            if pl_ex[24] == 'None':
               self.grava_conta_nova = self.grava_conta_nova + nulo +","
            else:
               self.grava_conta_nova = self.grava_conta_nova + "'"+pl_ex[24]+"',"
            if pl_ex[25] == 'None':
               self.grava_conta_nova = self.grava_conta_nova + nulo +","
            else:
               self.grava_conta_nova = self.grava_conta_nova + "'"+pl_ex[25]+"',"
            if pl_ex[26] == 'None':
               self.grava_conta_nova = self.grava_conta_nova + nulo +","
            else:
               self.grava_conta_nova = self.grava_conta_nova + "TIMESTAMP'"+pl_ex[26]+"',"
            if pl_ex[27] == 'None':
               self.grava_conta_nova = self.grava_conta_nova + nulo +","
            else:
               self.grava_conta_nova = self.grava_conta_nova + "'"+pl_ex[27]+"',"
            if pl_ex[28] == 'None':
               self.grava_conta_nova = self.grava_conta_nova + nulo +","
            else:
               self.grava_conta_nova = self.grava_conta_nova + "'"+pl_ex[28]+"',"
            if pl_ex[28] == 'None':
               self.grava_conta_nova = self.grava_conta_nova + nulo +");"
            else:
               self.grava_conta_nova = self.grava_conta_nova + "'"+pl_ex[29]+"');"
            ctbconta.write(self.grava_conta_nova+'\n')  
         ctbconta.close()
      self.desconecta_plan()
      # Referencia Fatos

      self.padrao_fatos = "INSERT INTO GER_REFERENCIA_FATOS (EMPRESA,REVENDA,REFFATO,CONTA,OPERACAO,CAMPO_ORIGEM,TIPO_TRANSACAO,TIPO_VALOR,ORIGEM,TIPO_TITULO,OPERACAO_TITULO,CAIXA,BANCO,CATEGORIA_OS,CONTRA_PARTIDA,RATEIO,NATUREZA,CONTA_PATRIMONIAL,CENTRO_CUSTO,TIPO_VAL_ATIVO,HISTORICO_PADRAO,PERMITE_INCLUSAO_MANUAL) VALUES"
      self.conecta_plan()
      with open('CTB_REFERENCIA_FATOS.SQL', 'w') as ctbfatos:
         self.fatos_pre = self.cursor_plan.execute("SELECT * FROM GER_REFERENCIA_FATOS ORDER BY conta_nova")
         for pl_ft in self.fatos_pre:
            self.grava_fatos_novos = self.padrao_fatos +"("+pl_ft[0]+","+pl_ft[1]+","+pl_ft[2]
            if pl_ft[22] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +",'"+pl_ft[4]+"','"+pl_ft[5]+"',"
            else:
               self.grava_fatos_novos = self.grava_fatos_novos + "'"+str(pl_ft[22])+"','"+pl_ft[4]+"','"+pl_ft[5]+"',"           
            if pl_ft[6] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos + "'"+str(pl_ft[6])+"',"
            if pl_ft[7] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos + "'"+str(pl_ft[7])+"',"            
            if pl_ft[8] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos +str(pl_ft[8])+"," 
            if pl_ft[9] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos + "'"+str(pl_ft[9])+"',"
            if pl_ft[10] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos +str(pl_ft[10])+"," 
            if pl_ft[11] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos +str(pl_ft[11])+"," 
            if pl_ft[12] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos +str(pl_ft[12])+"," 
            if pl_ft[13] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos +str(pl_ft[13])+"," 
            if pl_ft[23] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos + "'"+str(pl_ft[23])+"',"
            if pl_ft[15] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos +str(pl_ft[15])+"," 
            if pl_ft[16] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos + "'"+str(pl_ft[16])+"',"
            if pl_ft[17] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos +str(pl_ft[17])+"," 
            if pl_ft[18] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos +str(pl_ft[18])+"," 
            if pl_ft[19] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos +str(pl_ft[19])+"," 
            if pl_ft[20] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos +str(pl_ft[20])+"," 
            if pl_ft[21] == 'None':
               self.grava_fatos_novos = self.grava_fatos_novos + nulo +","
            else:
               self.grava_fatos_novos = self.grava_fatos_novos + "'"+str(pl_ft[21])+"');"
            ctbfatos.write(self.grava_fatos_novos+'\n')  
         ctbfatos.close()
      self.desconecta_plan()
      messagebox.showinfo('Fim','Processo finalizado.')
      caminho = os.path.abspath(os.path.dirname('.')) # Pega diretorio atual

   def fim_tela_aproc(self):
      self.tela_aproc.destroy()
   
   def busca_mascara(self):
      self.conecta_plan()
      self.cursor_plan.execute('select mascara from mascara_original')
      self.masc_ant1 = self.cursor_plan.fetchone()
      self.masc_ant = self.masc_ant1[0].replace('9','#')


   def aplicar_mascara(self, campo, mascara):
      campo_limpo = re.sub(r'\W+', '', campo)
      resultado = []
      j = 0
      for i in range(len(mascara)):
         if j >= len(campo_limpo):
            break
         if mascara[i] == '#':
            resultado.append(campo_limpo[j])
            j += 1
         else:
            resultado.append(mascara[i])
      return ''.join(resultado)

   def grava_masc(self):
      self.conecta_plan()
      for conta_nova, conta_mascara in self.plan_masc.items():
         pos = conta_mascara.rfind('.')
         if pos == -1:
            cta_sup = ''
         else:
            cta_sup1 = conta_mascara[0:pos]
            cta_sup = cta_sup1.replace('.','')  
            
         self.cursor_plan.execute('UPDATE PLANO_ESPELHADO set conta_editada_nova =?, conta_superiora_nova =? where conta_nova =?',(conta_mascara, cta_sup, conta_nova))
      self.banco_plan.commit()
      self.desconecta_plan()
      # Cria dicionario para GER_REFERENCIA_FATOS
      self.conecta_plan()
      self.muda_fatos = {}
      pega_contas = self.cursor_plan.execute('SELECT conta, conta_nova FROM plano_espelhado order by conta_nova')
      for pega_conta in pega_contas:
         self.muda_fatos[pega_conta[0]] = pega_conta[1]
      self.desconecta_plan()
      # Inicia atualização da GER_REFERENCIA_FATOS
      self.conecta_plan()
      for cta_velha, cta_nova  in self.muda_fatos.items():
         self.cursor_plan.execute('UPDATE ger_referencia_fatos SET conta_nova =? where conta =?',(cta_nova,cta_velha))
      self.banco_plan.commit()
      self.desconecta_plan()
      # Atualiza conta Contrapartida GER_REFERENCIA_FATOS
      self.conecta_plan()
      for cta_velha, cta_nova  in self.muda_fatos.items():
         self.cursor_plan.execute('UPDATE ger_referencia_fatos SET contrapartida_nova =? where contra_partida =?',(cta_nova,cta_velha))
      self.banco_plan.commit()
      self.desconecta_plan()


      messagebox.showinfo('Execução','Estruturação do plano de contas e \nApropriação da GER_REFERENCIA_FATOS Concluidas.')


      self.fim_tela_aproc()



   def pre_exportacao(self):
      self.plan_masc = {}
      mascara = self.ent_masc.get()
      self.conecta_plan()
      self.masc_sem = self.cursor_plan.execute('SELECT conta_nova FROM PLANO_ESPELHADO ORDER BY conta')   
      for campo in self.masc_sem:
         self.campo_masc = self.aplicar_mascara(campo[0],mascara) # Aplica mascara
         self.plan_masc[campo[0]] = self.campo_masc # Alimenta dicionario
      self.desconecta_plan()
      self.grava_masc()
      #print(self.plan_masc)

   def desfaz_relac(self, event):
      self.ckduplop = self.lista_ex.selection()
      for n in self.lista_ex.selection():
         conta, conta_nova, des_conta_nova = self.lista_ex.item(n, 'values')
         self.ex_cta_antiga = conta
         self.ex_cta_nova = conta_nova
         self.ex_descr_cta_nova = des_conta_nova
      self.conecta_plan()
      self.cursor_plan.execute('update plano_espelhado set conta_nova = ?, des_conta_nova = ? where conta = ?',('','',self.ex_cta_antiga))
      self.banco_plan.commit()
      self.cursor_plan.execute("update plano_origem set controle =? where conta =?", ('N',self.ex_cta_antiga))
      self.banco_plan.commit()
      self.cursor_plan.execute("update novo_plano set controle =? where conta =?",('N', self.ex_cta_nova))
      self.banco_plan.commit()
      self.desconecta_plan()
      self.monta_lista()

   def abandona_exc(self):
      self.tela_exclui_relac.destroy()

   def ClickDuplo(self, event):
      self.ckduplop = self.lista_ex.selection()
      for n in self.lista_ex.selection():
         conta, conta_nova, des_conta_nova = self.lista_ex.item(n, 'values')
         self.ex_cta_antiga = conta
         self.ex_cta_nova = conta_nova
         self.ex_descr_cta_nova = des_conta_nova
      self.exclui_relac()
            
   def monta_lista(self):
      self.lista_ex.delete(*self.lista_ex.get_children())
      self.conecta_plan()
      lista = self.cursor_plan.execute('''SELECT CONTA, CONTA_NOVA, DES_CONTA_NOVA FROM plano_espelhado order by conta''')
      for i in lista:
         self.lista_ex.insert('',END, values=i)
      self.desconecta_plan() 

   def lista_excecao(self):
      self.lista_ex = ttk.Treeview(self.frame_grid, columns=('CONTA', 'CONTA_NOVA', 'DES_CONTA_NOVA'), show='headings', selectmode = 'browse')
      self.lista_ex.heading('#1', text ='Conta Antiga') 
      self.lista_ex.heading('#2', text = 'Conta Nova')
      self.lista_ex.heading('#3', text = 'Descrição da Conta')
      self.lista_ex.column('#1', width=10)
      self.lista_ex.column('#2', width=10)
      self.lista_ex.column('#3', width=80)
      self.style = ttk.Style()
      self.style.configure('Treeview.Heading', foreground = 'black', font = ('Calibri', 13,'bold'))
      self.lista_ex.place(relx = 0.05, rely = 0.05, relheight=0.90, relwidth=0.90)
      self.scr_lista_exe = Scrollbar(self.frame_grid, orient='vertical', command = self.lista_ex.yview)
      self.lista_ex.configure(yscroll = self.scr_lista_exe)
      self.scr_lista_exe.place(relx = 0.95, rely = 0.05, relwidth = 0.03, relheight = 0.89)
      self.monta_lista()
      self.lista_ex.bind('<Double-1>', self.desfaz_relac)

   def frame_gridx(self):
      self.frame_grid = Frame(self.tela_relac, height=470, width=4000)
      self.frame_grid.pack(side = BOTTOM)
      
   def relaciona_contas(self):
      pass

   def inicializa_tabelas(self):
      self.conecta_plan()
      self.cursor_plan.execute('delete from novo_plano')
      self.cursor_plan.execute('delete from plano_origem')
      self.cursor_plan.execute('delete from mascara_original') 
      self.cursor_plan_execute('delete from plano_espelhado') 
      self.cursor_plan.execute('delete from ger_referencia_fatos')
      self.desconecta_plan()
   
   def verifica_tabela(self):
      self.conecta_plan()
      ver = self.cursor_plan.execute('select count(*) from plano_origem')      
      for verifica in ver:
         if verifica[0] != 0:
            self.desconecta_plan()
            return
         else:
            self.inicializa_tabelas()
            self.le_plano_base()
            self.lbl_msg = Label(self.conver, text = 'Tabelas necessárias para o processo do De-Para carregadas do DMS com sucesso.', font = 'verdana 15 bold', fg = 'green')
            self.desconecta_plan()
            return

   def verifica_plano_novo(self):
      self.conecta_plan()
      vernovo = self.cursor_plan.execute('select count(*) from novo_plano')      
      for verifica in vernovo:
         if verifica[0] == 0:
            messagebox.showinfo('Plano Novo','Plano de contas do cliente ainda não importado.\nFavor importar para continuar!')   
            self.desconecta_plan()
            return
         else:
            limpe = messagebox.askquestion('Plano Novo','Plano de contas do cliente já importado, ir para relacionamento de contas?')
            if limpe == 'yes':
               self.relacionamento()
               self.desconecta_plan()
               return
            else:
               self.desconecta_plan()
               return

   def abre_origem(self):
      self.caminho = os.path.abspath(os.path.dirname('.'))
      self.arq_ori = filedialog.askopenfilename(initialdir=self.caminho, 
                                            title = "Selecione um arquivo" , 
                                            filetypes=(("Arquivos CSV", "*.csv"), ("","*.CSV")),)

      self.arq_abr = self.arq_ori
      with open(self.arq_abr, 'r', encoding='utf8') as csvfile:
         novoplano = csv.reader(csvfile, delimiter=';')
         self.lbl_importa = Label(self.conver, text = self.arq_abr, font = ('verdana 12 bold'))      
         self.lbl_importa.place(relx = 0.40, rely = 0.20)
         for n_plano in novoplano:
            self.conecta_plan()
            self.cursor_plan.execute('insert into novo_plano (conta,descricao_conta) values(?, ?)',(n_plano[0], n_plano[1]))
            self.banco_plan.commit()
            self.desconecta_plan()
         messagebox.showinfo('Importação CSV','Arquivo CSV importado com sucesso!')       

   def le_plano_base(self):
      self.conecta_DB()
      self.le_plan_ori = self.cursor.execute('select * from ctb_conta')
      for self.plan_ori in self.le_plan_ori:
         self.EMPRESA = str(self.plan_ori[0])
         self.REVENDA = str(self.plan_ori[1])
         self.CONTA = str(self.plan_ori[2])
         self.CONTA_SUPERIORA = str(self.plan_ori[3])
         self.CONTA_EDITADA = str(self.plan_ori[4])
         self.COSIF = str(self.plan_ori[5])
         self.DES_CONTA = str(self.plan_ori[6])
         self.NATUREZA = str(self.plan_ori[7])
         self.NIVEL = str(self.plan_ori[8])
         self.REDUZIDO = str(self.plan_ori[9])
         self.RELATORIOS = str(self.plan_ori[10])
         self.LANCAMENTO_DIVIDIDO = str(self.plan_ori[11])
         self.ACEITA_SUMARIZACAO = str(self.plan_ori[12])
         self.CODIGO = str(self.plan_ori[13])
         self.OPERACAO = str(self.plan_ori[14])
         self.CONTA_REFERENCIAL = str(self.plan_ori[15])
         self.COD_AGLUTINADORA = str(self.plan_ori[16])
         self.NATUREZA_GRUPO = str(self.plan_ori[17])
         self.NIVEL_DIVISAO = str(self.plan_ori[18])
         self.CONTA_HARLEY = str(self.plan_ori[19])
         self.CONTA_REFERENCIAL_FCONT = str(self.plan_ori[20])
         self.INATIVO_CONSULTAS = str(self.plan_ori[21])
         self.DTA_INCLUSAO = str(self.plan_ori[22])
         self.CONTA_TRANSFERENCIA = str(self.plan_ori[23])
         self.ANOMES_TRANSFERENCIA = str(self.plan_ori[24])
         self.COD_CENTRO_CUSTO_ECF = str(self.plan_ori[25])
         self.conecta_plan()
         self.cursor_plan.execute('Insert into plano_origem (empresa, revenda, conta, des_conta) values(?,?,?,?)',(
                  self.EMPRESA,self.REVENDA,self.CONTA,self.DES_CONTA))
         self.banco_plan.commit()
         self.cursor_plan.execute('Insert into plano_espelhado (EMPRESA,REVENDA,CONTA,CONTA_SUPERIORA,CONTA_EDITADA,COSIF,DES_CONTA,NATUREZA,NIVEL,REDUZIDO,RELATORIOS,LANCAMENTO_DIVIDIDO,ACEITA_SUMARIZACAO,CODIGO,OPERACAO,CONTA_REFERENCIAL,COD_AGLUTINADORA,NATUREZA_GRUPO,NIVEL_DIVISAO,CONTA_HARLEY,CONTA_REFERENCIAL_FCONT,INATIVO_CONSULTAS,DTA_INCLUSAO,CONTA_TRANSFERENCIA,ANOMES_TRANSFERENCIA,COD_CENTRO_CUSTO_ECF) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                  (self.EMPRESA,self.REVENDA,self.CONTA,self.CONTA_SUPERIORA,self.CONTA_EDITADA,self.COSIF,self.DES_CONTA,
                  self.NATUREZA,self.NIVEL,self.REDUZIDO,self.RELATORIOS, self.LANCAMENTO_DIVIDIDO, self.ACEITA_SUMARIZACAO,
                  self.CODIGO,self.OPERACAO,self.CONTA_REFERENCIAL,self.COD_AGLUTINADORA,self.NATUREZA_GRUPO,self.NIVEL_DIVISAO,
                  self.CONTA_HARLEY,self.CONTA_REFERENCIAL_FCONT,self.INATIVO_CONSULTAS,self.DTA_INCLUSAO,self.CONTA_TRANSFERENCIA,
                  self.ANOMES_TRANSFERENCIA,self.COD_CENTRO_CUSTO_ECF))
         self.banco_plan.commit()

      self.le_fato_ori = self.cursor.execute('select * from ger_referencia_fatos')
      for fato in self.le_fato_ori:
         self.EMPRESA = fato[0]
         self.REVENDA = fato[1]
         self.REFFATO = fato[2]
         self.CONTA = fato[3]
         self.OPERACAO = fato[4]
         self.CAMPO_ORIGEM = fato[5]
         self.TIPO_TRANSACAO = fato[6]
         self.TIPO_VALOR = fato[7]
         self.ORIGEM = fato[8]
         self.TIPO_TITULO = fato[9]
         self.OPERACAO_TITULO = fato[10]
         self.CAIXA = fato[11]
         self.BANCO = fato[12]
         self.CATEGORIA_OS = fato[13]
         self.CONTRA_PARTIDA = fato[14]
         self.RATEIO = fato[15]
         self.NATUREZA = fato[16]
         self.CONTA_PATRIMONIAL = fato[17]
         self.CENTRO_CUSTO = fato[18]
         self.TIPO_VAL_ATIVO = fato[19]
         self.HISTORICO_PADRAO = fato[20]
         self.PERMITE_INCLUSAO_MANUAL = fato[21]
         self.cursor_plan.execute('insert into ger_referencia_fatos values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(
                        self.EMPRESA,self.REVENDA,self.REFFATO,self.CONTA,self.OPERACAO,self.CAMPO_ORIGEM,self.TIPO_TRANSACAO,
                        self.TIPO_VALOR,self.ORIGEM,self.TIPO_TITULO,self.OPERACAO_TITULO,self.CAIXA,self.BANCO,self.CATEGORIA_OS,
                        self.CONTRA_PARTIDA,self.RATEIO,self.NATUREZA,self.CONTA_PATRIMONIAL,self.CENTRO_CUSTO,self.TIPO_VAL_ATIVO,
                        self.HISTORICO_PADRAO,self.PERMITE_INCLUSAO_MANUAL))
         self.banco_plan.commit()

      self.le_mascara = self.cursor.execute('select * from ctb_mascara')
      for masc in self.le_mascara:
         self.EMPRESA = masc[0]
         self.REVENDA = masc[1]
         self.GRUPO_CONTABIL = masc[2]
         self.MASCARA= masc[3]
         self.cursor_plan.execte('insert into mascara_original (EMPRESA, REVENDA, GRUPO_CONTABIL, MASCARA) values (?,?,?,?)',(self.EMPRESA, self.REVENDA, self.GRUPO_CONTABIL, self.MASCARA))
         self.banco_plan.commit()
      self.desconecta_plan()

   def sai_relacao(self):
      self.desconecta_plan()
      self.frame_grid.destroy()
      self.tela_relac.destroy()

   def grava_relacao(self):
      tmp_origem = self.lista_ori.get()
      pos_ori = tmp_origem.find('-')
      self.cta_origem = tmp_origem[0:pos_ori-1]
      self.des_origem = tmp_origem[pos_ori+2:]
      tmp_destino = self.lista_des.get()
      pos_des = tmp_destino.find('-')
      self.cta_destino = tmp_destino[0:pos_des-1]
      self.des_destino = tmp_destino[pos_des+2:]
      if self.ent_nova_desc.get() == '':
         self.descricao = self.des_origem
      else:
         self.descricao = self.ent_nova_desc.get()   
      self.conecta_plan()
      self.cursor_plan.execute('update plano_espelhado set conta_nova = ?, des_conta_nova = ? where conta = ?',(self.cta_destino,self.descricao,self.cta_origem))
      self.banco_plan.commit()
      self.cursor_plan.execute("update plano_origem set controle =? where conta =?", ('S',self.cta_origem))
      self.banco_plan.commit()
      self.cursor_plan.execute("update novo_plano set controle =? where conta =?",('S', self.cta_destino))
      self.banco_plan.commit()
      self.desconecta_plan()
      self.ent_nova_desc.delete(0,END)
      self.lista_ori.destroy()
      self.lista_des.destroy()
      self.lista_contas1()
      self.monta_lista()

   def lista_contas1(self):
      self.conecta_plan()
      self.lbl_ori = Label(self.tela_relac, text = 'Plano de contas origem', font=('verdana', 8, 'bold'))
      self.lbl_ori.place(relx = 0.05, rely=0.05)
      self.cursor_plan.execute("SELECT conta, des_conta FROM plano_origem where controle <> 'S' order by conta")
      self.combo_ori = []
      for linha in self.cursor_plan.fetchall():
         self.combo_ori.append(str(linha[0]) + ' - ' + str(linha[1]))
      self.lista_ori = ttk.Combobox(self.tela_relac, value = self.combo_ori, width = 45)
      self.lista_ori.place(relx=0.05, rely=0.08)
      self.lista_ori.set('Selecione a Conta Origem')
      self.lbl_des = Label(self.tela_relac, text = 'Plano de contas destino', font=('verdana', 8, 'bold'))
      self.lbl_des.place(relx = 0.40, rely=0.05)
      self.conecta_plan()
      self.cursor_plan.execute("SELECT conta, descricao_conta FROM novo_plano where controle <> 'S' order by conta ")
      self.combo_des = []
      for linha in self.cursor_plan.fetchall():
         self.combo_des.append(str(linha[0]) + ' - ' + str(linha[1]))
      self.lista_des = ttk.Combobox(self.tela_relac, value = self.combo_des, width = 45)
      self.lista_des.place(relx=0.40, rely=0.08)
      self.lista_des.set('Selecione a Conta do novo Plano')
      self.lbl_nova_desc = Label(self.tela_relac, text = 'Nova Descrição', font=('verdana', 8, 'bold'))
      self.lbl_nova_desc.place(relx = 0.40, rely = 0.12)
      self.ent_nova_desc = Entry(self.tela_relac, width= 48)
      self.ent_nova_desc.place(relx = 0.40, rely = 0.15)      

   def lista_contas(self):
      self.conecta_plan()
      self.lbl_ori = Label(self.tela_relac, text = 'Plano de contas origem', font=('verdana', 8, 'bold'))
      self.lbl_ori.place(relx = 0.05, rely=0.05)
      self.cursor_plan.execute("SELECT conta, des_conta FROM plano_origem where controle <> 'S' order by conta")
      self.combo_ori = []
      for linha in self.cursor_plan.fetchall():
         self.combo_ori.append(str(linha[0]) + ' - ' + str(linha[1]))
      self.lista_ori = ttk.Combobox(self.tela_relac, value = self.combo_ori, width = 45)
      self.lista_ori.place(relx=0.05, rely=0.08)
      self.lista_ori.set('Selecione a Conta Origem')
      self.lbl_des = Label(self.tela_relac, text = 'Plano de contas destino', font=('verdana', 8, 'bold'))
      self.lbl_des.place(relx = 0.40, rely=0.05)
      self.conecta_plan()
      self.cursor_plan.execute("SELECT conta, descricao_conta FROM novo_plano where controle <> 'S' order by conta ")
      self.combo_des = []
      for linha in self.cursor_plan.fetchall():
         self.combo_des.append(str(linha[0]) + ' - ' + str(linha[1]))
      self.lista_des = ttk.Combobox(self.tela_relac, value = self.combo_des, width = 45)
      self.lista_des.place(relx=0.40, rely=0.08)
      self.lista_des.set('Selecione a Conta do novo Plano')
      self.lbl_nova_desc = Label(self.tela_relac, text = 'Nova Descrição', font=('verdana', 8, 'bold'))
      self.lbl_nova_desc.place(relx = 0.40, rely = 0.12)
      self.ent_nova_desc = Entry(self.tela_relac, width= 48)
      self.ent_nova_desc.place(relx = 0.40, rely = 0.15)
#      self.ent_nova_desc.insert(0,'Em branco mantêm a mesma')
      self.frame_gridx()
      self.lista_excecao()
      self.lbl_msg1 = Label(self.tela_relac, text = 'Clique duplo sobre a linha do quadro abaixo para excluir a relação.', font = 'arial 10 bold' , fg = 'red')
      self.lbl_msg1.place(relx = 0.05, rely = 0.22)
      self.btn_confirma = Button(self.tela_relac, text = 'Grava',  bg = '#D3D3D3', font = 'Arial 12 bold', width= 10, fg = 'green', command = self.grava_relacao)
      self.btn_confirma.place(relx = 0.73, rely = 0.06)
      self.btn_cancela = Button(self.tela_relac, text = 'Cancela',  bg = '#D3D3D3', font = 'Arial 12 bold', width= 10, fg = 'red', command = self.sai_relacao)
      self.btn_cancela.place(relx = 0.86, rely = 0.06)

## BLOCO CENTRO DE CUSTOS