'''
Created on 16 de nov de 2019

@author: jeff
'''
from admin.modelo.Admin import Admin
from admin.modelo.Aluno import Aluno


class PegarDadosAdm():
    def getDadosCad(self,a,b,c,d):
        adm = Admin()
        adm.setNome(a)
        adm.setCargo(b) 
        adm.setUser(c)
        adm.setSenha(d)

        
    #só pra teste
    def getDadosAlu(self,m):
        self.alu = Aluno()
        self.alu.setMatricula(m)
        print(self.alu.getMatricula())
        
        
    