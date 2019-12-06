'''
Created on 7 de nov de 2019

@author: jeff
'''

class Aluno:
    
    __nome = ""
    __matricula = ""

#getters 
    
    def getNome(self):
        return self.__nome
    def getMatricula(self):
        return self.__matricula
    
#setters

    def setNome(self,nome):
        self.__nome = nome
    def setMatricula(self,matricula):
        self.__matricula = matricula
