import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
class any:
    def ir(self,evt):
        pass
        #pegar infos do banco
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("graficosAnos.glade")
        self.graficosAnos = builder.get_object("winGranos") 
        self.atraso = builder.get_object("cbtAnu")  
        builder.connect_signals(self)
        self.graficosAnos.show_all()
        self.graficosAnos.connect("destroy", Gtk.main_quit)
        Gtk.main()
    
    if '''serie do banco''' == '1° Ano':
        def criar(self,evt):
            self.pax(evt)
            priAno = [self.priago,self.priset,self.priout,self.prinov,self.pridez]            
                    
            barWidth=(0.25)
            plt.figure(figsize=(10,5))
            r1 = np.arange(len(priAno))
            
            plt.bar(r1, priAno, color ='#6A5ACD', width=barWidth, label="1° ano" )

            plt.xlabel('Meses')
            plt.xticks([r + barWidth for r in range(len(priAno))],['Agosto','Setembro','Outubro',' Novembro  ','Dezembro'])
            plt.ylabel('Avaliação Média')
            plt.title('Seu Desempenho')
            
            plt.legend()
            plt.show()        
        
    if '''serie do banco''' == '2° Ano':
        def criar(self,evt):
            self.pax(evt)            
            segAno = [self.segfev,self.segmar,self.segabr,self.segmai,self.segjun,self.segago,self.segset,self.segout,self.segnov,self.segdez]            
                    
            barWidth=(0.25)
            plt.figure(figsize=(10,5))
            r1 = np.arange(len(segAno))
            
            plt.bar(r1, segAno, color ='#6A5ACD', width=barWidth, label="1° ano" )
        
            plt.xlabel('Meses')
            plt.xticks([r + barWidth for r in range(len(priAno))],['Fevereiro','Março','Abril','Maio','Junho','Agosto','Setembro','Outubro',' Novembro  ','Dezembro'])    
            plt.ylabel('Avaliação Média')
            plt.title('Seu Desempenho')
            
            plt.legend()
            plt.show()        
        
    if '''serie do banco''' == '3° Ano': 
        def criar(self,evt):
            self.pax(evt)            
            terAno = [self.terfev,self.termar,self.terabr,self.termai,self.terjun,self.terago,self.terset,self.terout,self.ternov,self.terdez]
                    
            barWidth=(0.25)
            plt.figure(figsize=(10,5))
            r1 = np.arange(len(terAno))
            
            plt.bar(r1, terAno, color ='#6A5ACD', width=barWidth, label="1° ano" )
            
            plt.xlabel('Meses')
            plt.xticks([r + barWidth for r in range(len(terAno))],['Fevereiro','Março','Abril','Maio','Junho'])
            plt.ylabel('Avaliação Média')
            plt.title('Seu Desempenho')
            
            plt.legend()
            plt.show()        