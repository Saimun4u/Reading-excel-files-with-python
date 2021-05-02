import openpyxl
import os

os.chdir('C:\\Users\\Saimun\\Python ardit\\reading excel xls')

workbook = openpyxl.load_workbook('example.xlsx')

print(type(workbook))