"""
@author: Gabriele Rocha
"""

import gi
from gi.repository import Gtk, Gdk


gi.require_version("Gtk","3.0")


class CssLogin:
    def cad_style(self):
        css = b"""
                
            .butLogCad{
                
                    background-color:#000;
                    color:#fff;
            
            }
            
            .matAlu{
            
                    border-bottom:2px solid #000;
                    border-top:none;
                    border-right:none;
                    border-left:none;
            }
            
            .txtLogin{
                    
                    font-size:30px;
                    font-weight:bold;
                    font-family:Hammersmith One;
                    color:#000;
                
            }
            
            .LabTextLoa{
                
                font-size:30px;
                font-weight:bold;
                font-family:Hammersmith One;
                color:#000;
            
            }
            
            .inp{
                
                border-bottom:2px solid #000;
                border-top:none;
                border-right:none;
                border-left:none;
            
            }
            
            .apaCam{
                
               background-color:#fff;
               border:none;
               color:#000;
               font-family:Sanchez;
            }
          
        """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)
