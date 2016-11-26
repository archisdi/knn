#Library untuk membaca file excel
from xlrd import open_workbook

#Library untuk menduplikat file excel
from xlutils.copy import copy

#Package buat sendiri
from classification import knn as kn

#buka file training dan testing
book1 = open_workbook("Train.xls")
book2 = open_workbook("Test2.xls")
bookwr = copy(book2)

datatrain = book1.sheet_by_index(0)
datatest = book2.sheet_by_index(0)
wr = bookwr.get_sheet(0)

#Main Program
for i in range(1, datatest.nrows):
    item = []
    for j in range(1, datatest.ncols):
        item.append(datatest.cell(i, j).value)
    result = (kn.determine(kn, item, datatrain))
    print(i,' = ', result)
    wr.write(i, 11, result)
wr.write(0,11,'y')
bookwr.save('Classified.xls')