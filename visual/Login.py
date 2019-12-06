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
            teste = control.selecionarTodos()
            for i in range(0,teste.__len__(),1):
                    print("Usuário:",teste[i].getUser())
                    print("Senha:",teste[i].getSenha())
                    user = teste[i].getUser()
                    senha = teste[i].getSenha()
            print(self.useAdm.get_text())
            print(self.senAdm.get_text())
            if user == self.useAdm.get_text() and senha == teste[i].getSenha():
                adm = DadosAdm()
                adm.dpAdm.show()
            
            
            
            
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
            try:
                admin = Admin()#instância da classe admin
                admin.setNome(admin.getNome())#encapsulamento recebe os dados que o usuário digita tudo para adicionar o banco
                admin.setCargo(admin.getCargo())
                admin.setUser(admin.getUser())
                admin.setSenha(admin.getSenha())
                control  = AdminControle()
                if control.inserir(admin):
                    dAdm = DadosAdm()
                    dAdm.labAdmName.set_text(pd.adm.getNome())
                    dAdm.labAdmUser.set_text(pd.adm.getUser())
                    dAdm.labAdmCar.set_text(pd.adm. getCargo())
                    self.labAvi.set_text("*Usuário cadastrado com sucesso*")
                    """
                    test = control.selecionarTodos()
                    for i in range(0,test.__len__(),1):
                        dAdm.labAdmName.set_text(test[i].getNome())
                        dAdm.labAdmUser.set_text(test[i].getUser())
                        dAdm.labAdmCar.set_text(test[i].getCargo())
            
                """
                    
      
            except Exception as e:
                print("Erro geral:",e)
           
                        
                   
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("visual/login.glade") 
        self.login = builder.get_object("logWin")
        self.matAlu= builder.get_object("matAlu")
        self.labMat = builder.get_object("labMat")
        self.useAdm = builder.get_object("useAdm")
        self.senAdm = builder.get_object("senAdm")
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
        Gtk.main()
        

        
        
        