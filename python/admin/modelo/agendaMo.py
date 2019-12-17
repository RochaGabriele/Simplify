'''
@author:José Maik
'''

class agendaMo:
    "OBJETOS SALA"
    __idSal = 0
    __priSala = ""
    __segSala = ""
    __terSala = ""
    __quarSala = ""
    __quiSala = ""
    __sexSala = ""
    __setSala = ""
    __oiSala = ""
    __noSala = ""
    "OBJETOS ALUNOS"
    __idAE = 0
    __priAE = ""
    __segAE = ""
    __terAE = ""
    __quarAE = ""
    __quiAE = ""
    __sexAE = ""
    __setAE = ""
    __oiAE = ""
    __noAE = ""
    
    "GETTERS SALAS"
    def getidSal(self):
        return self.__idSal
    def getpriSala(self):
        return self.__priSala
    def getsegSala(self):
        return self.__segSala
    def getterSala(self):
        return self.__terSala
    def getquarSala(self):
        return self.__quarSala
    def getquinSala(self):
        return self.__quinSala
    def getsexSala(self):
        return self.__sexSala
    def getsetSala(self):
        return self.__setSala
    def getoiSala(self):
        return self.__oiSala
    def getnoSala(self):
        return self.__noSala
    
    "SETTERS SALAS"
    def setidSal(self, idSal):
        self.__idSal = idSal
    def setpriSala(self,priSala):
        self.__priSala = priSala
    def setsegSala(self,segSala):
        self.__segSala = segSala
    def setterSala(self,terSala):
        self.__terSala = terSala
    def setquarSala(self,quarSala):
        self.__quarSala = quarSala
    def setquinSala(self,quinSala):
        self.__quinSala = quinSala
    def setsexSala(self,sexSala):
        self.__sexSala = sexSala
    def setsetSala(self,setSala):
        self.__setSala = setSala
    def setoiSala(self,oiSala):
        self.__oiSala = oiSala
    def setnoSala(self,noSala):
        self.__noSala = noSala
        
    "GETTERS ALUNOS"
    def getidAE(self):
        return self.__idAE
    def getpriAE(self):
        return self.__priAE
    def getsegAE(self):
        return self.__segAE
    def getterAE(self):
        return self.__terAE
    def getquarAE(self):
        return self.__quarAE
    def getquiAE(self):
        return self.__quiAE
    def getsexAE(self):
        return self.__sexAE
    def getsetAE(self):
        return self.__setAE
    def getoiAE(self):
        return self.__oiAE
    def getnoAE(self):
        return self.__noAE
    
    "SETTERS ALUNOS"
    def setidAE(self, idAE):
        self.__idAE = idAE
    def setpriAE(self,priAE):
        self.__priAE = priAE
    def setsegAE(self,segAE):
        self.__segAE = segAE
    def setterAE(self,terAE):
        self.__terAE = terAE
    def setquarAE(self,quarAE):
        self.__quarAE =quarAE
    def setquiAE(self,quiAE):
        self.__quiAE = quiAE
    def setsexAE(self,sexAE):
        self.__sexAE = sexAE
    def setsetAE(self,setAE):
        self.__setAE = setAE
    def setoiAE(self,oiAE):
        self.__oiAE = oiAE
    def setnoAE(self,noAE):
        self.__noAE = noAE
