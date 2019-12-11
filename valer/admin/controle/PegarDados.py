'''
Created on 16 de nov de 2019

@author: jeff
'''
from modelo.graficosUm import graficosUm
from modelo.graficosDois import graficosDois
from modelo.graficosTres import graficosTres
class PegarDados():
 
    gd = graficosDois()
    def getGraphDois(self,a,b,c,d,e,f,g,h,i,j):
        self.gd.setFev(a)
        self.gd.setMar(b)
        self.gd.setAbr(c)
        self.gd.setMai(d)
        self.gd.setJun(e)
        self.gd.setAgo(f)
        self.gd.setSete(g)
        self.gd.setOutu(h)
        self.gd.setNov(i)
        self.gd.setDez(j)
        
    
    gu =  graficosUm()
    def getGraphUm(self,f,g,h,i,j):
        self.gu.setAgo(f)
        self.gu.setSete(g)
        self.gu.setOutu(h)
        self.gu.setNov(i)
        self.gu.setDez(j)


    gt = graficosTres();
    def getGraphTres(self,a,b,c,d,e):
        self.gt.setFev(a)
        self.gt.setMar(b)
        self.gt.setAbr(c)
        self.gt.setMai(d)
        self.gt.setJun(e)

        
        
    