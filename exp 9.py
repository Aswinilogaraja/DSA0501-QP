import pandas as pd
import numpy as np
df = pd.read_csv('\aswin\OneDrive\Documents\qp\exp 9')
region_pivot = pd.pivot_table(df , values='Sale_amt', index='Region', aggfunc='sum')
manager_pivot = pd.pivot_table(df , values='Sale_amt', index='Manager', aggfunc='sum')
salesperson_pivot = pd.pivot_table(df, values='Sale_amt', index='SalesMan', aggfunc='sum')
print("Total Sale Amount Region-wise:\n", region_pivot)
print("\nTotal Sale Amount Manager-wise:\n", manager_pivot)
print("\nTotal Sale Amount Salesperson-wise:\n", salesperson_pivot)
