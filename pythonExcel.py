import xlrd
import xlsxwriter
filePath="/home/hidden/Documentos/excel.xls"

openFile= xlrd.open_workbook(filePath)
wb = openFile.sheet_by_name('Hoja1')
for i in range(0,wb.nrows):
    print(wb.cell_value(i,0),'\t',wb.cell_value(i,1),'\t',wb.cell_value(i,2),'\t',wb.cell_value(i,3))

openFile.xlsxwriter()