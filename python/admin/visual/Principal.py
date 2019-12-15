'''
Created on 16 de nov de 2019

@author: jeff
'''
import gi 
from gi.repository import Gtk


gi.require_version("Gtk","3.0")
class Principal():
        
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("Principal.glade")
        self.PriWin = builder.get_object("PriWin")
        
        self.PriWin.connect("destroy",Gtk.main_quit)
        builder.connect_signals(self)
        self.PriWin.show_all()
        Gtk.main()
        
prin = Principal()