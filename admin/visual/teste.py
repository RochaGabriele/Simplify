'''
    @author: Jefferson Oliveira, Gabriele Rocha
'''
import gi
from gi.repository import Gtk

from admin.controle.AdminControle import AdminControle
from admin.controle.Conds import Conds
from admin.modelo.Admin import Admin
from admin.modelo.Aluno import Aluno
from admin.visual.CadAluCss import CadAluCss
from admin.visual.testecss import testecss
from admin.visual.pontuC import pontuC

gi.require_version("Gtk","3.0")
class teste:
    __idAdmin = ""

    def getIdAdmin(self):
        return self.__idAdmin
    def setIdAdmin(self,i):
        self.__idAdmin = i
        
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("admin/visual/lista.glade")
        self.inst = builder.get_object("winLista")
        self.labAdmNom = builder.get_object("labAdmNom")
        self.labAdmUse = builder.get_object("labAdmUse")
        self.labAdmCa = builder.get_object("labAdmCa")
        #informatica
        #serie
        self.infSerie0 = builder.get_object("infSerie0")
        self.infSerie1 = builder.get_object("infSerie1")
        self.infSerie2 = builder.get_object("infSerie2")
        self.infSerie3 = builder.get_object("infSerie3")
        self.infSerie4 = builder.get_object("infSerie4")
        self.infSerie5 = builder.get_object("infSerie5")
        self.infSerie6 = builder.get_object("infSerie6")
        self.infSerie7 = builder.get_object("infSerie7")
        self.infSerie8 = builder.get_object("infSerie8")
        self.infSerie9 = builder.get_object("infSerie9")
        self.infSerie10 = builder.get_object("infSerie10")
        self.infSerie11 = builder.get_object("infSerie11")
        self.infSerie12 = builder.get_object("infSerie12")
        self.infSerie13 = builder.get_object("infSerie13")
        self.infSerie14 = builder.get_object("infSerie14")
        self.infSerie15 = builder.get_object("infSerie15")
        self.infSerie16 = builder.get_object("infSerie16")
        self.infSerie17 = builder.get_object("infSerie17")
       
        #nome
        self.aluInfor0 = builder.get_object("aluInfor0")
        self.aluInfor1 = builder.get_object("aluInfor1")
        self.aluInfor2= builder.get_object("aluInfor2")
        self.aluInfor3 = builder.get_object("aluInfor3")
        self.aluInfor4 = builder.get_object("aluInfor4")
        self.aluInfor5 = builder.get_object("aluInfor5")
        self.aluInfor6 = builder.get_object("aluInfor6")
        self.aluInfor7 = builder.get_object("aluInfor7")
        self.aluInfor8 = builder.get_object("aluInfor8")
        self.aluInfor9 = builder.get_object("aluInfor9")
        self.aluInfor10 = builder.get_object("aluInfor10")
        self.aluInfor11 = builder.get_object("aluInfor11")
        self.aluInfor12 = builder.get_object("aluInfor12")
        self.aluInfor13 = builder.get_object("aluInfor13")
        self.aluInfor14 = builder.get_object("aluInfor14")
        self.aluInfor15 = builder.get_object("aluInfor15")
        self.aluInfor16 = builder.get_object("aluInfor16")
        self.aluInfor17 = builder.get_object("aluInfor17")
        
        #editarInfor
        self.infEdit0 = builder.get_object("infEdit0")
        self.infEdit1 = builder.get_object("infEdit1")
        self.infEdit2 = builder.get_object("infEdit2")
        self.infEdit3 = builder.get_object("infEdit3")
        self.infEdit4 = builder.get_object("infEdit4")
        self.infEdit5 = builder.get_object("infEdit5")
        self.infEdit6 = builder.get_object("infEdit6")
        self.infEdit7 = builder.get_object("infEdit7")
        self.infEdit8 = builder.get_object("infEdit8")
        self.infEdit9 = builder.get_object("infEdit9")
        self.infEdit10 = builder.get_object("infEdit10")
        self.infEdit11 = builder.get_object("infEdit11")
        self.infEdit12 = builder.get_object("infEdit12")
        self.infEdit13 = builder.get_object("infEdit13")
        self.infEdit14 = builder.get_object("infEdit14")
        self.infEdit15 = builder.get_object("infEdit15")
        self.infEdit16 = builder.get_object("infEdit16")
        self.infEdit17 = builder.get_object("infEdit17")
        #deletarinfor
        self.infDel0 = builder.get_object("infDel0")
        self.infDel1 = builder.get_object("infDel1")
        self.infDel2 = builder.get_object("infDel2")
        self.infDel3 = builder.get_object("infDel3")
        self.infDel4 = builder.get_object("infDel4")
        self.infDel5 = builder.get_object("infDel5")
        self.infDel6 = builder.get_object("infDel6")
        self.infDel7 = builder.get_object("infDel7")
        self.infDel8 = builder.get_object("infDel8")
        self.infDel9 = builder.get_object("infDel9")
        self.infDel10 = builder.get_object("infDel10")
        self.infDel11 = builder.get_object("infDel11")
        self.infDel12 = builder.get_object("infDel12")
        self.infDel13 = builder.get_object("infDel13")
        self.infDel14 = builder.get_object("infDel14")
        self.infDel15 = builder.get_object("infDel15")
        self.infDel16 = builder.get_object("infDel16")
        self.infDel17 = builder.get_object("infDel17")
        #enfermagem
        #serie
        self.enfSerie0 = builder.get_object("enfSerie0")
        self.enfSerie1 = builder.get_object("enfSerie1")
        self.enfSerie2 = builder.get_object("enfSerie2")
        self.enfSerie3 = builder.get_object("enfSerie3")
        self.enfSerie4 = builder.get_object("enfSerie4")
        self.enfSerie5 = builder.get_object("enfSerie5")
        self.enfSerie6 = builder.get_object("enfSerie6")
        self.enfSerie7 = builder.get_object("enfSerie7")
        self.enfSerie8 = builder.get_object("enfSerie8")
        self.enfSerie9 = builder.get_object("enfSerie9")
        self.enfSerie10 = builder.get_object("enfSerie10")
        self.enfSerie11 = builder.get_object("enfSerie11")
        self.enfSerie12 = builder.get_object("enfSerie12")
        self.enfSerie13 = builder.get_object("enfSerie13")
        self.enfSerie14 = builder.get_object("enfSerie14")
        self.enfSerie15 = builder.get_object("enfSerie15")
        self.enfSerie16 = builder.get_object("enfSerie16")
        self.enfSerie17 = builder.get_object("enfSerie17")
        #nome
        self.enfAlu0 = builder.get_object("enfAlu0")
        self.enfAlu1 = builder.get_object("enfAlu1")
        self.enfAlu2 = builder.get_object("enfAlu2")
        self.enfAlu3 = builder.get_object("enfAlu3")
        self.enfAlu4 = builder.get_object("enfAlu4")
        self.enfAlu5 = builder.get_object("enfAlu5")
        self.enfAlu6 = builder.get_object("enfAlu6")
        self.enfAlu7 = builder.get_object("enfAlu7")
        self.enfAlu8 = builder.get_object("enfAlu8")
        self.enfAlu9 = builder.get_object("enfAlu9")
        self.enfAlu10 = builder.get_object("enfAlu10")
        self.enfAlu11 = builder.get_object("enfAlu11")
        self.enfAlu12 = builder.get_object("enfAlu12")
        self.enfAlu13 = builder.get_object("enfAlu13")
        self.enfAlu14 = builder.get_object("enfAlu14")
        self.enfAlu15 = builder.get_object("enfAlu15")
        self.enfAlu16 = builder.get_object("enfAlu16")
        self.enfAlu17 = builder.get_object("enfAlu17")
        #eventur
        #serie
        self.etSerie0 = builder.get_object("etSerie0")
        self.etSerie1 = builder.get_object("etSerie1")
        self.etSerie2 = builder.get_object("etSerie2")
        self.etSerie3 = builder.get_object("etSerie3")
        self.etSerie4 = builder.get_object("etSerie4")
        self.etSerie5 = builder.get_object("etSerie5")
        self.etSerie6 = builder.get_object("etSerie6")
        self.etSerie7 = builder.get_object("etSerie7")
        self.etSerie8 = builder.get_object("etSerie8")
        self.etSerie9 = builder.get_object("etSerie9")
        self.etSerie10 = builder.get_object("etSerie10")
        self.etSerie11 = builder.get_object("etSerie11")
        self.etSerie12 = builder.get_object("etSerie12")
        self.etSerie13 = builder.get_object("etSerie13")
        self.etSerie14 = builder.get_object("etSerie14")
        self.etSerie15 = builder.get_object("etSerie15")
        self.etSerie16 = builder.get_object("etSerie16")
        self.etSerie17 = builder.get_object("etSerie17")
        #nome
        self.etAlu0 = builder.get_object("etAlu0")
        self.etAlu1 = builder.get_object("etAlu1")
        self.etAlu2 = builder.get_object("etAlu2")
        self.etAlu3 = builder.get_object("etAlu3")
        self.etAlu4 = builder.get_object("etAlu4")
        self.etAlu5 = builder.get_object("etAlu5")
        self.etAlu6 = builder.get_object("etAlu6")
        self.etAlu7 = builder.get_object("etAlu7")
        self.etAlu8 = builder.get_object("etAlu8")
        self.etAlu9 = builder.get_object("etAlu9")
        self.etAlu10 = builder.get_object("etAlu10")
        self.etAlu11 = builder.get_object("etAlu11")
        self.etAlu12 = builder.get_object("etAlu12")
        self.etAlu13 = builder.get_object("etAlu13")
        self.etAlu14 = builder.get_object("etAlu14")
        self.etAlu15 = builder.get_object("etAlu15")
        self.etAlu16 = builder.get_object("etAlu16")
        self.etAlu17 = builder.get_object("etAlu17")

        builder.connect_signals(self)
        tes = testecss()
        tes.ctes()
        self.mostrarAlunosInfor()
        self.mostrarAlunosEnf()
        self.mostrarAlunosEvenTur()
        self.inst.show_all()
        self.inst.connect("destroy",Gtk.main_quit)
    
    
    def upd(self):
        builder = Gtk.Builder()
        builder.add_from_file("admin/visual/upd.glade")
        self.upda = builder.get_object("winUpd")
        builder.connect_signals(self)
        self.upda.show_all()
        self.upda.connect("destroy",Gtk.main_quit)
        
    def window1(self):
        builder = Gtk.Builder()
        builder.add_from_file("admin/visual/NovUm.glade")
        self.NovUm = builder.get_object("winEnt")   
        ##self.gtk_style()
        builder.connect_signals(self)
        self.NovUm.show_all()
        self.NovUm.connect("destroy", Gtk.main_quit)
        Gtk.main()

    def window2(self):
        builder = Gtk.Builder()
        builder.add_from_file("admin/visual/NovDoi.glade")
        self.NovDoi = builder.get_object("winCom")       
        builder.connect_signals(self)
        self.NovDoi.connect("destroy", Gtk.main_quit)
        ##self.gtk_style()
        self.NovDoi.show_all()
        
    def window3(self):
        builder = Gtk.Builder()
        builder.add_from_file("admin/visual/NovTre.glade")
        self.NovTre = builder.get_object("winRec")       
        builder.connect_signals(self)
        self.NovTre.connect("destroy", Gtk.main_quit)
        ##self.gtk_style()
        self.NovTre.show_all()
        
    def window4(self):
        builder = Gtk.Builder()
        builder.add_from_file("admin/visual/repro.glade")
        self.repro = builder.get_object("winRep")       
        builder.connect_signals(self)
        self.repro.connect("destroy", Gtk.main_quit)
        ##self.gtk_style()
        self.repro.show_all()
            
    def window5(self):
        builder = Gtk.Builder()
        builder.add_from_file("admin/visual/apro.glade")
        self.apro = builder.get_object("winApro")       
        builder.connect_signals(self)
        self.apro.connect("destroy", Gtk.main_quit)
        #self.gtk_style()
        self.apro.show_all()
    
    def window6(self):
        builder = Gtk.Builder()
        builder.add_from_file("admin/visual/media.glade")
        self.media = builder.get_object("winAvaliar")  
        self.atraso = builder.get_object("cbtAtr")
        self.assiduo = builder.get_object("cbtAss")
        self.ocorrencia = builder.get_object("cbtOco")
        self.postura = builder.get_object("cbtPos")
        self.desempenho = builder.get_object("cbtDes")     
        builder.connect_signals(self)
        self.media.connect("destroy", Gtk.main_quit)
        self.media.show_all()
        
    def window7(self):
        builder = Gtk.Builder()
        builder.add_from_file("admin/visual/cadastro.glade")
        self.cadastro = builder.get_object("winCadastro") 
        self.entNome = builder.get_object("entNome")
        self.entMatricula = builder.get_object("entMatricula")
        self.cbtCurso = builder.get_object("cbtCurso")
        self.cbtSerie = builder.get_object("cbtSerie")
        self.cadLab  = builder.get_object("cadLab")
        builder.connect_signals(self)
        self.cadastro.connect("destroy", Gtk.main_quit)
        CadA = CadAluCss()
        CadA.cadStyle()
        self.cadastro.show_all()
    def Editar(self):
        builder = Gtk.Builder()
        builder.add_from_file("admin/visual/Modificar.glade")
        self.modWin = builder.get_object("modWin")
        self.nomAt = builder.get_object("nomAt")
        self.userAt= builder.get_object("userAt")
        self.carAt = builder.get_object("carAt")
        self.senAt = builder.get_object("senAt")
        self.conSenAt = builder.get_object("conSenAt")
        self.btnCar = builder.get_object("btnCar")
        self.btnAtual = builder.get_object("btnAtual")
        self.top = builder.get_object("top")
        builder.connect_signals(self)
        self.mostrar()
        self.modWin.connect("destroy",Gtk.main_quit)
        self.modWin.show_all()
        
   
    #métodos dos dados do administrador
    def mostrar(self):
        control = AdminControle()
        test = control.selecionarTodos()
        for i in range(0,test.__len__(),1):#varredura na tabela admin no banco
            #verifica se os campos correspondem com o que está no banco
            self.labAdmNom.set_text(test[i].getNome())#muda o que está na tela de dados pessoais no lab de cada um, pelo o que está no banco
            self.labAdmCa.set_text(test[i].getCargo())
            self.labAdmUse.set_text(test[i].getUser())
    def modificar(self,evt):
        self.inst.hide()
        self.Editar()
    def Edit(self,evt):
        try:
            admin = Admin()
            admin.setId(self.getIdAdmin())
            admin.setNome(self.nomAt.get_text())
            admin.setUser(self.userAt.get_text())
            admin.setCargo(self.carAt.get_text())
            admin.setSenha(self.conSenAt.get_text())
            control = AdminControle()
            if(control.update(admin)):
                self.modWin.hide()
                self.inst.show_all()
                test = control.selecionarTodos()
                for i in range(0,test.__len__(),1):#varredura na tabela admin no banco
                #verifica se os campos correspondem com o que está no banco
                    self.setIdAdmin(test[i].getId())
                    self.labAdmNom.set_text(test[i].getNome())#muda o que está na tela de dados pessoais no lab de cada um, pelo o que está no banco
                    self.labAdmCa.set_text(test[i].getCargo())
                    self.labAdmUse.set_text(test[i].getUser())
                    self.modWin.hide()
                    self.inst.show()
                else:
                    print("Usuário não existente")
            else:
                print("Tá retornando falso")
        except Exception as e:
            print("Erro geral",str(e))
    def cancelType(self,evt):
        self.modWin.hide()
        self.inst.show_all()
    #metodos de cadastro do aluno
    def Cadastrar(self,evt):
        conds = Conds()
        if conds.camposEmBracoCad(self.entNome.get_text(),self.entMatricula.get_text()) == True:
            self.entNome.set_text("Campo em branco, preencha com o nome")
            self.entMatricula.set_text("Campo em branco, preencha com a matricula")
        else:
        
            try:
                alu = Aluno()
                alu.setNomeAlu(self.entNome.get_text())
                alu.setCurso(self.cbtCurso.get_active_text())
                alu.setSerie(self.cbtSerie.get_active_text())
                alu.setMatricula(self.entMatricula.get_text())
                control = AdminControle()
                if(control.inserirAlu(alu,evt)):
                       
                        self.cadastro.hide()
                        self.inst.show()
                                            
                else:
                        print("Erro")
            except Exception as e:
                print("Erro geral",str(e))   
                
    def mostrarAlunosInfor(self):
        try:
            control = AdminControle()
            inf  = control.selectInfor()
            print(inf)
            for a in range(0,1,1):
                self.infSerie0.set_text(inf[a].getSerie())
                self.aluInfor0.set_text(inf[a].getNomeAlu())
            for b in range(1,2,1):
                self.infSerie1.set_text(inf[b].getSerie())
                self.aluInfor1.set_text(inf[b].getNomeAlu())
            for c in range(2,3,1):
                self.infSerie2.set_text(inf[c].getSerie())
                self.aluInfor2.set_text(inf[c].getNomeAlu())
            for d in range(3,4,1):
                self.infSerie3.set_text(inf[d].getSerie())
                self.aluInfor3.set_text(inf[d].getNomeAlu())
            for e in range(4,5,1):
                self.infSerie4.set_text(inf[e].getSerie())
                self.aluInfor4.set_text(inf[e].getNomeAlu())
            for f in range(5,6,1):
                self.infSerie5.set_text(inf[f].getSerie())
                self.aluInfor5.set_text(inf[f].getNomeAlu())
            for g in range(6,7,1):
                self.infSerie6.set_text(inf[g].getSerie())
                self.aluInfor6.set_text(inf[g].getNomeAlu())
            for h in range(7,8,1):
                self.infSerie7.set_text(inf[h].getSerie())
                self.aluInfor7.set_text(inf[h].getNomeAlu())
            for i in range(8,9,1):
                self.infSerie8.set_text(inf[i].getSerie())
                self.aluInfor8.set_text(inf[i].getNomeAlu())
            for j in range(9,10,1):
                self.infSerie9.set_text(inf[j].getSerie())
                self.aluInfor9.set_text(inf[j].getNomeAlu())
            for k in range(10,11,1):
                self.infSerie10.set_text(inf[k].getSerie())
                self.aluInfor10.set_text(inf[k].getNomeAlu())
            for l in range(11,12,1):
                self.infSerie11.set_text(inf[l].getSerie())
                self.aluInfor11.set_text(inf[l].getNomeAlu())
            for m in range(12,13,1):
                self.infSerie12.set_text(inf[m].getSerie())
                self.aluInfor12.set_text(inf[m].getNomeAlu())
            for n in range(13,14,1):
                self.infSerie13.set_text(inf[n].getSerie())
                self.aluInfor13.set_text(inf[n].getNomeAlu())
            for o in range(14,15,1):
                self.infSerie14.set_text(inf[o].getSerie())
                self.aluInfor14.set_text(inf[o].getNomeAlu())
            for p in range(15,16,1):
                self.infSerie15.set_text(inf[p].getSerie())
                self.aluInfor15.set_text(inf[p].getNomeAlu())
            for q in range(16,17,1):
                self.infSerie16.set_text(inf[q].getSerie())
                self.aluInfor16.set_text(inf[q].getNomeAluno())
            for r in range(17,18,1):
                self.infSerie17.set_text(inf[r].getSerie())
                self.aluInfor17.set_text(inf[r].getNomeAlu())
        except Exception as e:
            print ("erro",str(e))
    def mostrarAlunosEnf(self):
        try:
            control = AdminControle()
            enf = control.selectEnfer()
            for a in range(0,1,1):
                #modifica as series
                self.enfSerie0.set_text(enf[a].getSerie())
                self.enfAlu0.set_text(enf[a].getNomeAlu())
            for b in range(1,2,1):
                self.enfSerie1.set_text(enf[b].getSerie())
                self.enfAlu1.set_text(enf[b].getNomeAlu())
            for c in range(2,3,1):
                self.enfSerie2.set_text(enf[c].getSerie())
                self.enfAlu2.set_text(enf[c].getNomeAlu())
            for d in range(3,4,1):
                self.enfSerie3.set_text(enf[d].getSerie())
                self.enfAlu3.set_text(enf[d].getNomeAlu())
            for e in range(4,5,1):
                self.enfSerie4.set_text(enf[e].getSerie())
                self.enfAlu4.set_text(enf[e].getNomeAlu())
            for f in range(5,6,1):
                self.enfSerie5.set_text(enf[f].getSerie())
                self.enfAlu5.set_text(enf[f].getNomeAlu())
            for g in range(6,7,1):
                self.enfSerie6.set_text(enf[g].getSerie())
                self.enfAlu6.set_text(enf[g].getNomeAlu())
            for h in range(7,8,1):
                self.enfSerie7.set_text(enf[h].getSerie())
                self.enfAlu7.set_text(enf[h].getNomeAlu())
            for i in range(8,9,1):
                self.enfSerie8.set_text(enf[i].getSerie())
                self.enfAlu8.set_text(enf[i].setNomeAlu())
            for j in range(9,10,1):
                self.enfSerie9.set_text(enf[j].getSerie())
                self.enfAlu9.set_text(enf[j].getNomeAlu())
            for k in range(10,11,1):
                self.enfSerie10.set_text(enf[k].getSerie())
                self.enfAlu10.set_text(enf[k].getNomeAlu())
            for l in range(11,12,1):
                self.enfSerie11.set_text(enf[l].getSerie())
                self.enfAlu11.set_text(enf[l].getNomeAlu())
            for m in range(12,13,1):
                self.enfSerie12.set_text(enf[m].getSerie())
                self.enfAlu12.set_text(enf[m].getNomeAlu())
            for n in range(13,14,1):
                self.enfSerie13.set_text(enf[n].getSerie())
                self.enfAlu13.set_text(enf[n].getNomeAlu())
            for o in range(14,15,1):
                self.enfSerie14.set_text(enf[o].getSerie())
                self.enfAlu14.set_text(enf[o].getNomeAlu())
            for p in range(15,16,1):
                self.enfSerie15.set_text(enf[p].getSerie())
                self.enfAlu15.set_text(enf[p].getNomeAlu())
            for q in range(16,17,1):
                self.enfSerie16.set_text(enf[q].getSerie())
                self.enfAlu16.set_text(enf[q].getNomeAlu())
            for r in range(17,18,1):
                self.enfSerie17.set_text(enf[r].getSerie())
                self.enfAlu17.set_text(enf[r].getNomeAlu())
        except Exception as e:
            print("erro geral:",str(e))
    def mostrarAlunosEvenTur(self):
        try:
            control = AdminControle()
            evtu = control.selectEvenTur()
            for a in range(0,1,1):
                self.etSerie0.set_text(evtu[a].getSerie())
                self.etAlu0.set_text(evtu[a].getNomeAlu())
            for b in range(1,2,1):
                self.etSerie1.set_text(evtu[b].getSerie())
                self.etAlu1.set_text(evtu[b].getNomeAlu())
            for c in range(2,3,1):
                self.etSerie2.set_text(evtu[c].getSerie())
                self.etAlu2.set_text(evtu[c].getNomeAlu())
            for d in range(3,4,1):
                self.etSerie3.set_text(evtu[d].getSerie())
                self.etAlu3.set_text(evtu[d].getNomeAlu())
            for e in range(4,5,1):
                self.etSerie4.set_text(evtu[e].getSerie())
                self.etAlu4.set_text(evtu[e].getNomeAlu())
            for f in range(5,6,1):
                self.etSerie5.set_text(evtu[f].getSerie())
                self.etAlu5.set_text(evtu[f].getNomeAlu())
            for g in range(6,7,1):
                self.etSerie6.set_text(evtu[g].getSerie())
                self.etAlu6.set_text(evtu[g].getNomeAlu())
            for h in range(7,8,1):
                self.etSerie7.set_text(evtu[h].getSerie())
                self.etAlu7.set_text(evtu[h].getNomeAlu())
            for i in range(8,9,1):
                self.etSerie8.set_text(evtu[i].getSerie())
                self.etAlu8.set_text(evtu[i].getNomeAlu())
            for j in range(9,10,1):
                self.etSerie9.set_text(evtu[j].getSerie())
                self.etAlu9.set_text(evtu[j].getNomeAlu())
            for k in range(10,11,1):
                self.etSerie10.set_text(evtu[k].getSerie())
                self.etAlu10.set_text(evtu[k].getNomeAlu())
            for l in range(11,12,1):
                self.etSerie11.set_text(evtu[l].getSerie())
                self.etAlu11.set_text(evtu[l].getNomeAlu())
            for m in range(12,13,1):
                self.etSerie12.set_text(evtu[m].getSerie())
                self.etAlu12.set_text(evtu[m].getNomeAlu())
            for n in range(13,14,1):
                self.etSerie13.set_text(evtu[n].getSerie())
                self.etAlu13.set_text(evtu[n].getNomeAlu())
            for o in range(14,15,1): 
                self.etSerie14.set_text(evtu[o].getSerie())
                self.etAlu14.set_text(evtu[o].getNomeAlu())
            for p in range(15,16,1):
                self.etSerie15.set_text(evtu[p].getSerie())
                self.etAlu15.set_text(evtu[p].getNomeAlu())
            for q in range(16,17,1):
                self.etSerie16.set_text(evtu[q].getSerie())
                self.etAlu16.set_text(evtu[q].getNomeAlu())
            for r in range(17,18,1):
                self.etSerie17.set_text(evtu[r].getSerie())
                self.etAlu17.set_text(evtu[r].getNomeAlu())
    #métodos do list    
        except Exception as e:
            print("Erro geral:", str(e))
    def editar(self,evt):
        self.upd()
        
    def remover(self,evt):
        pass
    
    def avaliar(self,evt):
        self.inst.hide()
        self.window1()
        
    def entendi(self,evt):
        self.NovUm.hide()
        self.window2()
        
    def comecar(self,evt):
        self.NovDoi.hide()
        self.window3()
        
    def naodeu(self,evt):
        self.NovTre.hide()
        self.window4()
        
    def prox(self,evt):
        self.NovTre.hide()
        self.window6()
     
    def calNovA(self,evt):
        self.apro.hide()
        self.window7()
    
    def calNovR(self,evt):
        self.repro.hide()
        self.window3()
        
    def mostra(self,evt):
        self.ok = pontuC()
        m = self.ok.calc(self.atraso.get_active_text(),self.assiduo.get_active_text(),self.ocorrencia.get_active_text(),self.postura.get_active_text(),self.desempenho.get_active_text())
        if m < 35:
            self.media.hide()
            self.window4()
        else:
            self.media.hide()
            self.window5()
            
    def algoBanco(self,evt):
        self.ok = pontuC()
        
    def canUpd(self,evt):
        self.upda.destroy()
        
    def closGra(self,evt):
        self.graficos.destroy()
        
    def bacDois(self,evt):
        self.NovDoi.destroy()
        self.window1()
        
    def canRepro(self,evt):
        self.repro.destroy()
        
    def canApro(self,evt):
        self.apro.destroy()
   
