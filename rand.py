from os import listdir
from os.path import isfile, join
from sklearn import metrics
from operator import itemgetter


def readCluster(path):
    f = open(path)
    p = []
    for linha in f:
        p.append([linha.split()[0], int(linha.split()[1])])
    aux = []
    for pa in p:
        aux.append(pa[1])
    f.close()
    return aux


def main():
    mReal = readCluster('realClusters/monkeyReal1.clu')
    gReal = readCluster('realClusters/c2ds3-2gReal.clu')
    spReal = readCluster('realClusters/c2ds1-2spReal.clu')
    randRes = open('randResult.csv', 'w')
    clus = listdir('fakeClusters')
    aux = []
    for p in clus:
        aux = readCluster('fakeClusters/' + p)
        if p[:5] == 'c2ds3':
            print(p + ',' + str(metrics.adjusted_rand_score(gReal, aux)) + '\n')
            randRes.write(
                p + ',' + str(metrics.adjusted_rand_score(gReal, aux)) + '\n')
        if p[:5] == 'c2ds1':
            print(p + ',' + str(metrics.adjusted_rand_score(spReal, aux)) + '\n')
            randRes.write(
                p + ',' + str(metrics.adjusted_rand_score(spReal, aux)) + '\n')
        if p[:5] == 'monke':
            print(p + ',' + str(metrics.adjusted_rand_score(mReal, aux)) + '\n')
            randRes.write(
                p + ',' + str(metrics.adjusted_rand_score(mReal, aux)) + '\n')


main()
