#Library untuk membaca file excel
from xlrd import open_workbook

#Library untuk menduplikat file excel
from xlutils.copy import copy

#Package buat sendiri
from classification import knn as kn

#Package untuk menghitung collection
from collections import Counter

book1 = open_workbook("Train.xls")
book2 = open_workbook("Test3.xls")

bookwr = copy(book2)

train = book1.sheet_by_index(0)
test = book2.sheet_by_index(0)
wr = bookwr.get_sheet(0)

wr.write(0,12,'T')
wr.write(0,13,'A')

cont = []
for i in range(1, test.nrows):
    item = []
    for j in range(1, test.ncols):
        item.append(test.cell(i, j).value)
    temp = (kn.determine(kn, item, train))
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