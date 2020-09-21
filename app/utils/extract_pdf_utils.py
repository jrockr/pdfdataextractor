from tabula import read_pdf
from tabulate import tabulate

df = read_pdf("/home/joydeep/git/pdfdataextractor/app/data/data.pdf",pages='1',multiple_tables=True)

print(tabulate(df))