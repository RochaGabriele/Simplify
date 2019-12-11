import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk


class CssDados:
    def dad_style(self):
        css = b"""
                
            .labDad{
                    
            
            }
          
        """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)