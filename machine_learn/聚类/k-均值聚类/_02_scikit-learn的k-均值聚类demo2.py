from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from  sklearn.cluster import KMeans

x, y = make_blobs(n_samples=150,
                 centers=3,
                 cluster_std=0.5,
                 shuffle=True,
                 random_state=0)


plt.scatter(x[:,0],
            x[:,1],
            c='white',
            marker='o',
            edgecolors='black',
            s=50)

"""P220"""
km = KMeans(n_clusters=3,  # 期望集群设置为3
            init='random', # random 经典的k-means聚类算法
            n_init=10,   # 执行10次独立的k-均值聚类算法
            max_iter=300,  #每次运行的最大迭代数
            tol=1e-04,          #控制集群内误差平方和的变化以定义收敛标准
            random_state=0)

y_km =km.fit_predict(x)
plt.grid()
plt.show()