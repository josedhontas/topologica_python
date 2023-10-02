class Grafo:
    def __init__(self):
        self.vertices = []
        self.adjacencias = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices.append(vertice)
            self.adjacencias[vertice] = []

    def adicionar_aresta(self, origem, destino):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.adjacencias[origem].append(destino)

    def ordenacao_topologica(self):
        visitados = {vertice: False for vertice in self.vertices}
        pilha = []

        for vertice in self.vertices:
            if not visitados[vertice]:
                self.ordenacao_topologica_util(vertice, visitados, pilha)

        return pilha

    def ordenacao_topologica_util(self, vertice, visitados, pilha):
        visitados[vertice] = True

        for vizinho in self.adjacencias[vertice]:
            if not visitados[vizinho]:
                self.ordenacao_topologica_util(vizinho, visitados, pilha)

        pilha.insert(0, vertice)
