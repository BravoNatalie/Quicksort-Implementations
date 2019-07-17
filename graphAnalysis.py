import matplotlib.pyplot as plt

files = ["results_method_1.txt", "results_method_2.txt",
         "results_method_3.txt", "results_method_4.txt"]

randomness_Level = {1: '< 0.3', 2: '<= 0.7', 3: '> 0.7'}

def creatTable(files):
    result_tab = list()

    for i, file in enumerate(files):
        method = i + 1
        with open(file, 'r') as reader:
            line = reader.readline()

            while line:
                line = line.rstrip('\n').split()
                randLv = int(line[0].split('_')[2])
                time = float(line[-1])
                instance = int(line[0].split('_')[-1].rstrip('.txt'))
                line = [instance, method, randLv, time]
                result_tab.append(line)
                line = reader.readline()

    return result_tab

def plot(title, xlabel, ylabel, data):
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.plot(data.values(),data.keys())
    plt.show()


result_tab = creatTable(files)

############ EXEMPLO:

m1R1 = {}
for line in result_tab:
    if(line[1] == 1 and line[2] == 1):
        dot = {line[0]: line[-1]}
        m1R1.update(dot)

plot("Método 1 & Randomização 1: Tamanho x Tempo", "Tamanho das Instancias", "Tempo (s)", m1R1)



