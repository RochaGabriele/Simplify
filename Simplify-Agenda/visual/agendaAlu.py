import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk
from controle.agendaControle import agendaControle
from modelo.agendaMo import agendaMo
from controle.dados import dados
class agendaAlu():
    def __init__(self):
        builder = Gtk.Builder()
        "JANELA CALENDARIO PRINCIPAL"
        builder.add_from_file("ageAlu.glade")
        self.janela = builder.get_object("ageAlu")
        self.calen = builder.get_object("calageAlu")
        self.verOrd = builder.get_object("verOAlu")
        self.verAE = builder.get_object("verAlu")
        self.bVerO = builder.get_object("butVO")
        self.bverAE = builder.get_object("butVAE")
    
        "JANELA PARA VER ORDEM DAS SALAS"
        self.verSal = builder.get_object("TabAlu")
        self.priS = builder.get_object("lbVPriAlu")
        self.segS = builder.get_object("lbVSegAlu")
        self.terS = builder.get_object("lbVTerAlu")
        self.quarS = builder.get_object("lbVQuarAlu")
        self.quinS = builder.get_object("lbVQuinAlu")
        self.sexS = builder.get_object("lbVSexAlu")
        self.setS = builder.get_object("lbVSetAlu")
        self.oiS = builder.get_object("lbVOiAlu")
        self.noS = builder.get_object("lbVNoAlu")
        self.fecS = builder.get_object("btfecSAlu")
        self.lab1 = builder.get_object("lb1Alu")
        self.lab2 = builder.get_object("lb2Alu")
        self.lab3 = builder.get_object("lb3Alu")
        self.lab4 = builder.get_object("lb4Alu")
        self.lab5 = builder.get_object("lb5Alu")
        self.lab6 = builder.get_object("lb6Alu")
        self.lab7 = builder.get_object("lb7Alu")
        self.lab8 = builder.get_object("lb8Alu")
        self.lab9 = builder.get_object("lb9Alu")
        
        "JANELA PARA VER ORDEM DOS AES"
        self.vAE = builder.get_object("LAEAlu")
        self.labAE = builder.get_object("lbAEAlu")
        self.labAS1 = builder.get_object("lbAS1Alu")
        self.labAS2 = builder.get_object("lbAS2Alu")
        self.labAS3 = builder.get_object("lbAS3Alu")
        self.labAS4 = builder.get_object("lbAS4Alu")
        self.labAS5 = builder.get_object("lbAS5Alu")
        self.labAS6 = builder.get_object("lbAS6Alu")
        self.labAS7 = builder.get_object("lbAS7Alu")
        self.labAS8 = builder.get_object("lbAS8Alu")
        self.labAS9 = builder.get_object("lbAS9Alu")
        self.labAE1 = builder.get_object("lbAE1Alu")
        self.labAE2 = builder.get_object("lbAE2Alu")
        self.labAE3 = builder.get_object("lbAE3Alu")
        self.labAE4 = builder.get_object("lbAE4Alu")
        self.labAE5 = builder.get_object("lbAE5Alu")
        self.labAE6 = builder.get_object("lbAE6Alu")
        self.labAE7 = builder.get_object("lbAE7Alu")
        self.labAE8 = builder.get_object("lbAE8Alu")
        self.labAE9 = builder.get_object("lbAE9Alu")
        self.fecAE = builder.get_object("btfecAAlu")
        builder.connect_signals(self)
        self.janela.show_all()
        Gtk.main()
        Gtk.main_quit()
        "SINAIS PARA JANELA PRINCIPAL"
    def verOrdem(self,evt):
        self.verSal.show_all()
    def fecOrdem(self,evt):
        self.verSal.hide()
    def verAES(self,evt):
        self.vAE.show_all()
    def fecAES(self,evt):
        self.vAE.hide()
ageA = agendaAlu()