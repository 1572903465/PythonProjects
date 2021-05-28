from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from  sklearn.cluster import KMeans

x, y = make_blobs(n_samples=150,
                 centers=3,
                 cluster_std=0.5,
                 shuffle=True,
                 random_state=0)




"""P220"""
km = KMeans(n_clusters=3,  # 期望集群设置为3
            init='k-means++',  # init 的属性设置为k-means++
            n_init=10,   # 执行10次独立的k-均值聚类算法
            max_iter=300,  #每次运行的最大迭代数
            tol=1e-04,          #控制集群内误差平方和的变化以定义收敛标准
            random_state=0)
y_km =km.fit_predict(x)

print(type(y_km))

"""P220-P221"""

plt.scatter(x[y_km == 0,0],
            x[y_km == 0,1],
            s=50, c='lightgreen',
            marker ='s',edgecolors='black',
            label = 'cluster 1'
            )

plt.scatter(x[y_km == 1,0],
            x[y_km == 1,1],
            s=50, c='orange',
            marker='o',edgecolors='black',
            label = 'cluster 2'

            )

plt.scatter(x[y_km == 2,0],
            x[y_km == 2,1],
            s=50, c='lightblue',
            marker='v',edgecolors='black',
            label = 'cluster 3'
           )

plt.scatter(km.cluster_centers_[:,0],
            km.cluster_centers_[:,1],
            s = 250, marker='*',
            c = 'red', edgecolors='black',
            label = 'centroids'
           )
plt.legend(scatterpoints = 1)
plt.grid()
plt.show()