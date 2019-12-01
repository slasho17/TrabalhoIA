import matplotlib.pyplot as plt
from matplotlib import style
colors = 10*["g", "r", "c", "b", "m", "y", "tab:purple",
             "tab:gray", "tab:orange", "tab:pink",
             "tab:brown", "darkblue", "aquamarine"]


def main():
    monkey = open('monkey.txt')
    g = open('c2ds3-2g.txt')
    sp = open('c2ds1-2sp.txt')

    f = input('Qual arquivo quer plotar?\n')
    opcao = input('qual o tipo 1:g, 2:sp, 3:monkey\n')
    file = open(f)
    dataSet = []
    element = []
    c = 0
    if opcao == '1':
        for line in g:
            for word in line.split():
                if(word == 'sample_label'):  # ignore the first line
                    break

                if(line.split().index(word) == 0):
                    element.append(word)
                else:
                    element.append(float(word))  # capting the data
            if(element):
                dataSet.append(element)
                c += 1
            element = []
        sp.close()
        for line in file:
            aux = []
            for word in line.split():
                if(line.split().index(word) == 0):
                    aux = word
                else:
                    for el in dataSet:
                        if aux == el[0]:
                            el.append(int(word))
                            break
    if opcao == '2':
        for line in sp:
            for word in line.split():
                if(word == 'sample_label'):  # ignore the first line
                    break

                if(line.split().index(word) == 0):
                    element.append(word)
                else:
                    element.append(float(word))  # capting the data
            if(element):
                dataSet.append(element)
                c += 1
            element = []
        sp.close()
        for line in file:
            aux = []
            for word in line.split():
                if(line.split().index(word) == 0):
                    aux = word
                else:
                    for el in dataSet:
                        if aux == el[0]:
                            el.append(int(word))
                            break
    if opcao == '3':
        for line in monkey:
            for word in line.split():
                if(word == 'sample_label'):  # ignore the first line
                    break

                if(line.split().index(word) == 0):
                    element.append(word)
                else:
                    element.append(float(word))  # capting the data
            if(element):
                dataSet.append(element)
                c += 1
            element = []
        monkey.close()
        for line in file:
            aux = []
            for word in line.split():
                if(line.split().index(word) == 0):
                    aux = word
                else:
                    for el in dataSet:
                        if aux == el[0]:
                            el.append(int(word))
                            break
    #
    for w in dataSet:
        print(w)
        w[3] = int(w[3])
    g.close()
    sp.close()
    monkey.close()
    file.close()

    for w in dataSet:
        plt.scatter(w[1], w[2], marker="*",
                    color=colors[w[3]], s=4, linewidths=4)

    plt.savefig('imgs/' + f.replace('clu', 'png'))


main()
