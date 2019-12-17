"""
@author: jefferson Oliveira
"""
import gi
from gi.repository import Gtk, Gdk


gi.require_version("Gtk","3.0")


class CadAluCss:
    def cadStyle(self):
        css = b"""
                .btnCadastrar{
                    
                    background-color:#000;
                    color:#fff;
                    border:2px solid #fff;
                    
                }
                .top{
                    
                    background-color:#000;
                    border-radius:10px 10px 0px 0px;
                    color:#fff;
                }
                .cadI{
                     
                     border-top:none;
                     border-right:none;
                     border-left:none;
                     border-bottom:2px solid #fff;
                     color:#fff;
                     background-color:#000;
                     
                     
                }
                .boxCad{
                    
                    background-color:#000;
                }
                          
        """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)
