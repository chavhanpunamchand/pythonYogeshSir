from openpyxl import Workbook
import time

wb = Workbook()
sheet = wb.active

sheet['A1'] = 78
sheet['A2'] = "Punamchand"
sheet['A3'] = 51.24
sheet['A4'] = 10

now = time.strftime("%x")
sheet['A5'] = now

wb.save("sample_file.xlsx")