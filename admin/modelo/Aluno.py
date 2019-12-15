'''
Created on 7 de nov de 2019

@author: jeff
'''

class Aluno:
    
    __nomeAlu = ""
    __matricula = ""
    __curso = ""
    __serie = ""
#getters 
    
    def getNomeAlu(self):
        return self.__nomeAlu
    def getMatricula(self):
        return self.__matricula
    def getCurso(self):
        return self.__curso
    def getSerie(self):
        return self.__serie
#setters
    def setCurso(self,curso):
        self.__curso = curso
    def setNomeAlu(self,nomeAlu):
        self.__nomeAlu = nomeAlu
    def setMatricula(self,matricula):
        self.__matricula = matricula
    def setSerie(self,serie):
        self.__serie = serie
