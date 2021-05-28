from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

x, y = make_blobs(n_samples=150,
                 centers=3,
                 cluster_std=0.5,
                 shuffle=True,
                 random_state=0)
print(x.shape)

print(x)
print(x[:,0],x[:,1])

plt.scatter(x[:,0],
            x[:,1],
            c='white',
            marker='o',
            edgecolors='black',
            s=50)

plt.grid()
plt.show()