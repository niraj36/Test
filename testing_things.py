import pandas as pd
import fizz_buzz as fb


data = pd.read_csv('C:/_data/Portfolios.csv')
print(data)

fizzy = fb.fizz_buzz(1, 10000, 3, 5)
print(fizzy)

return_fields = ['Symbol','Last']
prices = pd.read_csv('C:/_data/Portfolios.csv',usecols=return_fields).drop_duplicates(subset=['Symbol', 'Last'], keep='first')
print(prices)


uri = open('C:/_data/DatabaseConnectionSting_test.txt', 'r').read()
print(uri)

import os, sys
qq = sys.path.append(os.getcwd())
print(qq)
