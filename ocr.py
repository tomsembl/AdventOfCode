# from PIL import Image as ImagePIL
# from json import dumps
# from img2table.ocr import TesseractOCR
# from img2table.document import Image

# src = r"C:\temp\A\9XOY1MvHcO.bmp"
# # image = ImagePIL.open(src)
# # thresh = 128
# # fn = lambda x : 255 if x > thresh else 0
# # image = image.convert('L').point(fn, mode='1')
# # image.save(src)
# image = Image(src,detect_rotation=False)
# ocr = TesseractOCR(n_threads=1, lang="eng")

# # Table extraction
# extracted_tables = image.extract_tables(ocr=ocr,
#                                       #implicit_rows=False,
#                                       borderless_tables=True,
#                                       min_confidence=50)

# for table in extracted_tables:
#     print(table)
#     for i in table.content:
#         print(table.content[i])
#         for cell in table.content[i]:
#             print(cell.value)
#         print() 
#         #print(", ".join([row.text for row in table.content[i]]))
            
#             # for cell in row:
#             #     print(cell.text)

import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=CND1433P80\GTILOCALSQL;DATABASE=master;trusted_connection=yes')
cnxn.autocommit = True
cursor = cnxn.cursor()

cursor.execute("SELECT name FROM sys. databases")
cursor.execute("drop database [3D Oil Limited HYR 31 December 2022_50830fac-24d0-4b91-bd05-b0d2b0e0321e_00000000-0000-0000-0000-000000000000]")
for row in cursor.fetchall():
    print(row)