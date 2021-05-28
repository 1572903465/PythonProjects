import pandas as pd
import numpy as np
np.random.seed(123)
varivables = ['X','Y','Z']
lables =['ID_0','ID_1','ID_2','ID_3','ID_4']
x = np.random.random_sample([5,3])*10
df = pd.DataFrame(x, columns=varivables, index=lables)
print(df)