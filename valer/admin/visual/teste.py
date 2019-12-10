import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
from pontuC import pontuC
class teste:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("lista.glade")
        self.inst = builder.get_object("winLista")
        builder.connect_signals(self)
        self.inst.show_all()
        self.inst.connect("destroy",Gtk.main_quit)
        Gtk.main()
    
    def informacoes(self):
        builder = Gtk.Builder()
        builder.add_from_file("graficos.glade")
        self.graficos = builder.get_object("winGraficos")
        builder.connect_signals(self)
        self.graficos.show_all()
        self.graficos.connect("destroy",Gtk.main_quit)
        Gtk.main()
        
    def upd(self):
        builder = Gtk.Builder()
        builder.add_from_file("upd.glade")
        self.upda = builder.get_object("winUpd")
        builder.connect_signals(self)
        self.upda.show_all()
        self.upda.connect("destroy",Gtk.main_quit)
        Gtk.main()
        
    def window1(self):
        builder = Gtk.Builder()
        builder.add_from_file("NovUm.glade")
        self.NovUm = builder.get_object("winEnt")   
        ##self.gtk_style()
        builder.connect_signals(self)
        self.NovUm.show_all()
        self.NovUm.connect("destroy", Gtk.main_quit)
        Gtk.main()

    def window2(self):
        builder = Gtk.Builder()
        builder.add_from_file("NovDoi.glade")
        self.NovDoi = builder.get_object("winCom")       
        builder.connect_signals(self)
        self.NovDoi.connect("destroy", Gtk.main_quit)
        ##self.gtk_style()
        self.NovDoi.show_all()
        
    def window3(self):
        builder = Gtk.Builder()
        builder.add_from_file("NovTre.glade")
        self.NovTre = builder.get_object("winRec")       
        builder.connect_signals(self)
        self.NovTre.connect("destroy", Gtk.main_quit)
        ##self.gtk_style()
        self.NovTre.show_all()
        
    def window4(self):
        builder = Gtk.Builder()
        builder.add_from_file("repro.glade")
        self.repro = builder.get_object("winRep")       
        builder.connect_signals(self)
        self.repro.connect("destroy", Gtk.main_quit)
        ##self.gtk_style()
        self.repro.show_all()
            
    def window5(self):
        builder = Gtk.Builder()
        builder.add_from_file("apro.glade")
        self.apro = builder.get_object("winApro")       
        builder.connect_signals(self)
        self.apro.connect("destroy", Gtk.main_quit)
        #self.gtk_style()
        self.apro.show_all()
    
    def window6(self):
        builder = Gtk.Builder()
        builder.add_from_file("media.glade")
        self.media = builder.get_object("winAvaliar")  
        self.atraso = builder.get_object("cbtAtr")
        self.assiduo = builder.get_object("cbtAss")
        self.ocorrencia = builder.get_object("cbtOco")
        self.postura = builder.get_object("cbtPos")
        self.desempenho = builder.get_object("cbtDes")     
        builder.connect_signals(self)
        self.media.connect("destroy", Gtk.main_quit)
        self.media.show_all()
        
    def window7(self):
        builder = Gtk.Builder()
        builder.add_from_file("cadastro.glade")
        self.cadastro = builder.get_object("winCadastro") 
        self.nomeComp = builder.get_object("entNome")  
        self.curso = builder.get_object("cbtCurso")
        self.serie = builder.get_object("cbtSerie")
        builder.connect_signals(self)
        self.cadastro.connect("destroy", Gtk.main_quit)
        #self.gtk_style()
        self.cadastro.show_all()
    
    def info(self,evt):   
        self.informacoes()
        
    def editar(self,evt):
        self.upd()
        
    def remover(self,evt):
        pass
    
    def avaliar(self,evt):
        self.window1()
        
    def entendi(self,evt):
        self.NovUm.hide()
        self.window2()
        
    def comecar(self,evt):
        self.NovDoi.hide()
        self.window3()
        
    def naodeu(self,evt):
        self.NovTre.hide()
        self.window4()
        
    def prox(self,evt):
        self.NovTre.hide()
        self.window6()
     
    def calNovA(self,evt):
        self.apro.hide()
        self.window7()
    
    def calNovR(self,evt):
        self.repro.hide()
        self.window3()
        
    def mostra(self,evt):
        self.ok = pontuC()
        m = self.ok.calc(self.atraso.get_active_text(),self.assiduo.get_active_text(),self.ocorrencia.get_active_text(),self.postura.get_active_text(),self.desempenho.get_active_text())
        if m < 35:
            self.media.hide()
            self.window4()
        else:
            self.media.hide()
            self.window5()
            
    def algoBanco(self,evt):
        self.ok = pontuC()
        
    def canUpd(self,evt):
        self.upda.destroy()
        
    def closGra(self,evt):
        self.graficos.destroy()
        
    def bacDois(self,evt):
        self.NovDoi.destroy()
        self.window1()
        
    def canRepro(self,evt):
        self.repro.destroy()
        
    def canApro(self,evt):
        self.apro.destroy()
     
a = teste()