import pandas as pd
import numpy as np
from scipy.spatial.distance import  pdist,squareform
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.cluster.hierarchy import set_link_color_palette
from matplotlib import pyplot as plt
from sklearn.cluster import  AgglomerativeClustering
np.random.seed(123)
varivables = ['X','Y','Z']
labels =['ID_0', 'ID_1', 'ID_2', 'ID_3', 'ID_4']
x = np.random.random_sample([5,3])*10
df = pd.DataFrame(x, columns=varivables, index=labels)
print(df)

row_dist = pd.DataFrame(squareform((pdist(df,metric='euclidean'))),# euclidean欧几里得距离
                        columns=labels, index=labels)
print(row_dist)

# row_clusters = linkage(pdist(df,metric='euclidean'),method='complete')
row_clusters = linkage(df.values,metric='euclidean',method='complete')
print(row_clusters)

df_cluser = pd.DataFrame(row_clusters,
             columns=['row label1','row labels2','disrace','no. of items in clust.'],
             index=['cluster %d'%(i+1) for i in range(row_clusters.shape[0])])

print(df_cluser)

row_dendr = dendrogram(row_clusters,
                       labels= labels,
                       # make dendrogram black (part 2/2)
                       # color_threshold = np.inf
                       )
plt.tight_layout()
plt.ylabel('Euclidean diatance')
plt.show()

ac = AgglomerativeClustering(n_clusters=2,affinity='euclidean',linkage='complete')
labels = ac.fit_predict(x)
print("Cluster labels %s"%labels)

