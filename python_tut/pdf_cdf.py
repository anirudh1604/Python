import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
iris=pd.read_csv("iris.csv")
iris_setosa=iris[iris.species=='setosa']
iris_versicolor=iris[iris.species=='versicolor']
iris_virginica=iris[iris.species=='virginica']
#setosa
counts,bin_edges=np.histogram(iris_setosa['petal_length'],bins=20,density=True)
pdf=counts/sum(counts)
print(pdf)
print(bin_edges)

cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)


#versicolor
'''counts,bin_edges=np.histogram(iris_versicolor['petal_length'],bins=10,density=True)
pdf=counts/sum(counts)
print(pdf)
print(bin_edges)

cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)

#virginica
counts,bin_edges=np.histogram(iris_virginica['petal_length'],bins=20,density=True)
pdf=counts/sum(counts)
print(pdf)
print(bin_edges)

cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)
'''
plt.show()

