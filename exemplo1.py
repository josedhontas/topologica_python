from topologica import Grafo

g = Grafo()

g.adicionar_aresta("Cálculo A", "Álgebra Linear")
g.adicionar_aresta("Álgebra Linear", "Cálculo C")
g.adicionar_aresta("Álgebra Linear", "Cálculo B")
g.adicionar_aresta("Cálculo A", "Cálculo B")
g.adicionar_aresta("Cálculo C", "Circuitos")
g.adicionar_aresta("Álgebra Linear", "Equações Diferenciais")
g.adicionar_aresta("Cálculo C", "Equações Diferenciais")


ordem_topologica = g.ordenacao_topologica()


print("Ordem Topológica dos Cursos:")
print(ordem_topologica)
