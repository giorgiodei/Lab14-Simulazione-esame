import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self._cromosomi=[]

    def creaGrafo(self):

        self._grafo.clear()
        self._cromosomi = DAO.getNodes()
        self._grafo.add_nodes_from(self._cromosomi)
        self._minimo_valore=None
        self._massimo_valore=None

        coppie=DAO.getEdges()

        for c in coppie:
            c1 = c["c1"]
            c2 = c["c2"]
            peso=DAO.getPeso(c1,c2)
            if self._minimo_valore is None:
                self._minimo_valore=peso
            if self._massimo_valore is None:
                self._massimo_valore=peso
            if peso>self._massimo_valore:
                self._massimo_valore=peso
            if peso<self._minimo_valore:
                self._minimo_valore=peso
            self._grafo.add_edge(c1, c2, weight=peso)


    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def getMinimoeMassimoValore(self):
        return self._minimo_valore, self._massimo_valore

    def getValoriSopraSoglia(self, valore):
        numeroSopra=0
        for a,b,peso in self._grafo.edges:
            if peso>=valore:
                numeroSopra+=1
        return numeroSopra

    def getValoriSottoSoglia(self, valore):
        numeroSotto = 0
        for a, b, peso in self._grafo.edges:
            if peso <= valore:
                numeroSotto += 1
        return numeroSotto