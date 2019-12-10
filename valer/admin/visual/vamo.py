"""    

        classe utilizada para a criação do visual do gráfico
"""

__author__="Gabriele rocha Barbosa"
__version__="1.0.1"

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
import numpy as np
import matplotlib.pyplot as plt
class vamo:
    def graph(self,evt):
        self.inst.hide()
        self.win2()
    
    '''
    FAZER OS WHERE DA MATRICULA
    '''
    if '''serie da tela graficos''' == '1':    
        
        priago = 0.0 #N EXISTE SE N VAI ZERAR
        priset = 0.0
        priout = 0.0
        prinov = 0.0
        pridez = 0.0
        def pax(self,evt):
            m = int(self.atraso.get_active_text())+int(self.assiduo.get_active_text())+int(self.postura.get_active_text())+int(self.desempenho.get_active_text())+int(self.ocorrencia.get_active_text())
            if self.mes.get_active_text() == 'Agosto':
                self.priago = m/5 #update no banco da coluna mes
                return self.priago
            if self.mes.get_active_text() == 'Setembro':
                self.priset = m/5
                return self.priset
            if self.mes.get_active_text() == 'Outubro':
                self.priout = m/5
                return self.priout
            if self.mes.get_active_text() == 'Novembro':
                self.prinov = m/5
                return self.prinov
            if self.mes.get_active_text() == 'Dezembro':
                self.pridez = m/5
                return self.pridez
            
            self.atraso.set_active(0)
            self.assiduo.set_active(0)         
            self.ocorrencia.set_active(0)         
            self.postura.set_active(0)         
            self.desempenho.set_active(0)
            
    
    if '''serie do banco''' == '2':    

        def pax(self,evt):
            m = int(self.atraso.get_active_text())+int(self.assiduo.get_active_text())+int(self.postura.get_active_text())+int(self.desempenho.get_active_text())+int(self.ocorrencia.get_active_text())
            if self.mes.get_active_text() == 'Fevereiro':
                self.segfev = m/5
                return self.segfev
            if self.mes.get_active_text() == 'Março':
                self.segmar = m/5
                return self.segmar
            if self.mes.get_active_text() == 'Abril':
                self.segabr = m/5
                return self.segabr
            if self.mes.get_active_text() == 'Maio':
                self.segmai = m/5
                return self.segmai
            if self.mes.get_active_text() == 'Junho':
                self.segjun = m/5
                return self.segjun
            if self.mes.get_active_text() == 'Agosto':
                self.segago = m/5
                return self.segago
            if self.mes.get_active_text() == 'Setembro':
                self.segset = m/5
                return self.segset
            if self.mes.get_active_text() == 'Outubro':
                self.segout = m/5
                return self.segout
            if self.mes.get_active_text() == 'Novembro':
                self.segnov = m/5
                return self.segnov
            if self.mes.get_active_text() == 'Dezembro':
                self.segdez = m/5
                return self.segdez
            
            self.atraso.set_active(0)
            self.assiduo.set_active(0)         
            self.ocorrencia.set_active(0)         
            self.postura.set_active(0)         
            self.desempenho.set_active(0)
                 
            
    if '''serie do banco''' == '3':

        def pax(self,evt):
            m = int(self.atraso.get_active_text())+int(self.assiduo.get_active_text())+int(self.postura.get_active_text())+int(self.desempenho.get_active_text())+int(self.ocorrencia.get_active_text())
            if self.mes.get_active_text() == 'Fevereiro':
                self.terfev = m/5
                return self.ter
            if self.mes.get_active_text() == 'Março':
                self.termar = m/5
                return self.termar
            if self.mes.get_active_text() == 'Abril':
                self.terabr= m/5
                return self.terabr
            if self.mes.get_active_text() == 'Maio':
                self.termai = m/5
                return self.termai
            if self.mes.get_active_text() == 'Junho':
                self.terjun = m/5
                return self.terjun
        
            self.atraso.set_active(0)
            self.assiduo.set_active(0)         
            self.ocorrencia.set_active(0)         
            self.postura.set_active(0)         
            self.desempenho.set_active(0)
            
'''
def criar(self,z): 
        
        
        #pegar os valores tabelas do banco
        priAno = [self.prifev,self.primar,self.priabr,self.primai,self.prijun,self.priago,self.priset,self.priout,self.prinov,self.pridez]
        #
        
                
        barWidth=(0.25)
        plt.figure(figsize=(10,5))
        r1 = np.arange(len(priAno))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]
        
        plt.bar(r1, priAno, color ='#6A5ACD', width=barWidth, label="1° ano" )
        plt.bar(r2, segAno, color ='#6495ED', width=barWidth, label="2° ano" )
        plt.bar(r3, terAno, color ='#00BFFF', width=barWidth, label="3° ano" )
        
        plt.xlabel('Meses')
        plt.xticks([r + barWidth for r in range(len(priAno))],['Fevereiro','Março','Abril','Maio','Junho','Agosto','Setembro','Outubro',' Novembro  ','Dezembro'])
        plt.ylabel('Avaliação Média')
        plt.title('Seu Desempenho')
        
        plt.legend()
        plt.show()
        
'''

