import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from visual.cssDados import CssDados
class DadosAdm:
    
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/DadosAdm.glade")
        self.dpAdm = builder.get_object("dpAdm")
        self.labAdmName = builder.get_object("labAdmName")
        self.labAdmUser = builder.get_object("labAdmUser")
        self.labAdmCar = builder.get_object("labAdmCar")
        builder.connect_signals(self)
        self.dpAdm.connect("destroy",Gtk.main_quit)
        cssD = CssDados()
        cssD.dad_style()
        self.dpAdm.show_all()

        