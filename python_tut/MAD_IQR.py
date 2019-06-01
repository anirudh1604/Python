import pandas as pd
from statsmodels import robust
import numpy as np
iris=pd.read_csv("iris.csv")
iris_setosa=iris[iris.species=='setosa']
print("MAD")
print (robust.mad(iris_setosa["petal_length"]))
print("\nMedian without Outliner")
print (np.median(iris_setosa["petal_length"]))
print("\nMedian with Outliner")
print (np.median(np.append(iris_setosa["petal_length"],50)))
print("\nMean without Outliner")
print (np.mean(iris_setosa["petal_length"]))
print("\nMean with Outliner")
print (np.mean(np.append(iris_setosa["petal_length"],50)))

print("\nPercentiles")
print (np.percentile(iris_setosa["petal_length"],np.arange(0,100,25)))

print("\n 90th Percentiles")
print (np.percentile(iris_setosa["petal_length"],90))
