def main():
    monkeyT = open('monkeys.txt', 'w')
    g = open('c2ds3-2g.txt', 'w')
    sp = open('c2ds1-2sp.txt', 'w')

    f = input('Qual arquivo quer plotar?\n')
    opcao = input('qual o tipo 1:g, 2:sp, 3:monkey\n')
    file = open(f, 'w')
    dataSet = []
    nome = 'nada'
    c = 0
    if(opcao == 1):
        for line in g:
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
        g.close()
        for line in file:
            for el in dataSet:
                if line[0] == el[0]:
                    el.append(line[1])
                    break

        for w in dataSet:
            print(w)
