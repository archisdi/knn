from xlrd import open_workbook
from xlutils.copy import copy
import math
from collections import Counter

book1 = open_workbook("Train.xls")
book2 = open_workbook("Test2.xls")

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


for i in range(1, test.nrows):
    item = []
    for j in range(1, test.ncols):
        item.append(test.cell(i, j).value)
    temp = (classification(item))
    print(temp)
    wr.write(i,11,temp)

bookwr.save('Classified.xls')
