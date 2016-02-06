import csv

f = open('test.csv', 'r')
f2 = csv.writer(open('Rdata.csv', 'r+'))
a = 1
for row in csv.reader(f):
    if a != 1:
        tempList = row.remove(row[0])
        print tempList
        f2.writerow(tempList)
    else:
        a = a+1
f.close()
f2.close()
