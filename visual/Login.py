'''
Created on 28 de set de 2019

@author: jeff
'''
import gi 
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from controle.PegarDados import PegarDados
from visual.DadosAlu import DadosAlu
from controle.Conds import Conds
from modelo.Admin import Admin
from visual.DadosAdm import DadosAdm
from controle.AdminControle import AdminControle
from visual.CssLogin import CssLogin
class Login():
        
    def manCad(self):
        self.LabTextLoa.hide()
    
   
               
    def entrar(self,evt):   
        con = Conds()
        if con.Campos_em_branco(self.matAlu.get_text()) == True:
            self.labMat.set_text("Campo matricula em branco, por favor prenchelo")
        else:
            self.login.hide()
            self.dad = DadosAlu()
          
                 
    def entrarAdm(self,evt):
        con = Conds()
        if con.CamposEmbrancoLog(self.useAdm.get_text(),self.senAdm.get_text()) == True :
            self.labAvi.set_text("Não deixe campo em branco")
        
           
        
        else:
            control = AdminControle()
            test = control.selecionarTodos()
            print(self.useAdm.get_text())
            print(self.senAdm.get_text())
            for i in range(0,test.__len__(),1):
            
                if(self.useAdm.get_text() == test[i].getUser() and self.senAdm.get_text() == test[i].getSenha()):
                    adm = DadosAdm()
                    adm.dpAdm.show()
                else:
                    print("error")
            
            
            
            
    def cadasAdm(self,evt):
        con = Conds()
        pd = PegarDados()
        pd.getDadosCad(self.nomCad.get_text(), 
                            self.carCad.get_text(), 
                            self.nomUseCad.get_text(), 
                            self.senCad.get_text())#método pegar dados da classe controle,pega os dados dos inputs,envia para o encapsualmento da modelo.
                               
        self.modAdm = Admin()
        
        if con.null_fields(self.nomCad.get_text(),self.nomUseCad.get_text(),self.carCad.get_text(),self.senCad.get_text(),self.conSenCad.get_text()) == True:
            self.labAvi.set_text("Campos em branco, por favor, preenchelos")
        if con.senhasDiferem(self.senCad.get_text(),self.conSenCad.get_text()) == True:
            self.labAvi.set_text("senha e confirmação de senha se diferem")
            con.makeFieldsBlank(self.nomCad,self.carCad,self.nomUseCad,self.senCad,self.conSenCad)
      
        else:
        
                control = AdminControle()
                if control.inserir(Admin):
                    DAdm = DadosAdm()
                    DAdm.labAdmName.set_text(pd.adm.getNome())
                    DAdm.labAdmUser.set_text(pd.adm.getUser())
                    DAdm.labAdmCar.set_text(pd.adm.getCargo())
                    self.labAvi.set_text("*Usuário cadastrado com sucesso*")
                    
                    test = control.selecionarTodos()
                    for i in range(0,test.__len__(),1):
                        DAdm.labAdmName.set_text(test[i].getNome())
                        DAdm.labAdmUser.set_text(test[i].getUser())
                        DAdm.labAdmCar.set_text(test[i].getCargo())
            
            
                    
      
     
                        
                   
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/login.glade") 
        self.login = builder.get_object("logWin")
        self.matAlu= builder.get_object("matAlu")
        self.labMat = builder.get_object("labMat")
        self.useAdm = builder.get_object("useAdm")
        self.senAdm = builder.get_object("senAdm")
        self.butLogCad = builder.get_object("butLogCad")
        self.nomCad = builder.get_object("nomCad")
        self.carCad = builder.get_object("carCad")
        self.ExpCad = builder.get_object("ExpCad")
        self.DiaCad = builder.get_object("DiaCad")
        self.boxLog = builder.get_object("boxLog")
        self.nomUseCad = builder.get_object("nomUseCad")
        self.senCad = builder.get_object("senCad")
        self.conSenCad = builder.get_object("conSenCad")
        self.labAvi = builder.get_object("labAvi")
        self.LabTextLoa = builder.get_object("LabTextLoa")
        self.imgLoAD = builder.get_object("imgLoAD")
        self.UserLog = builder.get_object("UserLog")
        self.senLog = builder.get_object("senLog")
        self.butLogAdm = builder.get_object("butLogAdm")
        self.gridLog = builder.get_object("gridLog")
        builder.connect_signals(self)
        self.login.connect("destroy",Gtk.main_quit)
        self.login.show_all()
        CssL = CssLogin()
        CssL.cad_style()
        Gtk.main()
        

        
        
        