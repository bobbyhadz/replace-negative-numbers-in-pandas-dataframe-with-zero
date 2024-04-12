# Replace negative Numbers in a Pandas DataFrame with Zero

import pandas as pd


df = pd.DataFrame({
    'A': [-1, -2, 0, 1, 2],
    'B': [-3, -4, 3, 4, -5]
})

print(df)

print('-' * 50)

df[df < 0] = 0

print(df)