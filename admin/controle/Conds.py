'''
Created on 14 de nov de 2019

@author: jeff
'''


#import re
#from django.forms import forms

class Conds():
        
    
    def Campos_em_branco(self,mat):
        if mat == "":
            return True
    def CamposEmbrancoLog(self,a,b):
        if  a  == "" or b == "" :
            return True 
    def null_fields(self,nomC,nomU,cargo,sen,conSen):
        if nomC == "" or nomU == "" or cargo == "" or sen == "" or conSen == "" :
            return True
    def senhasDiferem(self,a,b):
        if a != b :
            return True
    def camposEmBracoCad(self,a,b):   
        if a == "" or b == "":
            return True
    def makeFieldsBlank(self,a,b,c,d,e):
                a.set_text("")
                b.set_text("")
                c.set_text("")
                d.set_text("")
                e.set_text("")
 