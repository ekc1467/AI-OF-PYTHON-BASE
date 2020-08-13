import openpyxl

filename = "sample.xlsx"

book = openpyxl.load_workbook(filename)

sheet = book.worksheets[1]
sheetname = book.sheetnames;
