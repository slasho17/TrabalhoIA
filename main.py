import clustering as clustering
import plots as plots
import numpy as numpy
import objects as objects


def printPartition(path, cluster):
    file = open(path, 'w')
    for each in cluster:
        file.write(str(each.nome) + ' ' + str(each.cluster)+'\n')


def main():
    auxiliar = input(
        "Qual o arquivo que deseja inserir?\n1 = c2ds1-2sp.txt\n2 = c2ds3-2g.txt\n3 = monkey.txt\n")
    if auxiliar == "1":
        p = "c2ds1-2sp"
        path = "bases/c2ds1-2sp.txt"
    elif auxiliar == '2':
        p = "c2ds3-2g"
        path = "bases/c2ds3-2g.txt"
    elif auxiliar == '3':
        p = "monkey"
        path = "bases/monkey.txt"
    # file = pandas.read_csv(path, sep='\t')
    # data = file.iloc[:, :].values
    data = readDataSet(path)
    option = int(input(
        "Qual algoritmo deseja aplicar nesses dados?\n1 = k-means\n2 = single-link\n3 = average-link\n0 = sair\n"))

    if(option == 1):
        print("Voce escolheu o k-means")
        nClusters = int(input("Quantos clusters voce deseja utilizar?\n"))
        nIterations = int(input("Quantas iteracoes voce deseja realizar?\n"))
        # incializa o kmeans
        result = clustering.kMeans(nClusters, nIterations, data, p)
        # itera o kmeans
        result.fit()
        plots.kMeansPlot(result)
        pat = "fakeClusters/" + p + "kMeans" + \
            str(nClusters) + "_" + str(nIterations) + '.clu'
        if(auxiliar == '3'):
            for aaa in result.data:
                aaa.cluster += 1
        printPartition(pat, result.data)

    elif(option == 2):
        print("Voce escolheu o sigle-link")
        kMin = int(input("Qual o minimo de clusters que deseja?\n"))
        kMax = int(input("Qual o maximo de clusters que deseja?\n"))
        result = clustering.singleLink(kMin, kMax, data, p)
        result.fit()

    elif(option == 3):
        print("Voce escolheu o average-link\n")
        kMin = int(input("Qual o minimo de clusters que deseja?\n"))
        kMax = int(input("Qual o maximo de clusters que deseja?\n"))
        # result = clustering.averageLink(kMin, kMax, data)


def readDataSet(name):
    path = name
    print(path)
    file = open(path)
    element = []
    dataSet = []
    nome = 'nada'
    c = 0
    for line in file:
        for word in line.split():
            if(word == 'sample_label'):  # ignore the first line
                break
            else:
                if(line.split().index(word) == 0):
                    nome = word
                else:
                    element.append(float(word))  # capting the data
        if(element):
            novoObjeto = objects.objects(nome, element, c)
            dataSet.append(novoObjeto)
            c += 1
        element = []
    file.close()
    return dataSet


main()
