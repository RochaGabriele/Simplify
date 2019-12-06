'''
Created on 16 de nov de 2019

@author: jeff
'''
from modelo.Admin import Admin
from modelo.Aluno import Aluno
class PegarDados():
 
    adm = Admin()
       
    
    def getDadosCad(self,a,b,c,d):
        self.adm.setNome(a)
        self.adm.setCargo(b)
        self.adm.setUser(c)
        self.adm.setSenha(d)
      

        
    #só pra teste
    def getDadosAlu(self,m):
        self.alu = Aluno()
        self.alu.setMatricula(m)
        print(self.alu.getMatricula())
        
        
    