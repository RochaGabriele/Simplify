# '''
#Created on 28 de set de 2019

#@author: jefferson Oliveira

#@version: 1.0.1 
#'''
import gi 
from gi.repository import Gtk
from admin.visual.agendaAlu import agendaAlu
from admin.controle.AdminControle import AdminControle
from admin.controle.Conds import Conds
from admin.controle.PegarDadosAdm import PegarDadosAdm
from admin.modelo.Admin import Admin
from admin.visual.CssLogin import CssLogin
from admin.visual.DadosAlu import DadosAlu
from admin.visual.teste import teste


gi.require_version("Gtk","3.0")

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
          
    #Método para fazer login do administrador             
    def entrarAdm(self,evt):
        con = Conds()#instâcia da classe controle conds
        #Verifica se os campos estão em branco
        if con.CamposEmbrancoLog(self.useAdm.get_text(),self.senAdm.get_text()) == True :
            self.labAvi.set_text("Não deixe campo em branco")
        
           
        #Senão Executar um método de seleção para verificar se aquele usuário está no banco
        else:
            control = AdminControle()#instância da classe controle
            test = control.selecionarTodos()
            print(test)#execução do selecionar
            print(self.useAdm.get_text())#printa o que a pessoa digitou no campo usuário
            print(self.senAdm.get_text())#printa o que a pessoa digitou no campo senha
            for i in range(0,test.__len__(),1):#varredura na tabela admin no banco
                #verifica se os campos correspondem com o que está no banco
                if(self.useAdm.get_text() == test[i].getUser() and self.senAdm.get_text() == test[i].getSenha()):
                    tes = teste()#instância da classe teste
                    tes.setIdAdmin(test[i].getId())
                    tes.labAdmNom.set_text(test[i].getNome())#mudando o que está na tela de dados pessoais no lab de cada um, pelo o que está no banco
                    tes.labAdmCa.set_text(test[i].getCargo())
                    tes.labAdmUse.set_text(test[i].getUser())
                    self.login.hide()
                    tes.inst.show()
                else:
                    print("Usuário não existente")
            
            
            
           
    def cadasAdm(self,evt):
        con = Conds()
        pd = PegarDadosAdm()
        pd.getDadosCad(self.nomCad.get_text(), 
                            self.carCad.get_text(), 
                            self.nomUseCad.get_text(), 
                            self.senCad.get_text())#método pegar dados da classe controle,pega os dados dos inputs,envia para o encapsualmento da modelo.
                               
        
        if con.null_fields(self.nomCad.get_text(),self.nomUseCad.get_text(),self.carCad.get_text(),self.senCad.get_text(),self.conSenCad.get_text()) == True:
            self.labAvi.set_text("Campos em branco, por favor, preenchelos")
        if con.senhasDiferem(self.senCad.get_text(),self.conSenCad.get_text()) == True:
            self.labAvi.set_text("senha e confirmação de senha se diferem")
            con.makeFieldsBlank(self.nomCad,self.carCad,self.nomUseCad,self.senCad,self.conSenCad)
        else:
            try:
                adm = Admin()
                adm.setNome(self.nomCad.get_text())
                adm.setCargo(self.carCad.get_text())
                adm.setUser(self.nomUseCad.get_text())
                adm.setSenha(self.senCad.get_text())
                control = AdminControle()
                if control.inserir(adm,evt):
                    self.labAvi.set_text("*Usuário cadastrado com sucesso*")
                else:
                    print("erro")
            except Exception as e:
                    print("Erro geral",str(e))
                    
            
            
    def apagarCampos(self,evt):
         
        self.nomCad.set_text("")
        self.carCad.set_text("")
        self.nomUseCad.set_text("")
        self.senCad.set_text("")
        self.conSenCad.set_text("")
      
    def LoginAluno(self,evt):
        con = Conds()
        if con.Campos_em_branco(self.matAlu.get_text()) == True:
            self.labMat.set_text("Campo em branco, preencha")
        else:
            control = AdminControle()
            log = control.selecionarTodosAes()
            for i in range(0,log.__len__(),1):   
                if(self.matAlu.get_text() == str(log[i].getMatricula())):
                    al = agendaAlu()
                    al.labMatUser.set_text(log[i].getMatricula())
                    al.labNomAlu.set_text(log[i].getNomeAlu())
                    al.labSerUser.set_text(log[i].getSerie())
                    al.labCursoUser.set_text(log[i].getCurso())
                    al.janela.show_all()
                else:
                    self.labMat.set_text("Usuário não existente")
            
            
                           
                           
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("admin/visual/login.glade") 
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
        Gtk.main.quit()
        

        
        
        # '''
#Created on 28 de set de 2019

#@author: jeff

#@version: 1.0.1 
#'''
import gi 
from gi.repository import Gtk


gi.require_version("Gtk","3.0")

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
          
    #Método para fazer login do administrador             
    def entrarAdm(self,evt):
        con = Conds()#instâcia da classe controle conds
        #Verifica se os campos estão em branco
        if con.CamposEmbrancoLog(self.useAdm.get_text(),self.senAdm.get_text()) == True :
            self.labAvi.set_text("Não deixe campo em branco")
        
           
        #Senão Executar um método de seleção para verificar se aquele usuário está no banco
        else:
            control = AdminControle()#instância da classe controle
            test = control.selecionarTodos()
            print(test)#execução do selecionar
            print(self.useAdm.get_text())#printa o que a pessoa digitou no campo usuário
            print(self.senAdm.get_text())#printa o que a pessoa digitou no campo senha
            for i in range(0,test.__len__(),1):#varredura na tabela admin no banco
                #verifica se os campos correspondem com o que está no banco
                if(self.useAdm.get_text() == test[i].getUser() and self.senAdm.get_text() == test[i].getSenha()):
                    tes = teste()#instância da classe teste
                    tes.setIdAdmin(test[i].getId())
                    tes.labAdmNom.set_text(test[i].getNome())#mudando o que está na tela de dados pessoais no lab de cada um, pelo o que está no banco
                    tes.labAdmCa.set_text(test[i].getCargo())
                    tes.labAdmUse.set_text(test[i].getUser())
                    self.login.hide()
                    tes.inst.show()
                else:
                    print("Usuário não existente")
            
            
            
           
    def cadasAdm(self,evt):
        con = Conds()
        pd = PegarDadosAdm()
        pd.getDadosCad(self.nomCad.get_text(), 
                            self.carCad.get_text(), 
                            self.nomUseCad.get_text(), 
                            self.senCad.get_text())#método pegar dados da classe controle,pega os dados dos inputs,envia para o encapsualmento da modelo.
                               
        
        if con.null_fields(self.nomCad.get_text(),self.nomUseCad.get_text(),self.carCad.get_text(),self.senCad.get_text(),self.conSenCad.get_text()) == True:
            self.labAvi.set_text("Campos em branco, por favor, preenchelos")
        if con.senhasDiferem(self.senCad.get_text(),self.conSenCad.get_text()) == True:
            self.labAvi.set_text("senha e confirmação de senha se diferem")
            con.makeFieldsBlank(self.nomCad,self.carCad,self.nomUseCad,self.senCad,self.conSenCad)
        else:
            try:
                adm = Admin()
                adm.setNome(self.nomCad.get_text())
                adm.setCargo(self.carCad.get_text())
                adm.setUser(self.nomUseCad.get_text())
                adm.setSenha(self.senCad.get_text())
                control = AdminControle()
                if control.inserir(adm,evt):
                    self.labAvi.set_text("*Usuário cadastrado com sucesso*")
                else:
                    print("erro")
            except Exception as e:
                    print("Erro geral",str(e))
                    
            
            
    def apagarCampos(self,evt):
         
        self.nomCad.set_text("")
        self.carCad.set_text("")
        self.nomUseCad.set_text("")
        self.senCad.set_text("")
        self.conSenCad.set_text("")
      
    def LoginAluno(self,evt):
        con = Conds()
        if con.Campos_em_branco(self.matAlu.get_text()) == True:
            self.labMat.set_text("Campo em branco, preencha")
        else:
            control = AdminControle()
            log = control.selecionarTodosAes()
            for i in range(0,log.__len__(),1):   
                if(self.matAlu.get_text() == str(log[i].getMatricula())):
                    al = agendaAlu()
                    al.labMatUser.set_text(log[i].getMatricula())
                    al.labNomAlu.set_text(log[i].getNomeAlu())
                    al.labSerUser.set_text(log[i].getSerie())
                    al.labCursoUser.set_text(log[i].getCurso())
                    al.janela.show_all()
                else:
                    self.labMat.set_text("Usuário não existente")
            
            
                           
                           
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("admin/visual/login.glade") 
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
        

        
        
        
