import pandas as pd
import openpyxl

df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                  index=['one', 'two', 'three'], columns=['a', 'b', 'c'])

print(df)

df.to_excel('Example.xlsx', sheet_name='new_sheet_name')

#         a   b   c
# one    11  21  31
# two    12  22  32
# three  31  32  33