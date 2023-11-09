import pandas as pd
import numpy as np
data = {'A': [1, 2, np.nan, 4, 5],
'B': [np.nan, 2, 3, np.nan, 5],
'C': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
df.isna()
