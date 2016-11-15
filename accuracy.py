from xlrd import open_workbook
from xlutils.copy import copy
import math
from collections import Counter

book1 = open_workbook("Train.xls")
book2 = open_workbook("Test3.xls")

bookwr = copy(book2)

train = book1.sheet_by_index(0)
test = book2.sheet_by_index(0)
wr = bookwr.get_sheet(0)

def classification(item):
    trainres = []
    for i in range(1, train.nrows):
        item2 = []
        for j in range(1, train.ncols):
            item2.append(train.cell(i, j).value)
        trainres.append((euclidean_distance(item, item2), train.cell(i, 11).value))
    trainres = sorted(trainres)
    # return trainres
    trainres = Counter(elem[1] for elem in trainres[0:501])
    # print(trainres)
    if (trainres[0] > trainres[1]):
        return 0
    else:
        return 1

def euclidean_distance(x1, x2):
    x = 0
    for i in range(10):
        x = x + math.pow((x2[i] - x1[i]), 2)
    return math.sqrt(x)

wr.write(0,12,'T')
wr.write(0,13,'A')

cont = []
for i in range(1, test.nrows):
    item = []
    for j in range(1, test.ncols):
        item.append(test.cell(i, j).value)
    temp = (classification(item))
    temp2 = int(train.cell(i, 11).value)
    print(temp,'-',temp2)
    wr.write(i, 12, temp)
    if(temp == temp2):
        wr.write(i, 13, 1)
        cont.append(1)
    else:
        wr.write(i, 13, 0)
        cont.append(0)

temp3 = Counter(cont)

acc = (100 / test.nrows) * temp3[1]
wr.write(0, 14, 'accuracy')
wr.write(1, 14, acc)

bookwr.save('Accuracy.xls')