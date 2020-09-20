
"""

XLSX to CSV transforms any XLSX file into a series of CSV files based on the XLSX's sheets.

CSV may not contain more than one sheet, so the intention is to ease the process of transforming a multi-sheet .xlsx into several .csv

"""

import pandas as pd 
import numpy as np

path = r'YOUR PATH\yourfile.xlsx'
sheets = ['sheetname1', 'sheetname2'] 

for sheet in sheets:
    splitter = pd.read_excel(path, sheet_name=sheet) 
    splitter.to_csv(f'{sheet}.csv')