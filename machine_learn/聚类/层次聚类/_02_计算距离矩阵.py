import pandas as pd
import numpy as np
from scipy.spatial.distance import  pdist,squareform
np.random.seed(123)
varivables = ['X','Y','Z']
labels =['ID_0', 'ID_1', 'ID_2', 'ID_3', 'ID_4']
x = np.random.random_sample([5,3])*10
df = pd.DataFrame(x, columns=varivables, index=labels)
print(df)

row_dist = pd.DataFrame(squareform(
                        (pdist(df,metric='euclidean'))), # euclidean欧几里得距离
                        columns=labels, index=labels)
print(row_dist)

