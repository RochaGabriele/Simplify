'''
Created on 14 de dez de 2019

@author: jeff
'''

import gi
from gi.repository import Gtk, Gdk


gi.require_version("Gtk","3.0")


class testecss:
    def ctes(self):
        css = b"""
                .dadLabb{
                        
                        background-color:#000;
                        font-size:30px;
                        
                }
        """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)