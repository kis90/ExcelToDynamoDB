import openpyxl
filename = 'Dynamic.xlsx'
xlsx = openpyxl.load_workbook(filename)
sheet = xlsx.active
data = sheet.rows
csv = open("data.csv", "w+")

for row in data:
    l = list(row)
    for i in range(len(l)):
        if i == len(l) - 1:
            csv.write(str(l[i].value))
        else:
            csv.write(str(l[i].value) + ',')
    csv.write('\n')
csv.close()
