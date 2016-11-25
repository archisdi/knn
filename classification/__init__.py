import math
from collections import Counter

class knn:
    def determine(self, item, train):
        trainres = []
        rows = train.nrows
        k = int((rows/180)+1)
        for i in range(1, rows):
            item2 = []
            for j in range(1, train.ncols):
                item2.append(train.cell(i, j).value)
            trainres.append((knn.euclidean_distance(knn, item, item2), train.cell(i, 11).value))
        trainres = sorted(trainres)
        trainres = Counter(elem[1] for elem in trainres[0:k])
        if (trainres[0] > trainres[1]):
            return 0
        else:
            return 1

    def euclidean_distance(self, x1, x2):
        x = 0
        for i in range(len(x1)):
            x = x + math.pow((x2[i] - x1[i]), 2)
        return math.sqrt(x)