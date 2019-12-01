import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
colors = 10*["g", "r", "c", "b", "m", "y", "tab:purple",
             "tab:gray", "tab:orange", "tab:pink",
             "tab:brown", "darkblue", "aquamarine"]


def singleLink(cluster):
    x = []
    y = []
    for partition in cluster.clusters:
        color = colors[cluster.clusters.index(partition)]
        x = []
        y = []
        for data in partition:
            x.append(data.data[0])
            y.append(data.data[1])
        plt.scatter(x, y, marker="*", color=color, s=4, linewidths=4)

    plt.savefig('imgs/singleLink/' + cluster.path +
                str(cluster.nClusters) + '.png')


def averageLink(cluster):
    x = []
    y = []
    for partition in cluster.clusters:
        color = colors[cluster.clusters.index(partition)]
        x = []
        y = []
        for data in partition:
            x.append(data.data[0])
            y.append(data.data[1])
        plt.scatter(x, y, marker="*", color=color, s=4, linewidths=4)

    plt.savefig('imgs/avgLink/' + cluster.path +
                str(cluster.nClusters) + '.png')


def kMeansPlot(cluster):

    for partition in cluster.partitions:
        color = colors[cluster.partitions.index(partition)]
        x = []
        y = []
        for data in partition:
            x.append(data.data[0])
            y.append(data.data[1])
        plt.scatter(x, y, marker="*", color=color, s=2, linewidths=2)

    plt.savefig('imgs/kMeans/' + cluster.path +
                str(cluster.nClusters) + '.png')
    #
    x = []
    y = []
    z = 0
    for centroid in cluster.centroids:

        z += 1
        x.append(centroid.data[0])
        y.append(centroid.data[1])

    plt.scatter(x, y, marker="o", color="k", s=10, linewidths=5)

    plt.savefig('imgs/kMeans/' + cluster.path +
                str(cluster.nClusters) + '.png')
