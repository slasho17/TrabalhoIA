import math as math
import random as random
import numpy as numpy
import plots as plots
import objects as objects
from scipy.spatial import distance


def sorting(elem):
    return elem.y


class averageLink:
    def __init__(self, kMin, kMax, data, path):
        self.numero = 0
        self.kMin = kMin
        self.kMax = kMax
        self.kTotal = kMax-kMin
        self.path = path
        self.data = data
        # uma lista com todos os clusters, organizada da seguinte forma = self.clusters = [[[x0,y0]],[[x1,y1],[x2,y2]]], nesse caso a lista tem dois clusters, o primeiro tem um elemento apenas, e o segundo tem dois
        self.clusters = [[i] for i in data]
        # a quantidade de cluster que tem no mundo, vai mudar cada vez que ocorre um merge em algum cluster
        self.nClusters = len(data)
        # a quantidade de informacoes que tem no mundo, provavelmente nao vai ser usada
        self.rows = len(data)
        # mantem uma tabela onde o indice é a posicao dos cluster em self.cluster, as informacoes sao a distancia entre os dois cluster
        self.mable()
        self.minList = []
        # contem duas posicoes de clusters(indices da lista self.cluster), dos dois clusters mais proximos um do outro

    def fit(self):
        while(self.nClusters > self.kMin):
            self.mable()
            print(self.nClusters)
            aux = self.minList[0].a
            self.clusters[aux] += self.clusters[self.minList[0].b]
            del(self.clusters[self.minList[0].b])
            self.nClusters -= 1
            if(self.nClusters <= self.kMax):
                pat = "fakeClusters/" + self.path + \
                    "avg" + str(self.nClusters) + '.clu'
                printPartition(pat, self)
                plots.averageLink(self)
            #self.atualizarTable(self.minTuple[0], self.minTuple[1])

    # recebe dois clusters e retorna a distancia minima entre dois clusters

    def findMinDist(self, i, j):
        if(i == j):
            return 0
        x = 0
        k = 0
        l = 0
        z = 0
        w = 0
        for a in i:
            z += a.data[0]
            w += a.data[1]
            x += 1
        z = z/x
        w = w/x
        x = 0
        for a in j:
            k += a.data[0]
            l += a.data[1]
            x += 1
        k = k/x
        l = l/x

        return round(distance.euclidean([z, w], [k, l]), 4)

    def mable(self):
        a = 0
        minList = []
        for i in self.clusters:
            b = 0
            print(a)
            for j in self.clusters:
                if(a > b):
                    y = self.findMinDist(i, j)
                    aux = objects.ot(a, b, y)
                    minList.append(aux)
                b = b+1
            a = a+1
        minList.sort(key=sorting)
        print(minList[0].y)
        print(minList[0].a)
        print(minList[0].b)

        self.minList = minList


def printPartition(path, cluster):
    file = open(path, 'w')
    if(cluster.path == 'monkey'):
        a = 1
    else:
        a = 0

    for i in cluster.clusters:
        for l in i:
            for k in cluster.data:
                if l.nome == k.nome:
                    k.cluster = a
                    break
        a += 1

    for each in cluster.data:
        file.write(str(each.nome) + ' ' + str(each.cluster)+'\n')


class singleLink:
    def __init__(self, kMin, kMax, data, path):
        self.numero = 0
        self.kMin = kMin
        self.kMax = kMax
        self.kTotal = kMax-kMin
        self.path = path
        self.data = data
        # uma lista com todos os clusters, organizada da seguinte forma = self.clusters = [[[x0,y0]],[[x1,y1],[x2,y2]]], nesse caso a lista tem dois clusters, o primeiro tem um elemento apenas, e o segundo tem dois
        self.clusters = [[i] for i in data]
        # a quantidade de cluster que tem no mundo, vai mudar cada vez que ocorre um merge em algum cluster
        self.nClusters = len(data)
        # a quantidade de informacoes que tem no mundo, provavelmente nao vai ser usada
        self.rows = len(data)
        # mantem uma tabela onde o indice é a posicao dos cluster em self.cluster, as informacoes sao a distancia entre os dois cluster
        self.mable()
        self.minList = []
        # contem duas posicoes de clusters(indices da lista self.cluster), dos dois clusters mais proximos um do outro

    def fit(self):
        while(self.nClusters > self.kMin):
            self.mable()
            print(self.nClusters)
            aux = self.minList[0].a
            self.clusters[aux] += self.clusters[self.minList[0].b]
            del(self.clusters[self.minList[0].b])
            self.nClusters -= 1
            if(self.nClusters <= self.kMax):
                pat = "fakeClusters/" + self.path + \
                    "single" + str(self.nClusters) + '.clu'
                printPartition(pat, self)
                plots.singleLink(self)
            #self.atualizarTable(self.minTuple[0], self.minTuple[1])

    # recebe dois clusters e retorna a distancia minima entre dois clusters

    def findMinDist(self, i, j):
        if(i == j):
            return 0
        dist = math.inf
        for a in i:
            for b in j:
                x = distance.euclidean(a.data, b.data)
                if (dist > x):
                    dist = x
        return round(dist, 4)

    def mable(self):
        a = 0
        minList = []
        for i in self.clusters:
            b = 0
            print(a)
            for j in self.clusters:
                if(a > b):
                    y = self.findMinDist(i, j)
                    aux = objects.ot(a, b, y)
                    minList.append(aux)
                b = b+1
            a = a+1
        minList.sort(key=sorting)
        print(minList[0].y)
        print(minList[0].a)
        print(minList[0].b)

        self.minList = minList


class kMeans:

    def __init__(self, nClusters, nIterations, data, path):
        self.nClusters = nClusters  # int com a quantidade
        self.nIterations = nIterations  # int com a quantidade
        self.data = data  # array com objects
        self.rows = len(data)  # int com a quantidade de linhas
        self.path = path
        # inicializa os centroides
        centroids = []
        for i in range(nClusters):
            centroids.append(data[random.randint(0, self.rows-1)])

        # array com posicoes dos centroids, tipo x e y, que são objects tambem
        self.centroids = centroids

        # inicializa dataCentroid com [] para ser uzada em findCentroidForDataPoint
        dataCentroid = []
        for i in range(self.rows):
            # array de int com o numero do centroid para cada posicao de dado
            dataCentroid.append([])
        self.dataCentroid = dataCentroid  # lista de int

        # inicializa cada dado para seu respectivo centroide
        auxit = self.rows
        for dataPos in range(auxit):
            self.findCentroidForDataPoint(dataPos)

        partitions = [[]for i in range(self.nClusters)]
        for j in range(auxit):
            partitions[self.dataCentroid[j]].append(self.data[j])
        self.partitions = partitions  # lista de listas de objects

    def findCentroidForDataPoint(self, dataPos):
        for i in range(self.nClusters):
            if(self.dataCentroid[dataPos] == []):
                self.dataCentroid[dataPos] = i

            distanceNow = float(distance.euclidean(
                self.centroids[self.dataCentroid[dataPos]].data, self.data[dataPos].data))

            newDistance = float(distance.euclidean(
                self.centroids[i].data, self.data[dataPos].data))

            if(distanceNow > newDistance):
                self.dataCentroid[dataPos] = i

    def fit(self):
        a = 0
        for i in range(self.nIterations):
            print(a)
            a += 1
            self.remakeCentroids()
            for dataPos in range(self.rows):
                self.findCentroidForDataPoint(dataPos)

            self.setPartitions()
        for j in range(self.rows):
            self.data[j].cluster = self.dataCentroid[j]

    def remakeCentroids(self):
        a = 0
        for p in self.partitions:
            x = 0
            y = 0
            l = 0
            for d in p:
                x += d.data[0]
                y += d.data[1]
                l += 1
            if l == 0:
                l = 1
            self.centroids[a].data[0] = x/l
            self.centroids[a].data[1] = y/l
            a = a+1

    def setPartitions(self):
        self.partitions = [[]
                           for i in range(self.nClusters)]  # reset partitions
        for j in range(self.rows):
            self.partitions[self.dataCentroid[j]].append(
                self.data[j])  # findin new partitions
