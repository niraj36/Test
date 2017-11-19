import pandas as pd
import fizz_buzz as fb


data = pd.read_csv('C:/_data/Portfolios.csv')
fizzy = fb.fizz_buzz(1, 10000, 3, 5)

return_fields = ['Symbol','Last']
prices = pd.read_csv('C:/_data/Portfolios.csv',usecols=return_fields).drop_duplicates(subset=['Symbol', 'Last'], keep='first')

print(prices)
print(prices)
print(fizzy)
print(fizzy)
print(data)
print(data)
