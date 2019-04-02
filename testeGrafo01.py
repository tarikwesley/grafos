class Grafo:
        def __init__(self):
            self.qtVertice = 0
            self.grauVertice = 0
            self.ponderado = 0
            self.listaVertices = []

        def setQtVertice(self, qt):
            self.qtVertice = qt

        def getQtVertice(self):
            return self.qtVertice

        def setGrauVertice(self, grau):
            self.grauVertice = grau

        def getGrauVertice(self):
            return self.grauVertice

        def setPonderado(self, pd):
            self.ponderado = pd

        def getPonderado(self):
            return self.qtVertice

class Vertice:
        def __init__(self):
            self.info = None
            self.qtVerticesAdjacentes = 0
            self.arestas = []
            self.pesos = []

        def setInfo(self, inf):
            self.info = inf

        def getInfo(self):
            return self.info

        def setQtVerticesAdjacentes(self, qt):
            self.qtArestas = qt

        def getQtVerticesAdjacentes(self):
            return self.qtArestas

#Iniciando Grafo
grafo = Grafo()

grafo.setQtVertice(int(input("Forneça o número de vertices: ")))
grafo.setGrauVertice(int(input("Forneça o grau máximo dos vertices: ")))
grafo.setPonderado(int(input("É ponderado? 1 - Sim, 0 - Não: ")))

#Define o nome dos vertices
for i in range(0, grafo.getQtVertice(), 1):
    vertice = Vertice()
    vertice.setInfo(input("Forneça o nome do {}º vertice: ".format(i+1)))
    grafo.listaVertices.append(vertice)

#Define os vertices adjecentes
for i in range(0, grafo.getQtVertice(), 1):
    qtArestas = int(input("Forneca a quantidade de arestas do vertice {}: ".format(grafo.listaVertices[i].getInfo())))
    while qtArestas > grafo.getGrauVertice():
        qtArestas = int(input("Erro, insira um valor menor que o grau maximo dos vertices: "))
    grafo.listaVertices[i].setQtVerticesAdjacentes(qtArestas)
    for j in range(0, grafo.listaVertices[i].getQtVerticesAdjacentes(), 1):
        grafo.listaVertices[i].arestas.append(input("Forneca o {}º vertice adjacente: ".format(j+1)))

#Organização de grafo
for i in range(0, grafo.getQtVertice(), 1):
    for j in range(0, grafo.getQtVertice(), 1):
        if grafo.listaVertices[i].getInfo() in grafo.listaVertices[j].arestas:
            if not(grafo.listaVertices[j].getInfo() in grafo.listaVertices[i].arestas):
                grafo.listaVertices[i].arestas.append(grafo.listaVertices[j].getInfo())

#Pesos
if (grafo.ponderado != 0):
    for i in range(0, len(grafo.listaVertices), 1):
        for j in range(0, len(grafo.listaVertices[i].arestas), 1):
            grafo.listaVertices[i].pesos.append(int(input("Forneça o peso da {}º aresta do vertice {}: ".format(j+1, grafo.listaVertices[i].getInfo()))))

#Imprime o grafo
print("\nGrafo:\n")
for i in range(0, len(grafo.listaVertices), 1):
    print("{}:".format(grafo.listaVertices[i].getInfo()), end="")
    for j in range(0, len(grafo.listaVertices[i].arestas), 1):
        if (grafo.ponderado != 0):
            peso = grafo.listaVertices[i].pesos[j]
        else:
            peso = "-"
        print(" -{}- {}".format(peso, grafo.listaVertices[i].arestas[j]), end="")
    print("\n")
