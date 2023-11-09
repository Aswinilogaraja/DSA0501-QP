import pandas as pd
data = {
    'Item': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],
    'Unit': [100, 150, 120, 130, 110, 160, 130, 140, 170, 120,
             200, 180, 140, 120, 110, 190, 130, 140, 150, 120]
}

df = pd.DataFrame(data)
pivot_table = df.pivot_table(index='Item', values='Unit', aggfunc='sum')

# Rename the column for clarity
pivot_table.columns = ['Total Units Sold']

# Display the pivot table
print(pivot_table)