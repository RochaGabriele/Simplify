'''
Created on 28 de set de 2019

@author: jeff
'''
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

from admin.visual.CssLogin import CssLogin
from admin.visual.Login import Login



class Ent():
 
    def teste(self):
        print("Teste")
    def cont(self,evt):
        self.ent.hide()
        self.a = Login()
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("admin/visual/ent.glade")
        self.ent = builder.get_object("entApli")
        self.but = builder.get_object("butEnt")
        self.ent.connect("destroy",Gtk.main_quit)
        builder.connect_signals(self)
        CssL = CssLogin()
        CssL.cad_style()
        self.ent.show()
        Gtk.main()
