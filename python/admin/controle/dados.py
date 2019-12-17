'''
@author: José Maik
'''


from admin.modelo.agendaMo import agendaMo


class dados:
    "INSTANCIAS DA CLASSE AGENDA(SALAS)"
    def salas(self,a,b,c,d,e,f,g,h,i):
        self.m = agendaMo()
        self.m.setpriSala(a)
        self.m.setsegSala(b)
        self.m.setterSala(c)
        self.m.setquarSala(d)
        self.m.setquinSala(e)
        self.m.setsexSala(f)
        self.m.setsetSala(g)
        self.m.setoiSala(h)
        self.m.setnoSala(i)
        print(self.m.getpriSala())
        print(self.m.getsegSala())
        print(self.m.getterSala())
        print(self.m.getquarSala())
        print(self.m.getquinSala())
        print(self.m.getsexSala())
        print(self.m.getsetSala())
        print(self.m.getoiSala())
        print(self.m.getnoSala())
        
    "INSTANCIAS DA CLASSE AGENDA(ALUNOS)"
    def alunos(self,a1,b1,c1,d1,e1,f1,g1,h1,i1):
        self.m = agendaMo()
        self.m.setpriAE(a1)
        self.m.setsegAE(b1)
        self.m.setterAE(c1)
        self.m.setquarAE(d1)
        self.m.setquiAE(e1)
        self.m.setsexAE(f1)
        self.m.setsetAE(g1)
        self.m.setoiAE(h1)
        self.m.setnoAE(i1)
        print(self.m.getidAE())
        print(self.m.getpriAE())
        print(self.m.getsegAE())
        print(self.m.getterAE())
        print(self.m.getquarAE())
        print(self.m.getquiAE())
        print(self.m.getsexAE())
        print(self.m.getsetAE())
        print(self.m.getoiAE())
        print(self.m.getnoAE())
