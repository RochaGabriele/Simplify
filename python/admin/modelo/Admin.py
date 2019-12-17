'''
Created on 7 de nov de 2019

@author: jefferson Oliveira
'''

class Admin():
    
    __id = ""
    __nome = ""
    __cargo = ""
    __user = ""
    __senha = ""

#getters

    def getId(self):
        return self.__id
    def getNome(self):
        return self.__nome 
    def getCargo(self):
        return self.__cargo
    def getUser(self):
        return self.__user
    def getSenha(self):
        return self.__senha
    
#setters
    def setId(self,ide):
        self.__id = ide
    def setNome(self,nome):
        self.__nome = nome
    def setCargo(self,cargo):
        self.__cargo = cargo
    def setUser(self,user):
        self.__user  = user
    def setSenha(self,senha):
        self.__senha = senha
        
        
