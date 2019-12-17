'''
@author:Jefferson Oliveira
Janela usada para testes
'''


import gi
from gi.repository import Gtk


gi.require_version("Gtk", "3.0")



class DadosAlu():
    
    
   
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("admin/visual/DadosAlu.glade")
        self.dapWin = builder.get_object("dapWin")
        self.lama = builder.get_object("lama")
        self.labSerie = builder.get_object("labSerie")
        self.labCurso = builder.get_object("labCurso")
        self.labName = builder.get_object("labName")
        self.dapWin.connect("destroy",Gtk.main_quit)
        builder.connect_signals(self)
        self.dapWin.show_all()
        Gtk.main()

